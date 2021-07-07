import pytest
from wifihunter.utilities.color import Color

def test_color():
    Color.pl('{R}Testing{G}One{C}Two{P}Three{W}Done')
    print(Color.s('{C}Testing{P}String{W}'))
    Color.pl('{+} Good line')
    Color.pl('{!} Danger')
    
