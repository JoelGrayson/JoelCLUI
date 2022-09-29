import re
import sys

# Print
system_print=print #store print() before redefining

def format(u_str): #returns with escaped color characters
    STYLE={
        'reset': '\033[00m',
        'clear': '\033[00m',
        '/': '\033[00m',
        'default': '\033[00m',
        'bold': '\033[01m',
        'underline': '\033[04m'
    }

    TXT={ #colors
        'green': '\033[92m',
        'success': '\033[92m',
        'red': '\033[91m',
        'danger': '\033[91m',
        'yellow': '\033[93m',
        'warn': '\033[93m',
        'blue': '\033[94m',
        'black': '\033[30m',
        'orange': '\033[33m',
        'purple': '\033[35m',
        'cyan': '\033[36m',
        'gray': '\033[37m',
        'lightgray': '\033[37m',
        'darkgray': '\033[90m',
        'lightred': '\033[91m',
        'lightgreen': '\033[92m',
        'lightblue': '\033[94m',
        'pink': '\033[95m',
        'lightcyan': '\033[96m'
    }

    BG={ #colors
        'bg black': '\033[40m',
        'bg red': '\033[41m',
        'bg green': '\033[42m',
        'bg orange': '\033[43m',
        'bg blue': '\033[44m',
        'bg purple': '\033[45m',
        'bg cyan': '\033[46m',
        'bg lightgray': '\033[47m',
    }

    operationsRe='('+'|'.join(list(STYLE)+list(TXT)+list(BG))+')' #regex or statement of all the special keywords
    parserRe=r'\['+operationsRe+r'\]'

    while True:
        matched=re.search(parserRe, u_str)
        if matched is None:
            break #exits when no more tags
        
        u_char=matched.groups()[0] #.group() is just '['+color+']'
        start_i=matched.start()
        end_i=matched.end()
        if 'bg ' in u_char: #background value
            u_str=u_str[0:start_i]+BG[u_char]+u_str[end_i:]
        elif u_char in list(TXT): #text value
            u_str=u_str[0:start_i]+TXT[u_char]+u_str[end_i:]
        elif u_char in list(STYLE): #style value
            u_str=u_str[0:start_i]+STYLE[u_char]+u_str[end_i:]
        else: #unknown value
            raise Exception('Unknown [symbol] matching: '+u_char)
        
        matched.start()
    
    return u_str

def print(u_str):
    system_print(format(u_str))


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
    print('2+2=[green]4[/] and 3+3=[bg red]6[/]')
    print('[yellow]Warning. [red][underline]Error[/] [green]Success[/]')
    print('[bg blue][yellow]Colorful[/] Back to normal')

    print('Status: TBD')
    move_up()
    print('[bold]Status: [green]Complete[/]')

