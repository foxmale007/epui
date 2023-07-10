from tests.eptest import eptest
from micropython import const
from lib.uiConst import *

DEFAULT_TIMEOUT = const(20)     # 持续测试的时间，超过会自动退出，方便上传更新代码，也避免墨水屏一直刷新

@eptest(timeout=DEFAULT_TIMEOUT, with_fonts=(12,)) # 如果不使用系统默认字体，可以指定加载的字体以节约测试时间
async def test_sys_conf():
    from modules.sysconf import Sysconf
    return Sysconf()


@eptest(timeout=DEFAULT_TIMEOUT)
async def test_sys_more():
    from m_sysconf.more_view import SysconfMoreView
    return SysconfMoreView()


@eptest(timeout=DEFAULT_TIMEOUT)
async def test_wifi_conf():
    from modules.wificonf import Wificonf
    return Wificonf()


@eptest(timeout=DEFAULT_TIMEOUT)
async def test_theme_view():
    from m_sysconf.theme_view import SysconfThemeView
    return SysconfThemeView()


@eptest(timeout=DEFAULT_TIMEOUT)
async def test_airkiss():
    from m_wificonf.airkiss_view import WifiAirkissView
    return WifiAirkissView()


@eptest(timeout=DEFAULT_TIMEOUT)
async def test_about(_):
    from m_sysconf.about_view import SysconfAboutView
    return SysconfAboutView()


if __name__ == '__main__':
    test_about()
