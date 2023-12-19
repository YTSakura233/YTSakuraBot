"""
@author: YTSakura
@file: scheduler_mission.py
创建定时任务
"""
import itchat
import tomorrow


# 获取明天是否为工作日
def tomorrow_data():
    date_type = tomorrow.get_data()
    if date_type == 0:
        itchat.send_msg(msg='明天是工作日', toUserName='@fdde0f48da792464dfcb562502cdc1c6f517dc1b1b9b55b5fc7b0a0faa81cd0f')
    elif date_type == 1:
        itchat.send_msg(msg='明天是周末', toUserName='@fdde0f48da792464dfcb562502cdc1c6f517dc1b1b9b55b5fc7b0a0faa81cd0f')
    elif date_type == 2:
        itchat.send_msg(msg='明天是假日', toUserName='@fdde0f48da792464dfcb562502cdc1c6f517dc1b1b9b55b5fc7b0a0faa81cd0f')
    elif date_type == 3:
        itchat.send_msg(msg='明天调休，需要上班', toUserName='@fdde0f48da792464dfcb562502cdc1c6f517dc1b1b9b55b5fc7b0a0faa81cd0f')
