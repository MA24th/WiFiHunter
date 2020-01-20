==========
WiFiHunter
==========

A WiFi Penetration Toolkit,
Run on existing wireless-auditing tools for you
Stop memorizing command arguments & switches!,
It's designed to use all known methods for retrieving
The password of a wireless access point (AP).

These methods include:

1. WPS The `Offline Pixie-Dust attack <https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Offline_brute-force_attack>`_
2. WPS The `Online Brute-Force PIN attack <https://en.wikipedia.org/wiki/Wi-Fi_Protected_Setup#Online_brute-force_attack>`_
3. WPA The `WPA Handshake Capture <https://hashcat.net/forum/thread-7717.html>`_ + offline crack.
4. WPA The `PMKID Hash Capture <https://hashcat.net/forum/thread-7717.html>`_ + offline crack.
5. WEP Various known attacks against WEP,
   including *fragmentation*, *chop-chop*, *aireplay*, etc.


----------
INSTALLING
----------

::

    $ git clone https://github.com/MA24th/WiFiHunter.git
    $ cd WiFiHunter
    $ sudo python3 install setup.py


------
USEAGE
------
``$ sudo wifihunter --help``
