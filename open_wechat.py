import pyautogui
import time
def open_wc():
    time.sleep(5)
    lacation = pyautogui.locateCenterOnScreen('1122.png')
    buttonx, buttony = lacation
    pyautogui.doubleClick(buttonx,buttony)
    time.sleep(2)
    pyautogui.click(686,445)
    time.sleep(20)
if __name__ == '__main__':
    open_wc()
    # pyautogui.click(buttonx, buttony, clicks=2, interval=0, button='left')