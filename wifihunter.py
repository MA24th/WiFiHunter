#!/usr/bin/env python3

# Note: 
# This script runs WiFiHunter from within a cloned git repo.
# The script `bin/wifihunter` is designed to be run after installing (from /usr/sbin), 
# not from the cwd.

from wifihunter import __main__
__main__.entry_point()
