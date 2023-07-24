from main import main_loop
import lib.asyncio as asyncio

asyncio.run(main_loop())
# asyncio.run(main_loop(32000)) # 正式运行时也可以启用一个看门狗来reboot，防止出错跑飞，单位ms，定时器会自动喂狗