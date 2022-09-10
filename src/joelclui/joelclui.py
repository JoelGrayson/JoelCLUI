import re
import sys
from constants import style, txt, bg

system_print=print #store print() before redefining

def print(u_str):
    operationsRe='('+'|'.join(list(style)+list(txt)+list(bg))+')' #regex or statement of all the special keywords
    parserRe=r'\['+operationsRe+r'\]'

    while True:
        matched=re.search(parserRe, u_str)
        if matched is None:
            break #exits when no more tags
        
        u_char=matched.groups()[0] #.group() is just '['+color+']'
        start_i=matched.start()
        end_i=matched.end()
        if 'bg ' in u_char: #background value
            u_str=u_str[0:start_i]+bg[u_char]+u_str[end_i:]
        elif u_char in list(txt): #text value
            u_str=u_str[0:start_i]+txt[u_char]+u_str[end_i:]
        elif u_char in list(style): #style value
            u_str=u_str[0:start_i]+style[u_char]+u_str[end_i:]
        else: #unknown value
            raise Exception('Unknown [symbol] matching: '+u_char)
        
        matched.start()
    
    system_print(u_str)


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


def test():
    print('2+2=[green]4[/] and 3+3=[bg red]6[/]')
    print('[yellow]Warning. [red][underline]Error[/] [green]Success[/]')
    print('[bg blue][yellow]Colorful[/] Back to normal')

    print('Status: TBD')
    move_up()
    print('[bold]Status: [green]Complete[/]')
