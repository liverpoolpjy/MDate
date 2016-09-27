```
now = datetime.now()
mdate = MDate()
```
获取上个月的今天:
```
print mdate.last_month_date(now)
>>>2016-08-27 19:56:32.672000
```
获取近一年的月份列表，方便用于图表时间轴
```
print mdate.month_list_for_recent_year(now)
>>>[10, 11, 12, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
获取近一年月份起止时间点列表，方便用于数据查询的时间条件
```
print mdate.start_and_end_time_list_for_recent_year(now)
>>>[[datetime.datetime(2015, 10, 1, 0, 0), datetime.datetime(2015, 10, 31, 23, 59, 59)], [datetime.datetime(2015, 11, 1, 0, 0), datetime.datetime(2015, 11, 30, 23, 59, 59)], [datetime.datetime(2015, 12, 1, 0, 0), datetime.datetime(2015, 12, 31, 23, 59, 59)], [datetime.datetime(2016, 1, 1, 0, 0), datetime.datetime(2016, 1, 31, 23, 59, 59)], [datetime.datetime(2016, 2, 1, 0, 0), datetime.datetime(2016, 2, 29, 23, 59, 59)], [datetime.datetime(2016, 3, 1, 0, 0), datetime.datetime(2016, 3, 31, 23, 59, 59)], [datetime.datetime(2016, 4, 1, 0, 0), datetime.datetime(2016, 4, 30, 23, 59, 59)], [datetime.datetime(2016, 5, 1, 0, 0), datetime.datetime(2016, 5, 31, 23, 59, 59)], [datetime.datetime(2016, 6, 1, 0, 0), datetime.datetime(2016, 6, 30, 23, 59, 59)], [datetime.datetime(2016, 7, 1, 0, 0), datetime.datetime(2016, 7, 31, 23, 59, 59)], [datetime.datetime(2016, 8, 1, 0, 0), datetime.datetime(2016, 8, 31, 23, 59, 59)], [datetime.datetime(2016, 9, 1, 0, 0), datetime.datetime(2016, 9, 27, 19, 56, 32, 672000)]]
```
获取近一天起止时间点列表
```
print mdate.start_and_end_time_list_for_recent_day(now)
>>>[datetime.datetime(2016, 9, 26, 19, 56, 33, 672000), datetime.datetime(2016, 9, 27, 19, 56, 32, 672000)]
```