import calendar
mm,dd,yy=map(int, input().split())
print(calendar.day_name[calendar.weekday(yy, mm, dd)].upper())

