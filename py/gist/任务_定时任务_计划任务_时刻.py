import time
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler

def job_function():
    print('Tick! The time is: %s' % datetime.now())

scheduler = BackgroundScheduler()
# 周一到周日，每天凌晨执行任务
scheduler.add_job(job_function, 'cron', day_of_week='0-6', hour='0')
scheduler.start()

try:
    while True:
        time.sleep(60)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    print(u'[Error] 定时任务停止: 遇到错误!')