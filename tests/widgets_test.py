import uasyncio as asyncio
import utime

from tests.eptest import eptest
from lib.uiConst import *
from driver.display import screen
from widgets import *
from lib.snapshot import take_snapshot

DEFAULT_TIMEOUT = const(20)  # 持续测试的时间，超过会自动退出，方便上传更新代码，也避免墨水屏一直刷新


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=())  # 如果不使用系统默认字体，可以指定加载的字体以节约测试时间
async def test_canvas_draw(body: Layer):
    canvas = Canvas(BODY_WIDTH, BODY_HEIGHT)
    body.add_child(canvas)

    canvas.rect(10, 10, 200, 100)
    canvas.rect(50, 50, 80, 30)
    canvas.rect(150, 30, 30, 50)
    canvas.rect(50, 50, 80, 30)
    canvas.poly(21, 21, (0, 0, 10, 10, 0, 20, 0, 0), BLACK, False)
    canvas.rect(40, 20, 11, 11)
    canvas.ellipse(40 + 5, 20 + 5, 4, 4)

    canvas.ellipse(220, 20, 1, 1)
    canvas.ellipse(220, 25, 2, 2)
    canvas.ellipse(220, 35, 3, 3)
    canvas.ellipse(220, 45, 4, 4)
    canvas.ellipse(220, 58, 5, 5)
    canvas.ellipse(220, 72, 6, 6)
    canvas.ellipse(220, 90, 7, 7)
    canvas.ellipse(220, 108, 7, 7, BLACK, False, CORNER_TOP_LEFT)

    canvas.rect_rnd(250, 20, 30, 1 * 2 + 1, BLACK, True, 1).rect_rnd(250, 25, 30, 2 * 2 + 1, BLACK, True, 2) \
        .rect_rnd(250, 35, 30, 3 * 2 + 1, BLACK, True, 3).rect_rnd(250, 45, 30, 4 * 2 + 1, BLACK, True, 4) \
        .rect_rnd(250, 58, 30, 5 * 2 + 1, BLACK, True, 5).rect_rnd(250, 72, 30, 6 * 2 + 1, BLACK, True, 6) \
        .rect_rnd(250, 90, 30, 7 * 2 + 1, BLACK, True, 7)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=())
async def test_move(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'))
    body.add_child(Image('/tests/sprite01.bmp.gz', oid=8848), 130, 20)

    direction_x = 1
    direction_y = 1
    for n in range(20):
        mickey = get_by_id(8848)

        if mickey.y + mickey.height == body.height - 1 or mickey.y == 0:
            direction_y = -direction_y
        if mickey.x + mickey.width == body.width - 1 or mickey.x == 0:
            direction_x = -direction_x
        mickey.move(direction_x, direction_y)

        await asyncio.sleep_ms(300)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=())
async def test_canvas2(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'))
    canvas1 = Canvas(100, 100)
    body.add_child(canvas1, 10, 10)
    canvas1.ellipse(0, 0, 30, 30, BLACK, True)
    canvas1.ellipse(100, 100, 30, 30, BLACK, True)

    canvas2 = Canvas(80, 80, transparent_color=BLACK)
    body.add_child(canvas2, 150, 20)
    canvas2.ellipse(0, 80, 40, 40, BLACK, True)
    canvas2.ellipse(80, 0, 40, 40, BLACK, True)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=())
async def test_fixedlayout(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'), 0, 14)
    body.add_child(FixedLayout(50, 50, border_width=1), 10, 10)
    body.add_child(FixedLayout(40, 30, background_color=BLACK), 20, 80)

    fix = FixedLayout(40, 40, border_width=1)
    body.add_child(fix, 120, 60)

    fix.add_child(FixedLayout(20, 20, border_width=1), 5, 5)

    body.add_child(FixedLayout(40, 25, background_color=BLACK, border_radius=7), 200, 40)
    body.add_child(FixedLayout(40, 25, background_color=WHITE, border_width=1, border_radius=7), 200, 70)


class SampleBox(BaseWidget):

    def draw(self) -> bool:
        draw_layer: Layer = self.__draw_layer
        draw_layer.rect(self.x, self.y, self.width, self.height)
        draw_layer.line(self.x, self.y, self.x + self.width - 1, self.y + self.height - 1)
        draw_layer.line(self.x, self.y + self.height - 1, self.x + self.width - 1, self.y)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=())
