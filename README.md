# RFID-avec-RaspberryPi
J'ai fait Un Module complet ameliore de Simon de la lecture et d'ecriture 
en python du module RFID MFRC522 a en utilisant raspberry pi

MFRC522-python
==============
A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi.
This is a Python port of the example code for the NFC module MF522-AN.

**Important notice:** This library has not being actively updated in almost four years.
It might not work as intended on more recent Raspberry Pi devices. You might want to 
take a look to the open pull-requests and forks to see other implementations and bug-fixes.

## Requirements
This code requires you to have SPI-Py installed from the following repository:
https://github.com/lthiery/SPI-Py

```lsmod | grep spi```
```sudo pip3 install spidev```

## Examples
This repository includes a couple of examples showing how to read, write, and dump data from a chip. They are thoroughly commented, and should be easy to understand.

## Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

## Usage
Import the class by importing SimpleMFRC522 in the top of your script. For more info see the examples.

## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.

## Service
For the creation of the services some stuffs are done,
- copy the easy-water servce file to /lib/systemd/system
- commands
we reload
==> sudo systemctl daemon-reload

we enable service
==> sudo systemctl enable easy-water.service
==> sudo systemctl start easy-water.service

we stop , start , restart
==> sudo systemctl stop easy-water.service
==> sudo systemctl start easy-water.service
==> sudo systemctl retart easy-water.service

- to watch the journal of the service and standard output
journalctl -u easy-water.service





