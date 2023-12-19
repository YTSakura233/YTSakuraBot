"""
@author: YTSakura
@file: bot.py
@version: 0.1
ZoharBot主文件
"""
from apscheduler.schedulers.background import BackgroundScheduler
import itchat
import download
import tomorrow
import scheduler_mission


# 实时获取微信消息
@itchat.msg_register(itchat.content.TEXT)
def reply_content(msg):
    print("收到用户“%s”消息:%s" % (msg['FromUserName'], msg['Text']))
    if u'作者' in msg['Text'] or u'主人' in msg['Text']:
        return u'ZoharBot的作者是YTSakura，你可以在这里找到他：https://github.com/YTSakura233'
    if u'图片' in msg['Text'] or u'美图' in msg['Text']:
        if download.get_img():
            itchat.send_image('./img/' + str(download.img_count - 1) + '.jpg', msg['FromUserName'])
        else:
            return u'图片获取失败，请稍后再试。若多次失败请联系开发'
    if u'明天上班' in msg['Text']:
        type = tomorrow.get_data()
        if type == 0:
            return u'明天是工作日'
        elif type == 1:
            return u'明天是周末'
        elif type == 2:
            return u'明天为节假日'
        elif type == 3:
            return u'明天调休，需要上班'


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    scheduler = BackgroundScheduler()
    scheduler.add_job(scheduler_mission.tomorrow_data, 'cron', day_of_week='mon-sun', hour=22, minute=00)
    scheduler.start()
    itchat.run()