async def test_boxlayout(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'), 0, 14)
    boxlayout = BoxLayout(100, 80, border_width=1, valign=VALIGN_CENTER, halign=HALIGN_CENTER)
    body.add_child(boxlayout)

    boxlayout.add_child(SampleBox(50, 40, transparent_color=WHITE))
    boxlayout.add_child(SampleBox(30, 50, transparent_color=WHITE))

    # test move
    await asyncio.sleep_ms(2000)
    boxlayout.move(10, 10)

    await asyncio.sleep_ms(2000)
    boxlayout.move_to(100, 30)

    # test remove
    await asyncio.sleep_ms(2000)
    body.remove_child(boxlayout)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12, 16))
async def test_text(body: Layer):
    screen.register_font('DIN24', f'/{FONT_DIR}/DINCondensed24-num-r.bmf.gz')
    screen.register_font('IMP24', f'/{FONT_DIR}/impact24-num-r.bmf.gz')
    screen.register_font('MIN14', f'/{FONT_DIR}/MinusioNew14-en-r.bmf.gz')
    screen.register_font('OUT26', f'/{FONT_DIR}/outline-pixel-7-1_26-en-r.bmf.gz')
    screen.register_font('CAL32', f'/{FONT_DIR}/calculatrix-7-2_32-en-r.bmf.gz')
    screen.register_font('LED40', f'/{FONT_DIR}/LediZ-St-1_40-chr-r.bmf.gz')
    screen.register_font('ARI14', f'/{FONT_DIR}/arialbd14-num-r.bmf.gz')
    screen.register_font('COU28', f'/{FONT_DIR}/Courier28-en-r.bmf.gz')
    screen.register_font('LXK36', f'/{FONT_DIR}/LXKSimple36-num-r.bmf.gz')

    canvas = Canvas(BODY_WIDTH, BODY_HEIGHT)
    body.add_child(canvas)

    from lib.bmpgz import Bmp
    bmp = Bmp('/m_home/desk01.bmp.gz')
    canvas.blit(bmp.wb_frame, 0, 0)

    canvas.text("正好B", 15, 90)

    canvas.text("这个测试折行折行折行都发生范德萨范德萨法撒旦飞洒胜多负少的范德萨范德萨", 100, 18)

    # canvas.rect(100,50,80,40,BLACK,True)
    canvas.text("10:46", 100, 50, font='DIN24')

    canvas.text("-28:77", 60, 80, font='IMP24')

    canvas.rect(0, 0, 28, 13, BLACK, True)
    canvas.text("内存", 2, 0, WHITE, font=12)
    canvas.text("15% DISK:30%", 30, 0, font='MIN14')
    canvas.line(0, 0, 100, 0)
    canvas.line(0, 12, 100, 12)

    canvas.text("HELLO X", 10, 32, font='OUT26')
    canvas.text("85:76", 10, 50, font='CAL32')
    canvas.rect(6, 14, 63, 23, BLACK, True)
    canvas.text("DIG", 10, 6, WHITE, font='LED40')

    # canvas.text("14:23 -12.7", 120, 0, font='ARI14')
    canvas.text("14:23 -12.7", 120, 0, font='LXK36')

    canvas.text("EPUI Ver0.1.0", 140, 80, font='COU28')

    canvas.invert_area(230, 60, 40, 25)

    take_snapshot()


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,))
async def test_label(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz', oid='bg'))
    body.add_child(Label('这是个文字', oid='atext'), 0, 0)

    text_box1 = BoxLayout(border_width=2)
    text_box1.add_child(Label('哈哈哈'))
    body.add_child(text_box1, 0, 17)

    text_box2 = BoxLayout(120, halign=HALIGN_RIGHT, border_width=1, padding=(4, 2, 1))
    text_box2.add_child(Label('文字右对齐'))
    body.add_child(text_box2, 55, 17)

    text_box3 = BoxLayout(border_width=2, padding=2)
    text_box3.add_child(Label('这个是折行啊？', 48, auto_wrap=True))
    body.add_child(text_box3, 5, 45)

    body.add_child(TextBox('文本块', 70, 40, color=WHITE, border_width=1, halign=HALIGN_CENTER, valign=VALIGN_CENTER,
                           oid='center-text'), 70, 60)

    await asyncio.sleep_ms(2000)

    full_win = BaseWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    text_box_multi = BoxLayout(screen.width, screen.height, border_width=1, padding=(3, 7))
    text_box_multi.add_child(Label("""人类的逃亡分为五步：第一步，用地球发动机使地球停止转动，使发动机喷口固定在地球运行的反方向；第二步，全功率开动地球发动机，使地球加速到逃逸速度，飞出太阳系；第三步，在外太空继续加速，飞向比邻星；第四步，在中途使地球重新自转，调转发动机方向，开始减速；第五步，地球泊入比邻星轨道，成为这颗恒星的卫星。人们把这五步分别称为刹车时代、逃逸时代、流浪时代I（加速）、流浪时代II（减速）、新太阳时代。
整个移民过程将延续两千五百年时间，一百代人。""", screen.width - 2 - 7 * 2, screen.height - 2 - 3 * 2, auto_wrap=True,
                                   row_spacing=1))
    full_win.add_child(text_box_multi).show()
    await asyncio.sleep_ms(5000)
    full_win.close()

    await screen.full_update()  # 强刷一下


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,16))
async def test_layout(body: Layer):
    hbox1 = HBoxLayout()
    hbox1.add_child(Label('√', font_key=16))
    hbox1.add_child(Label('哈哈连续吗？', 48, font_key=16))  # 超过的要被截取
    hbox1.add_child(Label('nmmm...', font_key=16))
    body.add_child(hbox1)

    hbox2 = HBoxLayout(130, border_width=1, padding=2, valign=VALIGN_CENTER)
    hbox2.add_child(Label('早班'), flex=1)
    hbox2.add_child(Label('中班\n那啥圊', font_key=16), flex=1)
    hbox2.add_child(Label('晚班'))
    body.add_child(hbox2, 140, 0)

    vbox1 = VBoxLayout(None, 80, border_width=1, padding=2, halign=HALIGN_CENTER)
    vbox1.add_child(Label('早班'), flex=1)
    vbox1.add_child(Label('中班休息\n那啥', font_key=16), flex=2)
    label1 = Label('晚班哦')
    vbox1.add_child(label1)
    body.add_child(vbox1, 0, 20)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,16))
