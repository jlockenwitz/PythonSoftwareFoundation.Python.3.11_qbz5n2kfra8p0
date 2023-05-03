import pyautogui
import time
import keyboard
import pyperclip

def banner_process():
    banner_id = pyperclip.paste()
    banner_window = pyautogui.getWindowsWithTitle('Oracle Fusion Middleware Forms Services')[0]
    banner_window.activate()
    # pyautogui.click(770, 950)
    # make sure we're in the Go To field. If so, type DIST
    pyautogui.write('dist')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'f4')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f4')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'f4')
    time.sleep(1)
    pyautogui.write(banner_id)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'pagedown')
    pyautogui.press('f6')
    pyautogui.write('202303')
    pyautogui.press('tab')
    pyautogui.write('hdist')

keyboard.add_hotkey('ctrl+alt+b', banner_process) # set the keyboard shortcut to activate the function
keyboard.wait('ctrl+alt+q') # set the keyboard shortcut to stop the program