from .utilities.color import Color
from . import WiFiHunter

try:
    from .config import Configuration
except (ValueError, ImportError) as e:
    raise Exception(
        'You may need to run wifihunter from the root directory (which includes README.md)', e)

# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com

def start():
    try:
        wifihunter = WiFiHunter()
        wifihunter.setup()
    except Exception as e:
        Color.pexception(e)
        Color.pl('\n{!} {R}Exiting{W}\n')

    except KeyboardInterrupt:
        Color.pl('\n{!} {O}Interrupted, Shutting down...{W}')

    Configuration.exit_gracefully(0)