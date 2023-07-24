"""
    此模块定义了所有PIN脚接线参数
    根据实际的模块类型和接线可以更改
"""
from micropython import const
from lib.uiConst import KEY_SPACE, KEY_RETURN

# ======== ESP32-S2-MINI(LOLIN) ========
# -------- 屏幕 --------
EP_SCK_PIN = 18
EP_MOSI_PIN = 16
EP_MISO_PIN = 15    # 找个没有用到的PIN
EP_CS_PIN = 33
EP_DC_PIN = 35
EP_RST_PIN = 37
EP_BUSY_PIN = 39
EP_BAUD = 1152_0000     # 根据屏幕调整波特率，过高可能导致无响应
# -------- 按键 --------
KEY_UP_PIN = 10
KEY_DOWN_PIN = 11
KEY_LEFT_PIN = 13
KEY_RIGHT_PIN = 12
KEY_SPACE_PIN = 14
KEY_OK_PIN = 6
KEY_RETURN_PIN = 8

KEK_VOL_UP_PIN = 40
KEY_VOL_DOWN_PIN = 38
KEY_EARPHONE_PIN = 17   # 耳机插入
# -------- 电量(ADC0832) --------
BATT_CS_PIN = 36
BATT_CLK_PIN = 34
BATT_DI_PIN = 21
BATT_DO_PIN = -1  # 如果IN/OUT公用模式可以设置为-1
# -------- SD卡 --------
SD_SCK_PIN = 5
SD_MOSI_PIN = 7
SD_MISO_PIN = 3
SD_CS_PIN = 9
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
