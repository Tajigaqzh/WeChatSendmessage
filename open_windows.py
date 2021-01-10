import time
import pyautogui

class Open_Windows(object):
    def __init__(self,times):
        self.times=times

    def first_step_open_windows(self):
        pyautogui.doubleClick(422, 211)  # 打开第一个页面
        time.sleep(0.2)
        pyautogui.click(607, 142)  # 关闭第一个页面
        time.sleep(0.2)

    def open_windows(self):
        pyautogui.doubleClick(422, 274)  # 打开第二个页面
        time.sleep(0.3)
        pyautogui.click(607, 142)  # 关闭第二个页面
        time.sleep(0.2)

    def run(self):
        time.sleep(3)
        self.first_step_open_windows()
        number = 0
        b = [i for i in range(0, 500, 10)]
        while True:
            self.open_windows()
            number += 1
            if number in b:
                self.first_step_open_windows()
            if number == int(self.times):
                break
if __name__ == '__main__':
    ow=Open_Windows().run()
