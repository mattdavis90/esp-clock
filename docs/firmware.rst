How To Flash Latest MicroPython
-------------------------------

Install esptool from `Github <https://github.com/espressif/esptool>`_

Download the latest MicroPython for ESP8266 from `MicroPython <http://micropython.org/download#esp8266>`_

Run the following

    ./esptool.py --port /dev/ttyUSB0 erase_flash

    ./esptool.py --port /dev/ttyUSB0 write_flash --flash_size=1MB -fm dout 0 esp8266-20171101-v1.9.3.bin
