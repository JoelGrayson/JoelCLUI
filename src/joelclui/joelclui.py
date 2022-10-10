import sys
from .format import format as _format, CONSTANTS

# Print
system_print=print #store print() before redefining

def format(u_str, overflow=False): #exported wrapper for _format
    return _format( u_str if overflow else u_str+'[/]' )

def print(u_str, overflow=False): #prints formatted text with a remove formatting at the end unless overflow is set to True
    system_print(format(u_str, overflow=overflow))


# Navigation
def move_up(times=1):
    sys.stdout.write(f'\x1b[{times}A')
    sys.stdout.flush()

def move_down(times=1):
    sys.stdout.write(f'\x1b[{times}B')
    sys.stdout.flush()

def move_left(times=1):
    sys.stdout.write(f'\x1b[{times}D')
    sys.stdout.flush()

def move_right(times=1):
    sys.stdout.write(f'\x1b[{times}C')
    sys.stdout.flush()


# Other
def clear_line():
    print ("\033[A\033[A")

def test():
    out='-----Text-----\n'
    for txt in CONSTANTS.TXT.keys():
        out+=f'[{txt}]{txt}[/]\n'
    out+='-----BG-----\n'
    for bg in CONSTANTS.BG.keys():
        out+=f'[{bg}]{bg}[/]\n'
    out+='-----Style-----\n'
    for style in CONSTANTS.STYLE.keys():
        out+=f'[{style}]{style}[/]\n'
    print(out)
