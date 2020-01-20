import os
# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com

import time
from json import loads, dumps
from .color import Color
from ..config import Configuration


class CrackResult(object):
    ''' Abstract class containing results from a crack session '''

    # File to save cracks to, in PWD
    cracked_file = Configuration.cracked_file

    def __init__(self):
        self.date = int(time.time())
        self.readable_date = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(self.date))

    def dump(self):
        raise Exception('Unimplemented method: dump()')

    def to_dict(self):
        raise Exception('Unimplemented method: to_dict()')

    def print_single_line(self, longest_essid):
        raise Exception('Unimplemented method: print_single_line()')

    def print_single_line_prefix(self, longest_essid):
        essid = self.essid if self.essid else 'N/A'
        Color.p('{W} ')
        Color.p('{C}%s{W}' % essid.ljust(longest_essid))
        Color.p('  ')
        Color.p('{GR}%s{W}' % self.bssid.ljust(17))
        Color.p('  ')
        Color.p('{D}%s{W}' % self.readable_date.ljust(19))
        Color.p('  ')

    def save(self):
        ''' Adds this crack result to the cracked file and saves it. '''
        name = CrackResult.cracked_file
        saved_results = []
        if os.path.exists(name):
            with open(name, 'r') as fid:
                text = fid.read()
            try:
                saved_results = loads(text)
            except Exception as e:
                Color.pl('{!} error while loading %s: %s' % (name, str(e)))

        # Check for duplicates
        this_dict = self.to_dict()
        this_dict.pop('date')
        for entry in saved_results:
            this_dict['date'] = entry.get('date')
            if entry == this_dict:
                # Skip if we already saved this BSSID+ESSID+TYPE+KEY
                Color.pl('{+} {C}%s{O} already exists in {G}%s{O}, skipping.' % (
                    self.essid, Configuration.cracked_file))
                return

        saved_results.append(self.to_dict())
        with open(name, 'w') as fid:
            fid.write(dumps(saved_results, indent=2))
        Color.pl('{+} saved crack result to {C}%s{W} ({G}%d total{W})'
                 % (name, len(saved_results)))

    @classmethod
    def display(cls):
        ''' Show cracked targets from cracked file '''
        name = cls.cracked_file
        if not os.path.exists(name):
            Color.pl('{!} {O}file {C}%s{O} not found{W}' % name)
            return

        with open(name, 'r') as fid:
            cracked_targets = loads(fid.read())

        if len(cracked_targets) == 0:
            Color.pl('{!} {R}no results found in {O}%s{W}' % name)
            return

        Color.pl('\n{+} Displaying {G}%d{W} cracked target(s) from {C}%s{W}\n' % (
            len(cracked_targets), name))

        results = sorted([cls.load(item) for item in cracked_targets],
                         key=lambda x: x.date, reverse=True)
        longest_essid = max([len(result.essid or 'ESSID')
                             for result in results])

        # Header
        Color.p('{D} ')
        Color.p('ESSID'.ljust(longest_essid))
        Color.p('  ')
        Color.p('BSSID'.ljust(17))
        Color.p('  ')
        Color.p('DATE'.ljust(19))
        Color.p('  ')
        Color.p('TYPE'.ljust(5))
        Color.p('  ')
        Color.p('KEY')
        Color.pl('{D}')
        Color.p(' ' + '-' * (longest_essid + 17 + 19 + 5 + 11 + 12))
        Color.pl('{W}')
        # Results
        for result in results:
            result.print_single_line(longest_essid)
        Color.pl('')

    @classmethod
    def load_all(cls):
        if not os.path.exists(cls.cracked_file):
            return []
        with open(cls.cracked_file, 'r') as json_file:
            json = loads(json_file.read())
        return json

    @staticmethod
    def load(json):
        ''' Returns an instance of the appropriate object given a json instance '''
        if json['type'] == 'WPA':
            #from .wpa_result import CrackResultWPA
            result = CrackResultWPA(json['bssid'],
                                    json['essid'],
                                    json['handshake_file'],
                                    json['key'])
        elif json['type'] == 'WEP':
            #from .wep_result import CrackResultWEP
            result = CrackResultWEP(json['bssid'],
                                    json['essid'],
                                    json['hex_key'],
                                    json['ascii_key'])

        elif json['type'] == 'WPS':
            #from .wps_result import CrackResultWPS
            result = CrackResultWPS(json['bssid'],
                                    json['essid'],
                                    json['pin'],
                                    json['psk'])

        elif json['type'] == 'PMKID':
            #from .pmkid_result import CrackResultPMKID
            result = CrackResultPMKID(json['bssid'],
                                      json['essid'],
                                      json['pmkid_file'],
                                      json['key'])
        result.date = json['date']
        result.readable_date = time.strftime(
            '%Y-%m-%d %H:%M:%S', time.localtime(result.date))
        return result


