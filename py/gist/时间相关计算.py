################### 当前时间 ###################
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


################### 显示时间差 ###################
import time
start = time.time()
end = time.time()
min, sec = divmod(end-start, 60)
hour, min = divmod(min, 60)
print('%02d:%02d:%02d' % (hour, min, sec))


################### 格式化时间 ###################
import datetime
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


################### 加一天 ###################
print (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")


################### 减一小时 ###################
print(datetime.datetime.now() - datetime.timedelta(hours=1)).strftime("%Y-%m-%d %H:%M:%S")