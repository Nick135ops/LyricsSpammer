from time import sleep
import pyautogui

print('You have 3 secs to switch windows')
sleep(3)
with open(file='baby_lyrics.txt', mode='r') as f:
    for a_line in f:
        pyautogui.write(a_line)
        pyautogui.press('enter')
        sleep(3)
