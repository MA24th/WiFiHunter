# WiFiHunter
[![GPLv2 license](https://img.shields.io/badge/LICENSE-GPLv2-green)](https://github.com/ma24th/WiFiHunter/blob/master/LICENSE)
![Python package](https://github.com/MA24th/wifihunter/workflows/Python%20package/badge.svg)
![Upload Python Package](https://github.com/MA24th/wifihunter/workflows/Upload%20Python%20Package/badge.svg)
[![PyPI](https://img.shields.io/badge/PyPI-v1.0.0-blue.svg)](https://pypi.org/project/wifihunter/)
[![Discord Server](https://img.shields.io/badge/Discord-Server-blue.svg)](https://discord.gg/g65AqbPK6g)

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
