import datetime

def convert_date(date_string):
    formats = ['%m/%d/%Y', '%d-%m-%Y', '%Y-%m-%d']
    for date_format in formats:
        try:
            return datetime.datetime.strptime(date_string, date_format).strftime('%Y-%m-%d')
        except ValueError:
            pass
    return "Unknown date format"

print(convert_date('12/31/2020'))  # 2020-12-31
print(convert_date('31-12-2020'))  # 2020-12-31
print(convert_date('2020-12-31'))  # 2020-12-31
