# #datetime是python处理日期和时间的标准库
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(type(now))

# #获取指定日期和时间
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20)  #用指定日期时间创建datetime
# print(dt)

# #datetime转换成timestamp
# from datetime import datetime
# dt = datetime(2015, 4, 19, 12, 20)  #用指定日期时间创建datetime
# dt.timestamp()
# # print(dt.timestamp()) #1429417200.0

# #timestamp转换为datetime
# from datetime import datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))

# # timestamp也可以直接被转换到UTC标准时区的时间：
# from datetime import datetime
# t = 1429417200.0
# print(datetime.fromtimestamp(t))    #本地时间
# print(datetime.utcfromtimestamp(t))     #UTC时间

# #str转换为datetime
# from datetime import datetime
# cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
# print(cday)
# #字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。

# # datetime转换为str
# # 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过strftime()实现的：
# from datetime import datetime
# now = datetime.now()
# print(now.strftime('%a, %b %d %H:%M'))

# #datetime加减
# from datetime import datetime, timedelta
# now = datetime.now()
# print(now)
# nt = now + timedelta(hours=10)
# print(nt)
# ot = now - timedelta(hours=5)
# print(ot)
# dt = now + timedelta(days=1, hours=5)
# print(dt)
# # 可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。

# # 本地时间转化为UTC时间
# from datetime import datetime, timedelta, timezone
# tz_utc_8 = timezone(timedelta(hours=8))     #创建时区UTC+8:00
# now = datetime.now()
# print(now)
# dt = now.replace(tzinfo=tz_utc_8)
# print(dt)

# # 时区转换
# from datetime import datetime,timezone,timedelta
# utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
# print(utc_dt)
#
# bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
# # astimezone()将转换时区为东京时间:
# tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
# print(tokyo_dt)

# datetime表示的时间需要时区信息才能确定一个特定的时间，否则只能视为本地时间。
# 如果要存储datetime，最佳方法是将其转换为timestamp再存储，因为timestamp的值与时区完全无关。
