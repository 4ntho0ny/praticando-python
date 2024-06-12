import pyautogui as pg
import time

pg.press('win')
pg.typewrite('notepad')
pg.press('enter')
time.sleep(2)
pg.typewrite('Olá Mundo')
time.sleep(2)
pg.hotkey('ctrl', 's')
pg.typewrite('ex.txt')
time.sleep(2)
pg.press('enter')
pg.press('enter')
pg.press('enter')