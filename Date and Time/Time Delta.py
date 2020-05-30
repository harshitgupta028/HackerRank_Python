from datetime import datetime as dt
date_format= "%a %d %b %Y %H:%M:%S %z"
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), date_format) - dt.strptime(input(), date_format)).total_seconds())))