class CrackResultWEP(CrackResult):
    def __init__(self, bssid, essid, hex_key, ascii_key):
        self.result_type = 'WEP'
        self.bssid = bssid
        self.essid = essid
        self.hex_key = hex_key
        self.ascii_key = ascii_key
        super(CrackResultWEP, self).__init__()

    def dump(self):
        if self.essid:
            Color.pl('{+}      ESSID: {C}%s{W}' % self.essid)
        Color.pl('{+}      BSSID: {C}%s{W}' % self.bssid)
        Color.pl('{+} Encryption: {C}%s{W}' % self.result_type)
        Color.pl('{+}    Hex Key: {G}%s{W}' % self.hex_key)
        if self.ascii_key:
            Color.pl('{+}  Ascii Key: {G}%s{W}' % self.ascii_key)

    def print_single_line(self, longest_essid):
        self.print_single_line_prefix(longest_essid)
        Color.p('{G}%s{W}' % 'WEP'.ljust(5))
        Color.p('  ')
        Color.p('Hex: {G}%s{W}' % self.hex_key.replace(':', ''))
        if self.ascii_key:
            Color.p(' (ASCII: {G}%s{W})' % self.ascii_key)
        Color.pl('')

    def to_dict(self):
        return {
            'type': self.result_type,
            'date': self.date,
            'essid': self.essid,
            'bssid': self.bssid,
            'hex_key': self.hex_key,
            'ascii_key': self.ascii_key
        }


class CrackResultWPA(CrackResult):
    def __init__(self, bssid, essid, handshake_file, key):
        self.result_type = 'WPA'
        self.bssid = bssid
        self.essid = essid
        self.handshake_file = handshake_file
        self.key = key
        super(CrackResultWPA, self).__init__()

    def dump(self):
        if self.essid:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('Access Point Name'.rjust(19), self.essid))
        if self.bssid:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('Access Point BSSID'.rjust(19), self.bssid))
        Color.pl('{+} %s: {C}%s{W}' %
                 ('Encryption'.rjust(19), self.result_type))
        if self.handshake_file:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('Handshake File'.rjust(19), self.handshake_file))
        if self.key:
            Color.pl('{+} %s: {G}%s{W}' %
                     ('PSK (password)'.rjust(19), self.key))
        else:
            Color.pl('{!} %s  {O}key unknown{W}' % ''.rjust(19))

    def print_single_line(self, longest_essid):
        self.print_single_line_prefix(longest_essid)
        Color.p('{G}%s{W}' % 'WPA'.ljust(5))
        Color.p('  ')
        Color.p('Key: {G}%s{W}' % self.key)
        Color.pl('')

    def to_dict(self):
        return {
            'type': self.result_type,
            'date': self.date,
            'essid': self.essid,
            'bssid': self.bssid,
            'key': self.key,
            'handshake_file': self.handshake_file
        }


class CrackResultWPS(CrackResult):
    def __init__(self, bssid, essid, pin, psk):
        self.result_type = 'WPS'
        self.bssid = bssid
        self.essid = essid
        self.pin = pin
        self.psk = psk
        super(CrackResultWPS, self).__init__()

    def dump(self):
        if self.essid is not None:
            Color.pl('{+} %s: {C}%s{W}' % ('ESSID'.rjust(12), self.essid))
        if self.psk is None:
            psk = '{O}N/A{W}'
        else:
            psk = '{G}%s{W}' % self.psk
        Color.pl('{+} %s: {C}%s{W}' % ('BSSID'.rjust(12), self.bssid))
        Color.pl('{+} %s: {C}WPA{W} ({C}WPS{W})' % 'Encryption'.rjust(12))
        Color.pl('{+} %s: {G}%s{W}' % ('WPS PIN'.rjust(12), self.pin))
        Color.pl('{+} %s: {G}%s{W}' % ('PSK/Password'.rjust(12), psk))

    def print_single_line(self, longest_essid):
        self.print_single_line_prefix(longest_essid)
        Color.p('{G}%s{W}' % 'WPS'.ljust(5))
        Color.p('  ')
        if self.psk:
            Color.p('Key: {G}%s{W} ' % self.psk)
        Color.p('PIN: {G}%s{W}' % self.pin)
        Color.pl('')

    def to_dict(self):
        return {
            'type': self.result_type,
            'date': self.date,
            'essid': self.essid,
            'bssid': self.bssid,
            'pin': self.pin,
            'psk': self.psk
        }


