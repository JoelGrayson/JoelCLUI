import re
from .CONSTANTS import STYLE, TXT, BG

def expand_special_values(u_str): # Match Special Values
    ## Rainbow
    rainbow_chars=[TXT['red'], TXT['orange'], TXT['yellow'], TXT['green'], TXT['blue'], TXT['lightblue'], TXT['purple']]
    global rainbow_char_i
    rainbow_char_i=0

    def next_rainbow_char():
        global rainbow_char_i
        out=rainbow_chars[rainbow_char_i]
        rainbow_char_i=(rainbow_char_i+1) % len(rainbow_chars)
        return out

    matched=re.search(r'\[rainbow\]([^\\\[]*)', u_str) #matches all text except \ and [
    if matched:
        out=''
        for char in matched.groups()[0]: #group of characters
            out+=next_rainbow_char()+char
        u_str=u_str[:matched.start()]+out+u_str[matched.end()-1:]

    return u_str
    
def expand_style_txt_bg(u_str): # Match STYLE, TXT, BG
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
        else: #unknown value (never happens)
            raise Exception('Unknown [symbol] matching: '+u_char)
        
        matched.start()

    return u_str


def format(u_str): #returns with escaped color characters
    u_str=expand_special_values(u_str)
    u_str=expand_style_txt_bg(u_str)
    return u_str
