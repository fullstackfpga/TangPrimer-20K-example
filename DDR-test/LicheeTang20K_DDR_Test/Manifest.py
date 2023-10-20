target = "gowin"
action = "synthesis"

syn_family = "GW2"
syn_family_surfix = "A"
syn_device_prefix = "LV"
syn_device = "18"
syn_device_version = "C"
syn_grade = "C8/I7"
syn_package = "PG256"
syn_top = "ddr3_syn_top"
syn_properties = [{'use_sspi_as_gpio' : '1'}]
syn_project = "ddr_test"
syn_tool = "gowin"

modules = {"local" :
              [ "src" ]
          }