class CrackResultPMKID(CrackResult):
    def __init__(self, bssid, essid, pmkid_file, key):
        self.result_type = 'PMKID'
        self.bssid = bssid
        self.essid = essid
        self.pmkid_file = pmkid_file
        self.key = key
        super(CrackResultPMKID, self).__init__()

    def dump(self):
        if self.essid:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('Access Point Name'.rjust(19), self.essid))
        if self.bssid:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('Access Point BSSID'.rjust(19), self.bssid))
        Color.pl('{+} %s: {C}%s{W}' %
                 ('Encryption'.rjust(19), self.result_type))
        if self.pmkid_file:
            Color.pl('{+} %s: {C}%s{W}' %
                     ('PMKID File'.rjust(19), self.pmkid_file))
        if self.key:
            Color.pl('{+} %s: {G}%s{W}' %
                     ('PSK (password)'.rjust(19), self.key))
        else:
            Color.pl('{!} %s  {O}key unknown{W}' % ''.rjust(19))

    def print_single_line(self, longest_essid):
        self.print_single_line_prefix(longest_essid)
        Color.p('{G}%s{W}' % 'PMKID'.ljust(5))
        Color.p('  ')
        Color.p('Key: {G}%s{W}' % self.key)
        Color.pl('')

    def to_dict(self):
        return {
            'type': self.result_type,
            'date': self.date,
            'essid': self.essid,
            'bssid': self.bssid,
            'key': self.key,
            'pmkid_file': self.pmkid_file
        }


if __name__ == '__main__':

    # Deserialize WPA object
    Color.pl('\nCracked WPA:')
    json = loads('{"bssid": "AA:BB:CC:DD:EE:FF", "essid": "Test Router", "key": "Key", "date": 1433402428, "handshake_file": "hs/capfile.cap", "type": "WPA"}')
    obj = CrackResult.load(json)
    obj.dump()
    w = CrackResultWPA('AA:BB:CC:DD:EE:FF', 'Test Router',
                       'hs/capfile.cap', 'abcd1234')
    w.dump()

    w = CrackResultWPA('AA:BB:CC:DD:EE:FF', 'Test Router',
                       'hs/capfile.cap', 'Key')
    print('\n')
    w.dump()
    w.save()
    print(w.__dict__['bssid'])

    # Deserialize WEP object
    Color.pl('\nCracked WEP:')
    json = loads('{"bssid": "AA:BB:CC:DD:EE:FF", "hex_key": "00:01:02:03:04", "ascii_key": "abcde", "essid": "Test Router", "date": 1433402915, "type": "WEP"}')
    obj = CrackResult.load(json)
    obj.dump()

    crw = CrackResultWEP('AA:BB:CC:DD:EE:FF', 'Test Router',
                         '00:01:02:03:04', 'abcde')
    crw.dump()
    crw.save()

    # Deserialize WPS object
    Color.pl('\nCracked WPS:')
    json = loads(
        '{"psk": "the psk", "bssid": "AA:BB:CC:DD:EE:FF", "pin": "01234567", "essid": "Test Router", "date": 1433403278, "type": "WPS"}')
    obj = CrackResult.load(json)
    obj.dump()

    crw = CrackResultWPS('AA:BB:CC:DD:EE:FF',
                         'Test Router', '01234567', 'the psk')
    crw.dump()
    crw.save()

    # Deserialize PMKID object
    w = CrackResultPMKID('AA:BB:CC:DD:EE:FF', 'Test Router',
                         'hs/pmkid_blah-123213.16800', 'abcd1234')
    w.dump()

    w = CrackResultPMKID('AA:BB:CC:DD:EE:FF', 'Test Router',
                         'hs/pmkid_blah-123213.16800', 'Key')
    print('\n')
    w.dump()
    w.save()
    print(w.__dict__['bssid'])
