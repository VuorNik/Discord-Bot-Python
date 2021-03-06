import random

def dice_roll(throw):
  if not 'd' in throw or len(throw)<3:
    return 'Virheelliset noppaparametrit. Käytä esim. !roll 2d6.'
    
  n, d = throw.split('d')  

  dice = [
    str(random.choice(range(1, int(d) + 1)))
    for _ in range(int(n))
  ]
  msg = f'Heiton {n}d{d} tulos on '+', '.join(dice)
  return msg
