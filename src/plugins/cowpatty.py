# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com

from .dependency import Dependency
from ..config import Configuration
from ..handlers.color import Color
from ..handlers.process import Process
from ..plugins.hashcat import HcxPcapTool

import os
import re


class Cowpatty(Dependency):
    ''' Wrapper for Cowpatty program. '''
    dependency_required = False
    dependency_name = 'cowpatty'
    dependency_url = 'https://tools.kali.org/wireless-attacks/cowpatty'


    @staticmethod
    def crack_handshake(handshake, show_command=False):
        # Crack john file
        command = [
            'cowpatty',
            '-f', Configuration.wordlist,
            '-r', handshake.capfile,
            '-s', handshake.essid
        ]
        if show_command:
            Color.pl('{+} {D}Running: {W}{P}%s{W}' % ' '.join(command))
        process = Process(command)
        stdout, stderr = process.get_output()

        key = None
        for line in stdout.split('\n'):
            if 'The PSK is "' in line:
                key = line.split('"', 1)[1][:-2]
                break

        return key
