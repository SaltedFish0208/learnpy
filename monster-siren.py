from cefpython3 import cefpython
import sys

#我最讨厌两件东西
#一件是不写注释的源码
#另一件是写注释

sys.excepthook = cefpython.ExceptHook

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

cefpython.Initialize(settings=settingsforinitialize)
cefpython.CreateBrowserSync(url="https://monster-siren.hypergryph.com", window_title="Monster Siren Records", settings=settingsforcreate)

cefpython.MessageLoop()

cefpython.Shutdown()