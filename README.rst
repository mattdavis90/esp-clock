esp-clock
=========
Python Programmable WiFi Enabled Clock


To flash
--------
    $ ./esptool.py --port /dev/ttyUSB0 erase_flash
    $ ./esptool.py --port /dev/ttyUSB0 write_flash --flash_size=1MB -fm dout 0 esp8266-20171101-v1.9.3.bin
