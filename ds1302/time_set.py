import ds1302
clk_pin=18
data_pin=17
ce_pin=16
ds = ds1302.DS1302(clk_pin,data_pin,ce_pin)
print(ds.read_datetime())
#ds.write_datetime(2021,3,10,20,32,30)