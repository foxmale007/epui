"""
    此模块定义了所有PIN脚接线参数
    根据实际的模块类型和接线可以更改
"""
from micropython import const
from lib.uiConst import KEY_SPACE, KEY_RETURN

# ======== ESP32-S2-MINI(LOLIN) ========
# -------- 屏幕 --------

EP_SCK_PIN = 10
EP_MOSI_PIN = 11
EP_MISO_PIN = 12    # 找个没有用到的PIN
EP_CS_PIN = 9
EP_DC_PIN = 13
EP_RST_PIN = 21
EP_BUSY_PIN = 33
EP_BAUD = 1152_0000     # 根据屏幕调整波特率，过高可能导致无响应
# -------- 按键 --------
KEY_PAD_3_BUTTONS = const(0b0101001)    # 3键定义：左、右、OK（拨轮）
KEY_PAD_4_BUTTONS = const(0b0101011)    # 4键定义：左、右、OK、RETURN（常用4按钮）
KEY_PAD_5_BUTTONS = const(0b0111101)    # 5键定义：5向按钮，或4个方向键+OK
KEY_PAD_6_BUTTONS = const(0b0111111)    # 6键定义：4个方向键+OK+RETURN
KEY_PAD_7_BUTTONS = const(0b1111111)    # 7键定义：调试用5向面板+OK+RETURN，SPACE是中心键
KEY_PAD_MODE = KEY_PAD_7_BUTTONS

KEY_SPACE_PIN = 1
KEY_UP_PIN = 6
KEY_DOWN_PIN = 7
KEY_LEFT_PIN = 4
KEY_RIGHT_PIN = 5
KEY_OK_PIN = 2
KEY_RETURN_PIN = 3
# -------- 电量(ADC0832) --------
BATT_CS_PIN = 14
BATT_CLK_PIN = 18
BATT_DI_PIN = 16
BATT_DO_PIN = 17  # 如果IN/OUT公用模式可以设置为-1
# -------- SD卡 --------
SD_SCK_PIN = 37
SD_MOSI_PIN = 40
SD_MISO_PIN = 38
SD_CS_PIN = 39
SD_BAUD = 5000_0000

# 快照键KEY_RETURN，长按3秒激活，截取快照到/snapshot
SNAP_TRIGGER_FREQ_MS = 3000     # 长按激活的时长

# 电量采集量和电池容量映射关系，根据实际电池特性调整
# 参数依次：电量0,25%,50%,75%,100%,充电中
BATT_LEVEL_CONF = (176, 186, 195, 204, 209)

# 255*3.5*0.975/4.97 = 175.09
# 255*3.7*0.975/4.97 = 185.09
# 255*3.9*0.975/4.97 = 195.10
# 255*4.1*0.975/4.97 = 205.10
# 255*4.18*0.975/4.97 = 209.1 # 充电
