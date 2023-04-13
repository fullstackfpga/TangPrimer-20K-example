files = [
    "lut_ov5640_rgb565_1024_768.v",
    "testpattern.v",
    "syn_gen.v",
    "vga_timing.v",
    "cmos_8_16bit.v",
    "top.cst",
    "lcd.sdc",
    "top.v"
]

modules = {"local" :
              [ "gowin_rpll",
                "ddr3_memory_interface",
                "fifo_hs",
                "dvi_tx",
                "video_frame_buffer",
                "i2c_master"]
          }
