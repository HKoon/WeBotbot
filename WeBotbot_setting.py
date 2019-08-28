#有权限控制电脑的用户数组,将你想添加的用户昵称或备注名加入到该数组内
permissionUserName = ["单单单","观景之"]

robotToVip = True  #图灵是否自动回应有权限的用户

#是否对全部人开放机器人自动回复
robotToAll = False  #是否回应个人号

#robotToGroup = False #是否回应群聊,群聊还没做

#图灵机器人key放这里
KEY = 'fe116ee3db9b4dd78559b00183dc0c75'

#发送给文件传输助手的开启提示消息
usageMsg = u"-运行CMD命令：cmd xxx (xxx为命令)\n" \
           u"-输入 *关机 关闭电脑\n"\
           u"-输入 *待机 进入休眠模式\n" \
           u"-输入 *open dir 打开文件\n" \
           u"-输入 *download dir 下载文件\n" \
           u"-随便打字，和小鸡儿器人聊天\n" 

# 发送给指定用户的提示消息
myMsg = u"-- 寡人已经到公司搬砖啦\n"\
        u"-- 发送 -傻狗 即可弹窗提醒我回消息\n"\
        u"-- 发送 -我是傻狗 即可强制关我电脑\n"\
        u"-- 发送 -XXXX 开始和牛郎机器人聊天，可以问问天气，问新闻等等~~"

# 发送未关机提示信息
shutdownMsg = u"FUCK！！！\n"\
              u"你好像还没关机，宝贝\n"\
              u"--请输入 *关机 关闭电脑，乖~\n"