from modules.mbase import EPApp
from widgets import *
from lib.ufontMem import BMFont
from driver.display import screen
from lib.uiConst import *
from m_quickcalendar.chinease_calender import ChineaseCalender
import utime


class Quickcalendar(EPApp):

    def __init__(self):
        super().__init__()
        self.font_arial_bold: BMFont = None

    def active(self) -> BaseWidget | tuple(BaseWidget) | None:
        """
        模块激活，相当于模块自动启动的代码，返回状态栏组件
        :return: 挂载在状态栏的组件
        """
        self.font_arial_bold = screen.register_font('ARI14', f'/{FONT_DIR}/arialbd14-num-r.bmf.gz')

        return None

    def create_ui(self) -> list[tuple(BaseWidget, int, int)]:
        """
        模块初始化，构建自己的对象，挂载在Layer上
        组件大小为去掉状态栏的尺寸：296*(128-14) = 296 x 114
        该部分代码在进入模块时执行，绘制模块界面，注册键盘事件等
        :param body: 主显示区块Layer
        """
        calender = ChineaseCalender(utime.localtime(), tabindex=1)
        return_button = TextButton('退出', 34, 16, mode=BTN_INVERT, tabindex=3,
                                   click_handler=self.go_back)

        def show_help(_):
            help_dialog = Dialog(200, 110, close_text='知道了')
            help_dialog.add_child(Label('使用帮助', font_key=16), 10, 7)
            help_dialog.add_child(Label("""←→键短按切换日期/切换功能按钮
    长按切换月份
↑↓键短按切换周/切换月份
    长按切换年份
年份范围(2001~2099)""", row_spacing=2), 10, 28)
            help_dialog.show()

        help_button = TextButton('帮助', 34, 16, mode=BTN_INVERT, tabindex=2,
                                 click_handler=show_help)

        self.set_default_focus(calender)
        return [
            (calender, 0, 0),
            (return_button, 164 + 46 + 50, BODY_HEIGHT - 16),
            (help_button, 164 + 48 + 9 + 3, BODY_HEIGHT - 16)
        ]

    def name_cn(self) -> str:  # 模块的中文名
        return '万年历'
