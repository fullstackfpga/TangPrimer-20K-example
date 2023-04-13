files = [
    "lut_ov5640_rgb565_480_272.v",
    "testpattern.v",
    "syn_gen.v",
    "cmos_8_16bit.v",
    "top.cst",
    "lcd.sdc",
    "top.v"
]

modules = {"local" :
              [ "gowin_rpll",
                "ddr3_memory_interface",
                "fifo_hs",
                "video_frame_buffer",
                "i2c_master"]
          }
