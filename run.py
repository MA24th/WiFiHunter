#!/usr/bin/env python3

# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com

try:
    from wifihunter import __main__
except (ImportError) as e:
    raise Exception('You may need to reinstall wifihunter)', e)

__main__.start()
