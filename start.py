from AutoSend.open_windows import Open_Windows
from AutoSend.WechatQQsend import wechat_send_message
from AutoSend.open_wechat import open_wc
names=[]#names是一个包含好友姓名的字符串的列表
messages=[]#messages是一个包含发送信息的字符串的列表

if __name__ == '__main__':
    open_wc()
    ow=Open_Windows(5).run() #5处传递的是次数.run是运行,如果出现订阅号是打不开的，而且每10个自测一次
    ws=wechat_send_message(names,messages)
    ws.run()