async def test_timer_with_widget(body: Layer):
    from driver.timer import start_timer

    label1 = Label('')
    body.add_child(label1, 10)

    count: int = 0

    def time_func1():
        nonlocal count
        label1.text = f'[{count}: Memory free: {gc.mem_free() / 1024} k\nallocated: {gc.mem_alloc() / 1024} k ]'
        count += 1
        if count % 10 == 0:
            gc.collect()

    start_timer('mem', time_func1)

    label2 = Label('', font_key=16)
    body.add_child(label2, 0, 50)

    def time_func2():
        text = '{:04d}年{:02d}月{:02d}日 {:02d}:{:02d}:{:02d} 周{:02d}'.format(*utime.localtime())
        if text != label2.text:
            label2.text = text

    start_timer('prn', time_func2)

@eptest(timeout=60, with_fonts=(12))
async def test_keyboard(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'), 0, 14)

    label = Label('没有键按下', width=144, auto_wrap=True)
    body.add_child(label, 10, 20)

    body.add_child(Image('/tests/sprite01.bmp.gz', oid=8848), 130, 20)

    def print_key(key_dict: dict[int, bool]):
        texts: list(str) = []

        continuous = key_dict.get(KEY_UP)
        if continuous is not None:
            texts.append(f'方向上键被{"持续按下" if continuous else "按下"}')
            get_by_id(8848).move(0, -2 if continuous else -1)

        continuous = key_dict.get(KEY_LEFT)
        if continuous is not None:
            texts.append(f'方向左键被{"持续按下" if continuous else "按下"}')
            get_by_id(8848).move(-2 if continuous else -1, 0)

        continuous = key_dict.get(KEY_RIGHT)
        if continuous is not None:
            texts.append(f'方向右键被{"持续按下" if continuous else "按下"}')
            get_by_id(8848).move(2 if continuous else 1, 0)

        continuous = key_dict.get(KEY_DOWN)
        if continuous is not None:
            texts.append(f'方向下键被{"持续按下" if continuous else "按下"}')
            get_by_id(8848).move(0, 2 if continuous else 1)

        continuous = key_dict.get(KEY_SPACE)
        if continuous is not None:
            texts.append(f'中间键被{"持续按下" if continuous else "按下"}')

        continuous = key_dict.get(KEY_OK)
        if continuous is not None:
            texts.append(f'SET键被{"持续按下" if continuous else "按下"}')

        continuous = key_dict.get(KEY_RETURN)
        if continuous is not None:
            texts.append(f'RST键被{"持续按下" if continuous else "按下"}')

        lines = '\n'.join(texts)
        label.text = lines

        print(lines)

    body.add_key_handler(print_key)
    body.focus()  # 激活后可收消息


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12, FONT_MIN_EN))
async def test_progress(body: Layer):

    progress1 = Progress(100, 30)
    body.add_child(progress1, 5, 5)
    progress2 = Progress(100, 30, outline=True)
    body.add_child(progress2, 5, 40)

    progress3 = Progress(100, 30, rounded=True)
    body.add_child(progress3, 110, 5)
    progress4 = Progress(100, 30, rounded=True, outline=True)
    body.add_child(progress4, 110, 40)

    index = 0

    def next_weekday():
        weeks = ('日', '一', '二', '三', '四', '五', '六')
        nonlocal index
        index += 1
        return f'星期{weeks[index % 7]}'

    progress5 = Progress(100, 30, rounded=True, outline=True, label_format=next_weekday())
    body.add_child(progress5, 5, 75)

    progress6 = Progress(100, 14, rounded=True, outline=True, font_key='MIN14')
    body.add_child(progress6, 110, 75)

    # screen.line(110 + 98, 95+15, 110 + 98 + 20, 95+15)

    await asyncio.sleep_ms(2000)
    for n in range(1, 11):
        progress1.set_value(n * 10)
        progress2.set_value(n * 10)
        progress3.set_value(n * 10)
        progress4.set_value(n * 10)
        progress5.set_value(n * 10)
        progress5.label_format = next_weekday()
        progress6.set_value(n * 10)
        await asyncio.sleep_ms(2000)


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,))
async def test_layer(body: Layer):
    layer = Layer(100, 100)
    box = HBoxLayout(100, 100, border_width=1, space_between=5).add_child(Label("哈哈，整体移动")).add_child(
        BoxLayout(10, 10, background_color=BLACK))
    layer.add_child(box)
    body.add_child(layer, 20, 20)
    await asyncio.sleep_ms(2000)
    layer.move(-5, -5)
    await asyncio.sleep_ms(2000)
    layer.move_to(50, 5)

