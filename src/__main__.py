import os
import sys
# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com

try:
    from .config import Configuration
except (ValueError, ImportError) as e:
    raise Exception(
        'You may need to run wifihunter from the root directory (which includes README.md)', e)

from .handlers.color import Color


class WiFiHunter(object):

    def __init__(self):
        '''Initializes Wifihunter. 
        Checks for root permissions and ensures dependencies are installed.'''

        self.print_banner()

        Configuration.initialize(load_interface=False)

        if os.getuid() != 0:
            Color.pl('{!} {R}error: {O}wifihunter{R} must be run as {O}root{W}')
            Color.pl('{!} {R}re-run with {O}sudo{W}')
            Configuration.exit_gracefully(0)

        from .plugins.dependency import Dependency
        Dependency.run_dependency_check()

    def start(self):
        '''Starts target-scan + attack loop, 
        OR launches utilities dpeending on user input.'''

        from .handlers.result import CrackResult
        from .handlers.handshake import Handshake
        from .handlers.crack import CrackHelper
        if Configuration.show_cracked:
            CrackResult.display()

        elif Configuration.check_handshake:
            Handshake.check()

        elif Configuration.crack_handshake:
            CrackHelper.run()

        else:
            Configuration.get_monitor_mode_interface()
            self.scan_and_attack()

    def print_banner(self):
        ''' Displays ASCII Art '''

        Color.pl(r'{G}   **** {R}WiFiHunter{G} ****{W}')
        Color.pl(r'{G} ,***. .*. {R}1.0{G} .*. .***,{W}')
        Color.pl(r'{G}.***  ****     ****  ***.{W}')
        Color.pl(r'{G}***, ***, ,***, ,*** ,***{W}')
        Color.pl(r'{G}***. *** .*****. *** .***{W}')
        Color.pl(r'{G}***, *\\, ,|||, ,//* ,***{W}')
        Color.pl(r'{G}.\\\  \\\\.,.,.////  ///.{W}')
        Color.pl(r'{G} .\\\, .,.,,,,,.,. ,///.{W}')
        Color.pl(r'{G}   \\\*   {W},***,{G}   *///{W}')
        Color.pl(r'{W}          ,***,{W} {O}Author:{P} Mustafa Asaad{W}')
        Color.pl(r'{W}          ,***,{W} {O}Email:{P} ma24th@yahoo.com{W}')
        Color.pl(r'=======================================')

    def scan_and_attack(self):
        '''
        1) Scans for targets, asks user to select targets
        2) Attacks each target
        '''

        Color.pl('')
        from .handlers.scanner import Scanner
        # Scan
        s = Scanner()
        targets = s.select_targets()

        from .tools.all import AttackAll
        # Attack
        attacked_targets = AttackAll.attack_multiple(targets)

        Color.pl('{+} Finished attacking {C}%d{W} target(s), exiting' %
                 attacked_targets)


def entry_point():
    try:
        wifihunter = WiFiHunter()
        wifihunter.start()
    except Exception as e:
        Color.pexception(e)
        Color.pl('\n{!} {R}Exiting{W}\n')

    except KeyboardInterrupt:
        Color.pl('\n{!} {O}Interrupted, Shutting down...{W}')

    Configuration.exit_gracefully(0)


if __name__ == '__main__':
    entry_point()
