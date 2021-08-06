from cefpython3 import cefpython as cef
import sys

# 替换python预定义异常处理逻辑，为保证异常发生时能够结束所有进程
sys.excepthook = cef.ExceptHook

#参数
settingsforinitialize = {
    "auto_zooming":"system_api",
    "cache_path":"./cache",
    "windowless_rendering_enabled":True
}
settingsforcreate = {
    "application_cache_disabled":True,
    "text_area_resize_disabled":True,
    "default_font_size":16,
    "default_fixed_font_size":16,
    "minimum_font_size":10,
    "minimum_logical_font_size":10
}
# 创建浏览器
cef.Initialize(settings=settingsforinitialize)
cef.CreateBrowserSync(url="https://monster-siren.hypergryph.com", window_title="Monster Siren Records", settings=settingsforcreate)

# 消息循环：监听信号和处理事件
cef.MessageLoop()

# 结束进程
cef.Shutdown()
