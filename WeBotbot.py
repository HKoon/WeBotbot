# -*- coding: UTF-8 -*-
import WeBotbot_setting as ws
import itchat #微信核心库
import os
import time
import win32api,win32con #提示框库
import requests
import json
from threading import Thread #多线程
from apscheduler.schedulers.blocking import BlockingScheduler #计划任务
import io #发送图片使用

def get_UserName(names):
    guan = []
    for get_name in names:
        try:
            guan.append(itchat.search_friends(remarkName=get_name)[0]['UserName']) #备注名匹配
        except:
            try:
                guan.append(itchat.search_friends(nickName=get_name)[0]['UserName']) #昵称匹配
            except:
                try:
                    guan.append(itchat.search_friends(Alias=get_name)[0]['UserName']) #微信号匹配

                except:
                    print('没找到'+str(get_name)+'这号人物')
    return guan

# 设置计划任务模块
def scheduler():
    sched = BlockingScheduler()
    sched.add_job(send_notice, 'cron', hour=11,minute=59,second=59) #定时发送提醒
    sched.start()
    print('已启动计划任务')

def send_notice():
    itchat.send(ws.shutdownMsg, toUserName='filehelper')
    print('发送关机提醒')

def get_dict(lists,towhom):
    for list_dicts in lists:
        list_dict(list_dicts,towhom)

# 递归遍历字典里的内容，并按类型发送消息
def list_dict(dicts,towhom):
    if type(dicts) == list: 
        get_dict(dicts,towhom)
    else:
        print('开始遍历')
        for key,value in dicts.items():
            try: #尝试遍历子级字典或列表
                print('\nKeys:'+key)
                list_dict(value,towhom)
            except AttributeError: #不存在子级则代表已取出内容，根据类型回复消息，目前只捣鼓了 新闻 和 一般文字回复
                print('\nKeys:'+key+'value:'+str(value)+'\n')
                if key == 'text':
                    itchat.send(value,toUserName=towhom)
                if key == 'name':
                    itchat.send(value,toUserName=towhom)
                if key == 'icon' and value:
                    # 取网络图片暂存
                    url = 'http:'+str(value)
                    img = requests.get(url, stream=True)
                    imageStorage = io.BytesIO()
                    for block in img.iter_content(1024):
                        imageStorage.write(block)
                    imageStorage.seek(0)
                    itchat.send_image(imageStorage,toUserName=towhom)
                if key == 'detailurl':
                    itchat.send(value,toUserName=towhom)
                    time.sleep(1.8) #为了避免多条新闻轰炸（微信也不允许连发过多），设置了延时


def get_response(msg,user):
    print('请求图灵回复')
    # 构造了要发送给服务器的数据
    apiUrl = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": msg
            },
            "selfInfo": {
                "location": {
                    "city": "广州",
                    "province": "广东",
                    "street": "你心里"
                }
            }
        },
        "userInfo": {
            "apiKey": ws.KEY,
            "userId": user
        }
    }
    json_data = json.dumps(data) #转换为json格式
    #print(json_data)

    try:
        r = requests.post(apiUrl, data=json_data).json()
        print(r)  #返回值为列表与字典的嵌套
        val = r['results']#图灵机器人2.0 api里支持5种不同类型的回复，这一步先返回result不判断类型
        return val
    except: # 如果服务器没能正常交互（返回非json或无法连接），那么就会进入下面的return
        print("请求异常")
        # 将会返回一个None
        return

# 图灵机器人回复模块
def tuling_reply(msg,user,towhom):
    defaultReply = '闭嘴，说人话' # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    reply = get_response(msg,user) # 如果图灵Key出现问题，那么reply将会是None
    if reply:
        list_dict(reply,towhom)
    else:
        itchat.send(defaultReply, toUserName=towhom)

def get_reaction(message,userid):

    # cmd命令，可以实现远程操作电脑
    if message[0:4] == "*cmd":
        print('执行命令行')
        os.system(message.strip(message[1:5]))
    # 待机命令
    elif message == '*待机':
        print('准备待机')
        os.system('rundll32.exe powrProf.dll SetSuspendState')
        # 关机命令
    elif message == '*关机':
        print('正在关机')
        os.system('shutdown -s -t 10')
    # cmd打开应用程序 可自行修改
    elif message.split(" ")[0] == '*open':
        print('打开')
        os.system(message.split(' ')[1])
    elif message.split(" ")[0] == '*download':#下载文件指令
        itchat.send_file(message.split(' ')[1], toUserName=userid)
    elif message.split(" ")[0] == 'cd':#拦截cd命令通过os.chdir来实现目录切换
        os.chdir(msg['Text'].split(' ')[1])
    elif userid == 'filehelper':
        print('开始和小鸡儿器人聊天')
        user = 'koon'
        tuling_reply(message,user,'filehelper')
    elif message[0] == '-' or ws.robotToVip:
        print('小鸡儿机器人正在和别人聊天')
        user = userid[1:10] #取其中若干个字符做为机器人user标识
        tuling_reply(message[1:],user,userid)


    #定制提醒及回复
    if message == '-傻狗':
        win32api.MessageBox(0, '微信来消息啦', "傻狗信息",win32con.MB_OK) # 接收到消息弹框提醒
        itchat.send('来啦来啦', toUserName=userid)
    elif message == '-我是傻狗':
        itchat.send('傻狗，你咋不上天，还想关我电脑', toUserName=userid)


# 自动回应个人消息
@itchat.msg_register('Text')
def text_reply(msg):
    global flag
    message = msg['Text']
    userid = msg['FromUserName']

    # 文件助手命令逻辑
    # 如果发送消息给文件传输助手
    if msg.toUserName == 'filehelper':
        # 显示命令内容
        print(msg['Content'])
        get_reaction(message,'filehelper')
    elif userid in permissionUser: # 有权限用户同样获得控制权
        print(msg['Content'])
        get_reaction(message,userid)
    else:
        if ws.robotToAll:
            tuling_reply(message,user,userid)
            



if __name__ == '__main__':
    itchat.auto_login(hotReload=True, enableCmdQR=True)

    #多线程运行计划任务
    myplan = Thread(target=scheduler, args=())
    myplan.start()
    print('已启动多线程')

    # 根据permissionUserName内容自动取得UserName
    permissionUser = get_UserName(ws.permissionUserName)
    for username in permissionUser:
        itchat.send(ws.myMsg, toUserName=username) #发通知已经开启功能

    itchat.send(ws.usageMsg, toUserName='filehelper')
    itchat.run()
    print('已启动监听')


  