@eptest(timeout=60, with_fonts=(12,))
async def test_button(body: Layer):
    def fullupd_handler(_):
        print('手动全刷')
        await screen.full_update()

    def show_label_text(btn: TextButton):
        print(btn.text, '被按下')

    body.add_child(FixedLayout(SCREEN_WIDTH // 2, SCREEN_HEIGHT, background_color=WHITE), 0, 0)
    body.add_child(FixedLayout(SCREEN_WIDTH // 2, SCREEN_HEIGHT, background_color=BLACK), SCREEN_WIDTH // 2, 0)
    body.add_child(
        HBoxLayout(space_between=5)
            .add_child(ImageButton('/modules_icon/sysconf16.bmp', 24, 24, tabindex=1, oid=8848))
            .add_child(TextButton('执行全刷', tabindex=2, click_handler=fullupd_handler))
            .add_child(TextButton('确定', image='/icons/agree.bmp', tabindex=3, click_handler=show_label_text))
            .add_child(
            ImageButton('/modules_icon/ebook16.bmp', 24, 24, tabindex=4, color=WHITE, click_handler=show_label_text))
            .add_child(
            TextButton('取消', image='/icons/cancel.bmp', tabindex=5, color=WHITE, click_handler=show_label_text)),
        5, 5
    )
    body.add_child(
        HBoxLayout(space_between=20)
            .add_child(TextButton('返回', image='/icons/return.bmp', tabindex=6, click_handler=show_label_text))
            .add_child(TextButton('退出', image='/icons/exit.bmp', tabindex=7, click_handler=show_label_text))
            .add_child(
            TextButton('刷新', image='/icons/refresh.bmp', tabindex=8, color=WHITE, click_handler=show_label_text)),
        5, 35
    )

    body.add_child(
        HBoxLayout(space_between=20)
            .add_child(TextButton('OK', mode=BTN_SIMPLE, tabindex=9, click_handler=show_label_text))
            .add_child(TextButton('ON', mode=BTN_SIMPLE, tabindex=10, click_handler=show_label_text))
            .add_child(
            ImageButton('/modules_icon/quickcalc16.bmp', mode=BTN_SIMPLE, tabindex=11, click_handler=show_label_text))
            .add_child(TextButton('好的', mode=BTN_SIMPLE, tabindex=12, color=WHITE, click_handler=show_label_text))
            .add_child(
            ImageButton('/icons/exit.bmp', mode=BTN_SIMPLE, tabindex=13, color=WHITE, click_handler=show_label_text)),
        5, 60
    )

    body.add_child(
        HBoxLayout(space_between=20)
            .add_child(TextButton('OK', mode=BTN_INVERT, tabindex=14, click_handler=show_label_text))
            .add_child(TextButton('ON', mode=BTN_INVERT, tabindex=15, click_handler=show_label_text))
            .add_child(
            ImageButton('/modules_icon/quickcalc16.bmp', mode=BTN_INVERT, tabindex=16, click_handler=show_label_text))
            .add_child(TextButton('好的', mode=BTN_INVERT, tabindex=17, color=WHITE, click_handler=show_label_text))
            .add_child(
            ImageButton('/icons/exit.bmp', mode=BTN_INVERT, tabindex=18, color=WHITE, click_handler=show_label_text)),
        5, 85
    )

    get_by_id(8848).focus()


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,))
async def test_home_widget(body: Layer):
    # from widgets.slider import SimpleArrow, HSlider
    # from m_test.samples import SampleItem
    from m_home.home_widgets import HomeItem, HomeSlider

    async def handler(widget: BaseWidget):
        print('clicked', widget)
        await asyncio.sleep_ms(1000)
        print('checked', widget)

    body.add_child(HomeSlider(3, space_between=10, background_color=WHITE, valign=VALIGN_BOTTOM, padding=5, oid=3322,
                                click_handler=handler)
                     .add_child(
        HomeItem('', '时钟', '/modules_icon/clock16.bmp', 'modules_icon/clock24.bmp', oid=200, click_handler=handler))
                     .add_child(
        HomeItem('', '电子书', '/modules_icon/ebook16.bmp', 'modules_icon/ebook24.bmp', oid=202, click_handler=handler))
                     .add_child(
        HomeItem('', '词典', '/modules_icon/edict16.bmp', 'modules_icon/edict24.bmp', oid=203, click_handler=handler))
                     .add_child(
        HomeItem('', '计算器', '/modules_icon/quickcalc16.bmp', 'modules_icon/quickcalc24.bmp', oid=204,
                 click_handler=handler))
                     .add_child(
        HomeItem('', '日历', '/modules_icon/quickcalendar16.bmp', 'modules_icon/quickcalendar24.bmp', oid=204,
                 click_handler=handler)),
                     50, 30
                     )
    get_by_id(3322).focus()


@eptest(timeout=60, with_fonts=(12, 16))
async def test_window(body: Layer):

    def ok_handler(btn: TextButton):
        print('别瞎吵吵！', btn, '被点击了')

    def del_handler(_):
        print('已全部删除')

    body.add_child(
        HBoxLayout(space_between=10)
            .add_child(TextButton('Alert(大)', click_handler=lambda _: Message.alert('哈哈哈'), oid=666, tabindex=1))
            .add_child(TextButton('Alert(小)', click_handler=lambda _: Message.alert('哈哈哈\n很多字', font_key=12),
                                  tabindex=2)),
        20, 20
    ).add_child(
        HBoxLayout(space_between=10)
            .add_child(TextButton('Confirm', click_handler=lambda _: Message.confirm('确定点击？', ok_handler=ok_handler),
                                  tabindex=3))
            .add_child(TextButton('自定按钮文本', click_handler=lambda _: Message.confirm('确定删除？',
                cancel_text='手滑了', ok_text='寄了', ok_handler=del_handler), tabindex=4))
            .add_child(TextButton('超多文本', tabindex=5, click_handler=lambda _: Message.alert(
            '吃葡萄不吐葡萄皮不吃葡萄倒吐葡萄皮是不是很好玩呀哈哈哈撑死我了', close_text='知道了'))),
        20, 50
    )
    get_by_id(666).focus()


@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,))
async def test_snapshot(body: Layer):
    body.add_child(Image('/m_home/desk01.bmp.gz'), 0, 14)
    snap_text = Label('2秒后拍快照')
    body.add_child(BoxLayout(background_color=WHITE, padding=(2, 5)).add_child(snap_text))  # 加个容器因为文本默认背景是透明的
    await asyncio.sleep_ms(2000)
    snap_text.text = '快照保存至:' + take_snapshot()

if __name__ == '__main__':
    test_progress()
