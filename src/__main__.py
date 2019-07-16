# -*- coding: utf-8 -*-
# @Author  : itswcg
# @File    : main.py
# @Time    : 19-1-31 上午9:54
# @Blog    : https://blog.itswcg.com
# @github  : https://github.com/itswcg

import argparse

import itchat
from apscheduler.schedulers.blocking import BlockingScheduler

parser = argparse.ArgumentParser(description='greet-girl')
parser.add_argument('-w', '--wechatAccount', required=True, help='Please echo girl wechatAccount')
parser.add_argument('-H', '--hour', required=True, help='hour')
parser.add_argument('-M', '--minute', required=True, help='minute')
parser.add_argument('-m', '--message', required=True, help='message')


def greet_girl(name, message):
    try:
        girlfriend = itchat.search_friends(wechatAccount=name)[0]
    except IndexError:
        print('Girl Not Found')
    else:
        girlfriend.send(message)


def main():
    args = parser.parse_args()

    itchat.auto_login(enableCmdQR=2)
    scheduler = BlockingScheduler()

    scheduler.add_job(greet_girl, 'cron', hour=args.hour, minute=args.minute, args=[args.wechatAccount, args.message])

    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        itchat.logout()


if __name__ == '__main__':
    main()
