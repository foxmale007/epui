from micropython import const
import gc
import sys
from lib.epui import *

DEBUG: int = True   # 是否调试（开启快照，开启日志打印）

SCREEN_WIDTH = const(296)
SCREEN_HEIGHT = const(128)

STATUS_BAR_HEIGHT = const(14)

BODY_ID = 'ep_body'  # 主绘画界面ID
STATUS_BAR_ID = 'ep_status_bar'  # 状态条ID
SCREEN_MASK_ID = 'ep_screen_mask'  # 半透明遮罩ID
SCREEN_FLOAT_ID = 'ep_screen_flow'  # 最上层遮罩，用于弹窗或浮层

MOD_HOME = 'home'

FONT_DIR = 'fonts'

ZLIB_MAX_WBITS = const(15)

BODY_WIDTH = const(296)
BODY_HEIGHT = const(114)

BLACK = const(0)
WHITE = const(1)

# 小图片缓存
ICON_CACHED_SIZE = 32

# 画圆边角类型，可用或组合
CORNER_TOP_LEFT = const(0x04)
CORNER_TOP_RIGHT = const(0x02)
CORNER_BOTTOM_LEFT = const(0x08)
CORNER_BOTTOM_RIGHT = const(0x01)

BORDER_UP = const(0x01)
BORDER_RIGHT = const(0x02)
BORDER_DOWN = const(0x04)
BORDER_LEFT = const(0x08)
BORDER_ALL = const(0x0F)

# 垂直对齐
VALIGN_TOP = const(0)
VALIGN_CENTER = const(1)
VALIGN_BOTTOM = const(2)

# 水平对齐
HALIGN_LEFT = const(0)
HALIGN_CENTER = const(1)
HALIGN_RIGHT = const(2)

# 键盘键定义，8键无冲组合
KEY_OK = const(1)  # confirm/enter
KEY_RETURN = const(2)  # ESC

KEY_UP = const(3)  # UP ↑
KEY_RIGHT = const(4)  # DOWN ↓
KEY_DOWN = const(5)  # Left ←
KEY_LEFT = const(6)  # Left ←
KEY_SPACE = const(7)  # SPACE

KEK_VOL_UP = const(8)  # 音量+
KEY_VOL_DOWN = const(9)  # 音量-
KEY_EARPHONE = const(10)  # 耳机插入

# 箭头方向
ARROW_UP = const(0x01)
ARROW_RIGHT = const(0x02)
ARROW_DOWN = const(0x04)
ARROW_LEFT = const(0x08)

# 按钮模式
BTN_NORMAL = const(0)  # 默认带边框，获得焦点边框加粗模式
BTN_SIMPLE = const(1)  # 默认无边框，获得焦点带边框模式
BTN_INVERT = const(2)  # 默认无边框，获得焦点反色模式

BUTTON_BAR_HEIGHT = 30

# window按钮对齐
BUTTON_ALIGN_LEFT = const(0)
BUTTON_ALIGN_CENTER = const(1)
BUTTON_ALIGN_RIGHT = const(2)

# 几个系统内置字体
FONT_MIN_EN = 'MIN14'
FONT_16 = const(16)
FONT_12 = const(12)

# 增补字体，需要时自己初始化
FONT_ARIAL_BLACK_14 = 'ARI14'

WEEK_DAYS_CN = ('一', '二', '三', '四', '五', '六', '日')
WEEK_DAYS_EN = ('MON', 'TUE', 'WED', 'THUR', 'FRI', 'SAT', 'SUN')
