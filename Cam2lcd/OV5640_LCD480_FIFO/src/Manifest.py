files = [
    "lut_ov5640_rgb565_480_272.v",
    "video_timing_data.v",
    "color_bar.v",
    "cmos_8_16bit.v",
    "top.cst",
    "lcd.sdc",
    "top.v"
]

modules = {"local" :
              [ "gowin_rpll",
                "fifo_hs",
                "i2c_master"]
          }
