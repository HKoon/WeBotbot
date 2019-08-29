#有权限控制电脑的用户数组,将你想添加的用户昵称或备注名加入到该数组内
permissionUserName = ["Idea京儿","单单单"]

robotToVip = True  #图灵是否自动回应有权限的用户

#是否对全部人开放机器人自动回复
robotToAll = False  #是否回应个人号

#robotToGroup = False #是否回应群聊,群聊还没做

#图灵机器人key放这里
KEY = 'fe116ee3db9b4dd78559b00183dc0c75'

#发送给文件传输助手的开启提示消息
usageMsg = u"-发送 *cmd|xxx (xxx为命令) 即可执行cmd命令\n" \
           u"-发送 *关机 关闭电脑\n"\
           u"-发送 *待机 进入休眠模式\n" \
           u"-发送 *截屏 查看当前桌面状态\n" \
           u"-发送 *授权|xxx(昵称或备注名或微信号) 添加其为授权人\n" \
           u"-发送 *夺权|xxx(昵称或备注名或微信号) 可取消其授权\n" \
           u"-发送 *open|dir 打开文件或文件夹\n" \
           u"-发送 *download|dir 下载文件\n" \
           u"-发送 *cd|dir 切换目录\n" \
           u"-发送 *cd|dir 切换目录\n" \
           u"-发送 *plan|0:0:0(时间)|xxx(提醒消息) 可以设定提醒 (注:时间十位数不能为0,即不允许00、01等)\n" \
           u"-发送 *delplan 可以清空提醒\n" \
           u"-发送 *观诗音来 开启小鸡儿机器人自动回复\n" \
           u"-发送 *观诗音走 关闭小鸡儿机器人自动回复\n" \
           u"-发送 *开大 开启全局的小鸡儿机器人自动聊天，撩全场\n" \
           u"-发送 *闭嘴 关闭小鸡儿机器人自动撩全场\n" \
           u"-随便打字，和小鸡儿器人聊天" 

# 发送给指定用户的提示消息
myMsg = u"-- 朕已将电脑授权与你\n"\
        u"-发送 *傻狗 即可弹窗提醒我回消息\n"\
        u"-发送 *我是傻狗 即可强制关我电脑\n"\
        u"-发送 *待机 进入休眠模式\n" \
        u"-发送 *截屏 查看当前桌面状态\n" \
        u"-发送 *open|dir 打开文件或文件夹\n" \
        u"-发送 *download|dir 下载文件\n" \
        u"-发送 *cd|dir 切换目录\n" \
        u"-发送 *plan|0:0:0(时间)|xxx(提醒消息) 可以设定提醒\n" \
        u"-发送 *观诗音来 开启小鸡儿机器人自动回复\n" \
        u"-发送 *观诗音走 关闭小鸡儿机器人自动回复\n" \
        u"-任何时候发送 -XXXX(想说的话) 开始和牛郎机器人聊天，可以问问天气，问新闻等等~~"

# 计划任务设置，目前只实现了定时发送消息

# 计划任务数
plans = 2
# 第一个任务
# 计划任务时间格式为 hours:mins:secs
timing = ['16:18:0' , '16:20:0']
# 提示信息
noticeMsg = [ {u"FUCK！！！\n"\
              u"你好像还没关机，宝贝\n"\
              u"--请发送 *关机 关闭电脑，乖~\n"
              ,
              u"放饭！！！\n"\
              u"去吃饭了，兄嘚\n"
            ]