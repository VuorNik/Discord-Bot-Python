import webbrowser
import random
from datetime import datetime

def ruokalista(num):
  
    with open('ruoat.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    x = len(lines)
    howmany = num
    menu = get_list(x, howmany, lines)

    return menu


def get_list(length, howmany, lines):
    if howmany <= length:
        raw = random.sample(lines, howmany)
        menu = []
        for name in raw:
            menu.append(name.strip('\n'))            
        return menu
    else:
        print('valitse vähemmän')
