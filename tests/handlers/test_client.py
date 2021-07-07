from wifihunter.handlers.client import Client

def test_client():
    fields = 'AA:BB:CC:DD:EE:FF, 2020-01-01 00:00:01, 2020-01-01 00:00:05, -67, 2, (not associated), HOME-ABCD'.split(
        ',')
    c = Client(fields)
    print('Client', c)
