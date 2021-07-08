# WiFiHunter
[![GPLv2 license](https://img.shields.io/badge/LICENSE-GPLv2-green)](https://github.com/ma24th/WiFiHunter/blob/master/LICENSE)
[![Python package](https://github.com/MA24th/WiFiHunter/actions/workflows/python-package.yml/badge.svg)](https://github.com/MA24th/WiFiHunter/actions/workflows/python-package.yml)
[![Upload Python Package](https://github.com/MA24th/WiFiHunter/actions/workflows/python-publish.yml/badge.svg)](https://github.com/MA24th/WiFiHunter/actions/workflows/python-publish.yml)
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



## How to Install
from source code 
```bash
git clone https://github.com/MA24th/WiFiHunter.git
cd WiFiHunter
sudo python3 setup.py install
```
Or from PyPI
```bash
pip3 install wifihunter
```

## How to Use

```bash
sudo wifihunter --help
```


## How to Contribute
- You must follow [Contributing](https://github.com/MA24th/MA24th/blob/main/OpenSource/Software/CONTRIBUTING.md) Guidelines.
- We are committed to providing a friendly community, for more experience read [Code Of Conduct](https://github.com/MA24th/MA24th/blob/main/OpenSource/Software/CODE_OF_CONDUCT.md).


## How to Communicate
You're welcome to drop in and ask questions, 
discuss bugs and such, Check [Communication](https://github.com/MA24th/MA24th/blob/main/OpenSource/Software/COMMUNICATION.md) Methods.


## Frequently Asked Questions
Click on [FAQ](https://github.com/MA24th/MA24th/blob/main/OpenSource/Software/FAQ.md) before asking questions.


## Attribution
These Documents are adapted for [MA24th Open Source Software](https://github.com/MA24th/MA24th/blob/main/OpenSource/Software/),
For more information [contact me](mailto:ma24th@yahoo.com) with any additional questions or comments.


## License
Copyright (c) MA24th Software. All rights reserved.
Licensed under the [GPLv2](https://opensource.org/licenses/gpl-2.0) License.
