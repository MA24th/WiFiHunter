# WiFiHunter
[![GPLv2 license](https://img.shields.io/badge/LICENSE-GPLv2-green)](https://github.com/ma24th/WiFiHunter/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/ma24th/WiFiHunter.svg?branch=master)](https://travis-ci.com/ma24th/WiFiHunter)
[![PyPI](https://img.shields.io/badge/PyPI-v1.0.0-blue.svg)](https://pypi.org/project/wifihunter/)
[![Telegram Group](https://img.shields.io/badge/Telegram-Group-blue.svg)](https://telegram.me/@grid9x)

The WiFi Penetration Toolkit, 
Run on existing wireless-auditing tools for you,
Stop memorizing command arguments & switches!

It's designed to use all known methods for retrieving the password of a wireless access point (AP).  These methods include:
1. WPS: The [Offline Pixie-Dust attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack)
1. WPS: The [Online Brute-Force PIN attack](https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Online_brute-force_attack)
2. WPA: The [WPA Handshake Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
3. WPA: The [PMKID Hash Capture](https://hashcat.net/forum/thread-7717.html) + offline crack.
4. WEP: Various known attacks against WEP, including *fragmentation*, *chop-chop*, *aireplay*, etc.



#### INSTALLING
```bash
git clone https://github.com/MA24th/WiFiHunter.git
cd WiFiHunter
sudo python3 install setup.py
```


#### USEAGE

```bash
sudo wifihunter --help
```
