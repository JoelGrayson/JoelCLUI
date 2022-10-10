import sys
from format.format import format as _format

# Print
system_print=print #store print() before redefining

def format(u_str): #exported wrapper for _format
    return _format(u_str)

def print(u_str, format_overflow=False): #prints formatted text with a remove formatting at the end unless format_overflow is set to True
    system_print(format( u_str if format_overflow else u_str+'[/]' ))


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
    print('2+2=[green]4[/] and 3+3=[bg red]6')
    print('[yellow]Warning. [red][underline]Error[/] [green]Success')
    print('[bg blue][yellow]Colorful[/] Back to normal')

    print('Status: TBD')
    move_up()
    print('[bold]Status: [green]Complete')
