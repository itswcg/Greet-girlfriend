# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : main.py
# @Time    : 19-1-31 上午9:54
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

import argparse

import itchat
from apscheduler.schedulers.blocking import BlockingScheduler

parser = argparse.ArgumentParser(description='greet-girlfriend')
parser.add_argument('-n', '--name', required=True, help='Please echo girl-name')


def greet_girlfriend(name, message):
    try:
        girlfriend = itchat.search_friends(name=name)[0]
    except IndexError:
        print('Girlfriend Not Found')
    else:
        girlfriend.send(message)


if __name__ == '__main__':
    args = parser.parse_args()

    itchat.auto_login(hotReload=True, enableCmdQR=2)
    scheduler = BlockingScheduler()

    # Todo 每次随机时间段，随机问候语
    scheduler.add_job(greet_girlfriend, 'cron', hour=7, minute=0, args=[args.name, '早安, 宝贝'])
    scheduler.add_job(greet_girlfriend, 'cron', hour=23, minute=0, args=[args.name, '晚安, 宝贝'])

    try:
        scheduler.start()
    except:
        pass
