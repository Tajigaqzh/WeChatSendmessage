import win32gui
import win32api
import win32con
import time
import win32clipboard as w

class wechat_send_message(object):

    def __init__(self,names,messages):
        self.names = names                                                   # SW_SHOWNA  用当前的大小和位置显示一个窗口，不改变活动窗口
        self.messages = messages                                               # SW_RESTORE 用原来的大小和位置显示一个窗口，同时令其进入活动状态
                                                                             # SW_SHOWMAXIMZED 显示最大化的窗口
    def FindWindow(self,name):                                               # SHOWMINOACTIVE  最小化一个窗口，但不该表活动窗口
        win = win32gui.FindWindow(None, name)
        if win != 0:                                                         # 其他的：SW_HIDE 隐藏窗口，激活另一窗口
            win32gui.ShowWindow(win, win32con.SW_SHOWMINIMIZED)              # 展示最小化的窗口
            win32gui.ShowWindow(win, win32con.SW_SHOWNORMAL)                 # 与SW_RESTORE相同
            win32gui.ShowWindow(win, win32con.SW_SHOW)                       # 用当前的大小和位置显示一个窗口
            win32gui.SetWindowPos(win, win32con.HWND_TOPMOST, 100, 100, 500, 500, win32con.SWP_SHOWWINDOW)#第二个参数是置顶，前两个数字是位置，后两个数字是大小，最后一个是显示
            win32gui.SetForegroundWindow(win)  # 获取控制
            time.sleep(0.5)

        else:
            print('找不到该窗口，请双击联系人{}，保证其是一个单独的窗口'.format(name))
        return win

    def SetText(self,aString):
        w.OpenClipboard()                                      #打开剪切板
        w.EmptyClipboard()                                     #清空
        w.SetClipboardData(win32con.CF_UNICODETEXT, aString)    #写入
        w.CloseClipboard()                                      #关闭
    def ZhanTie(self):
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    def HuiChe(self):
        win32api.keybd_event(18, 0, 0, 0)  # Alt键位码
        win32api.keybd_event(83, 0, 0, 0)  # s键位码
        win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键

    def run(self):
        for name in self.names:
            for message in self.messages:
                win = self.FindWindow(name)
                if win != 0:
                    self.SetText(message)
                    self.ZhanTie()
                    self.HuiChe()
                    print("发给联系人 {} 的消息已经发送成功".format(name))
                else:
                    pass

if __name__ == '__main__':
    names = ['尼不到五千','Sister','文件传输助手']
    messages = ['测试代码']
    wechat_send_message(names,messages).run()
