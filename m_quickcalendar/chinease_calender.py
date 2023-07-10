from widgets.draw import Canvas
from lib.uiConst import *
from lib.mpy_calendar import LunarDate
import utime
from lib.ufontMem import fonts, BMFont

import math

class ChineaseCalender(Canvas):

    week_cn = ['一', '二', '三', '四', '五', '六', '日']
    solar_terms = ['小寒', '大寒', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种', '夏至',
                   '小暑', '大暑', '立秋', '处暑', '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪', '冬至']
    lunar_holidays = {
        '0101': '春节',
        '0115': '元宵',
        '0505': '端午',
        '0707': '七夕',
        '0815': '中秋',
        '0909': '重阳',
        '1208': '腊八',
        '1224': '小年',
        '0100': '除夕'
    }  # 农历节日表
    sonar_holidays = {
        '0101': '元旦',
        '0214': '情人',
        '0308': '妇女',
        '0312': '植树',
        '0501': '劳动',
        '0504': '青年',
        '0601': '儿童',
        '0701': '建党',
        '0801': '建军',
        '0909': '教师',
        '1001': '国庆',
        '1224': '圣诞'
    }  # 公历节日表
    solar_terms = ['小寒', '大寒', '立春', '雨水', '惊蛰', '春分', '清明', '谷雨', '立夏', '小满', '芒种', '夏至',  # index 0~11
                   '小暑', '大暑', '立秋', '处暑', '白露', '秋分', '寒露', '霜降', '立冬', '小雪', '大雪', '冬至']  # index 12~23

    def __init__(self, solar_time: tuple, **kwargs):
        """
        日历区块，支持键盘焦点选择日期和农历变化
        :param solar_time:
        :param next_btn_id:
        :param prev_btn_id:
        """
        super().__init__(BODY_WIDTH, BODY_HEIGHT, **kwargs)
        self.year = solar_time[0]
        self.month = solar_time[1]
        self.day = solar_time[2]
        self.font12: BMFont = fonts.get(12)

        self.font_arial_bold = fonts[FONT_ARIAL_BLACK_14]
        if self.font_arial_bold is None:
            raise ValueError(f'please init font {FONT_ARIAL_BLACK_14} first')

        self.max_day = 0
        self.week_align = 0

        def handle_key(key_dict: dict[int, bool]):

            nonlocal self
            def go_prev_month():
                nonlocal self
                prev_time = utime.localtime(utime.mktime((self.year, self.month - 1, 1, 0, 0, 0, -1, -1)))  # 上个月1号
                if prev_time[0] <= 2000:
                    return
                self.year = prev_time[0]
                self.month = prev_time[1]
                self.day = prev_time[2]
                self.update()

            def go_next_month():
                nonlocal self
                next_time = utime.localtime(utime.mktime((self.year, self.month + 2, 0, 0, 0, 0, -1, -1)))  # 下个月最后一天
                if next_time[0] >= 2100:
                    return
                self.year = next_time[0]
                self.month = next_time[1]
                self.day = next_time[2]
                self.update()

            continuous = key_dict.get(KEY_LEFT)
            if continuous is not None:
                if continuous:  # 长按换月
                    go_prev_month()
                else:   # 短按换日/功能
                    keys = key_dict.keys()
                    if KEY_LEFT in keys:
                        if self.day > 1:
                            self.day -= 1
                            self.update()
                        else:
                            self.tab_prev()

            continuous = key_dict.get(KEY_RIGHT)
            if continuous is not None:
                if continuous:  # 长按换月
                    go_next_month()
                else:  # 短按换日
                    if self.day < self.max_day:
                        self.day += 1
                        self.update()
                    else:
                        self.tab_next()

            continuous = key_dict.get(KEY_UP)
            if continuous is not None:
                if continuous:  # 长按换年
                    if self.year <= 2001:
                        return
                    prev_time = utime.localtime(
                        utime.mktime((self.year - 1, self.month + 2, 0, 0, 0, 0, -1, -1)))  # 前一年同月第一天
                    self.year = prev_time[0]
                    self.month = prev_time[1]
                    self.day = prev_time[2]
                    self.update()
                else:   # 短按换周/月
                    if self.day - 7 >= 1:
                        self.day -= 7
                        self.update()
                    else:
                        go_prev_month()

            continuous = key_dict.get(KEY_DOWN)
            if continuous is not None:
                if continuous:  # 长按换年
                    if self.year >= 2099:
                        return
                    next_time = utime.localtime(
                        utime.mktime((self.year + 1, self.month + 1, 0, 0, 0, 0, -1, -1)))  # 后一年同月最后一天
                    self.year = next_time[0]
                    self.month = next_time[1]
                    self.day = next_time[2]
                    self.update()
                else:   # 短按换周/月
                    if self.day + 7 <= self.max_day:
                        self.day += 7
                        self.update()
                    else:
                        go_next_month()

        self.key_handler = handle_key
        self.max_day: int = 0
        self.week_align: int = 0
        self.lunars: list[LunarDate | None] = []   # 农历
        self.sonars: list[tuple[int, int, int] | None] = []     # 公历
        self.day_info: list[str] = [''] * 31

        self.update()   # 计算&绘图

    @classmethod
    def __get_solar_term(cls, year, month) -> tuple[int, int]:
        """
        使用寿星公式计算2001~2099年所有节气，输入年月，输出该月的2个节气日期序号
        :param year:
        :param month:
        :return: 该月份的2个节气所在的日期（从1开始）
        """

        # 2001~2099修正字典，key='年份+节气0开始的序号'，在最后输出的时候，进行修正
        fix_dict = {
            '201900': -1,  # 2019小寒-1
            '208201': 1,  # 2082大寒+1
            '202603': -1,  # 2026年雨水-1
            '208405': 1,  # 2084年春分+1
            '200809': 1,  # 2008小满+1
            '200214': 1,  # 2002立秋+1
            '208907': 1,  # 2089霜降+1
            '208908': 1,  # 2089立冬+1
            '202123': -1,  # 2021年冬至-1
        }

        D = 0.2422
        C = [5.4055, 20.12, 3.87, 18.73, 5.63, 20.646, 4.81, 20.1, 5.52, 21.04, 5.678, 21.37, 7.108, 22.83, 7.5, 23.13,
             7.646, 23.042, 8.318, 23.438, 7.438, 22.36, 7.18, 21.94]
        C1 = C[(month) * 2 - 1 - 1]  # 节气1
        C2 = C[month * 2 - 1]  # 节气2
        Y = year % 100
        L = Y // 4
        if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and (C1 == 5.4055 or C1 == 3.87):
            # 注意：凡闰年3月1日前闰年数要减一，即：L=[(Y-1)/4],因为小寒、大寒、立春、雨水这两个节气都小于3月1日
            L = (Y - 1) // 4
        num1 = math.floor(Y * D + C1) - L
        num2 = math.floor(Y * D + C2) - L

        # days[num1 + fill - 1] = solarTerm[(month) * 2 - 1 - 1];
        # days[num2 + fill - 1] = solarTerm[(month) * 2 - 1];
        return (num1, num2)

    def __fill_day_info(self):

        [term_day1, term_day2] = self.__get_solar_term(self.year, self.month)

        for n in range(self.max_day):

            # 填充节日
            day_key = f'{self.month:02}{n + 1:02}'
            holiday_cn = ChineaseCalender.sonar_holidays.get(day_key)
            if holiday_cn is not None:
                self.day_info[n] = holiday_cn
                continue

            lunar = self.lunars[n]
            day_key = f'{lunar.lunar_month:02}{lunar.lunar_day:02}'
            holiday_cn = ChineaseCalender.lunar_holidays.get(day_key)
            if holiday_cn is not None:
                self.day_info[n] = holiday_cn
                continue

            # 填充节气
            if n + 1 == term_day1:
                self.day_info[n] = ChineaseCalender.solar_terms[self.month * 2 - 2]
                continue
            elif n + 1 == term_day2:
                self.day_info[n] = ChineaseCalender.solar_terms[self.month * 2 - 1]
                continue

            # 填充农历
            self.day_info[n] = lunar.cn_day()

    def __invert_by_day(self):
        col = (self.week_align + self.day - 1) % 7
        row = (self.week_align + self.day - 1) // 7
        self.invert_area(col * 42 + 2, 17 + row * 16, 42, 16)

    def update(self) -> None:
        # 计算
        self.max_day = utime.localtime(utime.mktime((self.year, self.month + 1, 0, 0, 0, 0, -1, -1)))[2]
        self.week_align = utime.localtime(utime.mktime((self.year, self.month, 1, 1, 0, 0, -1, -1)))[6]
        self.lunars = [LunarDate.fromSolarDate(self.year, self.month, day + 1) for day in range(self.max_day)]  # 农历
        self.sonars = [(self.year, self.month, day + 1) for day in range(self.max_day)]     # 公历
        self.__fill_day_info()

        # 绘图
        self.fill(0xff)

        idx = 1
        for w in range(7):
            self.font12.text_area(self, WEEK_DAYS_CN[w], w * 42 + 5, 2, 40, 14)
        self.line(2, 16, BODY_WIDTH - 2, 16)

        for n in range(7):
            for w in range(7):
                if idx == 1 and w < self.week_align:
                    continue
                if idx <= self.max_day:
                    num_w = (self.font_arial_bold.font_size // 2) if idx < 10 else self.font_arial_bold.font_size
                    en_start_x = w * 42 + (40 - num_w) // 2 - 10
                    row_y = 17 + n * 16
                    self.font_arial_bold.text_area(self, str(idx), en_start_x, row_y)
                    self.font12.text_area(self, self.day_info[idx - 1], w * 42 + (40 - self.font_arial_bold.font_size) // 2 + self.font_arial_bold.font_size - 9, row_y + 3)
                    #if idx == self.day:
                        #self.invert_area(en_start_x, row_y, num_w + (self.font_arial_bold.font_size << 1) - 1, 16)
                    idx += 1
        self.__invert_by_day()
        #self.vline(2 * 42 + 2, self.height-16, 16)
        self.font_arial_bold.text_area(self, f'{self.year:04}-{self.month:02}-{self.day:02}', 86+4, self.height-15)
        self.font12.text_area(self, self.lunars[self.day - 1].cn_date(), 164, self.height-14)
        self.change()



