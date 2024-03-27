ESP8266 PCB
===========

JLCPCB Footprints
-----------------

I created the following alias to download the footprints:

    # ~/.zshrc
    alias jlc='JLC2KiCadLib -dir lib -symbol_lib jlc_symbols -symbol_lib_dir "." -footprint_lib jlc_footprints.pretty'

So I can for example run `jlc C123455` to download both the symbol and the footprint for a given component.

    jlc C77967 --no_symbol # ESP8266EX chip
    jlc C505111 --no_symbol # Micro USB adapter
    jlc C7464026 --no_symbol # USB2UART chip
    jlc C160390 # I2C connector
    jlc C82227 # Temperature and humidity sensor
    jlc C2922787 # SK6812 Neopixel
    jlc C51118 # 3V3 AP2112K voltage regulator
    jlc C62892 # NPN transistor array
    jlc C318884 # Tactile switches
    jlc C424093 # Battery management IC
    jlc C97521 # flash chip (alternative: C5127618)
    jlc C295747 # JST battery connector
    jlc C963206 # slide switch
    # FET for switching between VUSB and VBAT
    # Zener Diode D3?
    
Credits
-------

- I used the wonderful [JLC2KiCadLib](https://pypi.org/project/JLC2KiCadLib/) to get the footprints from the JLC components.
