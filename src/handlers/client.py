# Author: Mustafa Asaad
# Date: JAN 1, 2020
# Email: ma24th@yahoo.com


class Client(object):
    '''
        Holds details for a 'Client' - a wireless device (e.g. computer)
        that is associated with an Access Point (e.g. router)
    '''

    def __init__(self, fields):
        '''
            Initializes & stores client info based on fields.
            Args:
                Fields - List of strings
                INDEX KEY
                    0 Station MAC (Client's MAC address)
                    1 First time seen,
                    2 Last time seen,
                    3 Power,
                    4 Packets,
                    5 BSSID, (Access Point's MAC address)
                    6 Probed ESSIDs
        '''
        self.station = fields[0].strip()
        self.power = int(fields[3].strip())
        self.packets = int(fields[4].strip())
        self.bssid = fields[5].strip()

    def __str__(self):
        ''' String representation of a Client '''
        result = ''
        for (key, value) in self.__dict__.items():
            result += key + ': ' + str(value)
            result += ', '
        return result


if __name__ == '__main__':
    fields = 'AA:BB:CC:DD:EE:FF, 2020-01-01 00:00:01, 2020-01-01 00:00:05, -67, 2, (not associated), HOME-ABCD'.split(
        ',')
    c = Client(fields)
    print('Client', c)
