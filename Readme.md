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
    
    jlc C22975 # 2k R4
    jlc C19666 # 4.7uF
    jlc C25804 # 10k
    jlc C155590 # Shottkydiode D3
    jlc C15127 # p channel mosfet
    jlc C15849 # 1uF
    jlc C23630 # 2.2uF
    jlc C19702 # 10uF
    jlc C14663 # 100nF
    jlc C255886 # 26Mhz oscilator
    jlc C1634 # 10pF
    jlc C22790 # 12k
    jlc C8218 # 200 Ohm
    jlc C519111 # 5.6pF
        
Credits
-------

- I used the wonderful [JLC2KiCadLib](https://pypi.org/project/JLC2KiCadLib/) to get the footprints from the JLC components.
