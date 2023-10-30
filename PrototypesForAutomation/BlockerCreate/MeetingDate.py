import datetime

def meetingdate(week,week_day):
    _, week_number, _, month, year = week.split()
    # week 6, 2023

    # dictionary to map week_day to a number where week starts from Monday (ISO 8601 standard)
    day_num_dict = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}

    week = int(week_number)
    year = int(year)
    day_of_week = day_num_dict[week_day]  # 1 = Monday, 2 = Tuesday, ..., 7 = Sunday

    # subtract 1 as Python date.weekday() is zero-based (Monday is 0, Tuesday is 1, ..., Sunday is 6)
    #day_of_week -= 1

    # get first day of the year
    first_day_of_year = datetime.date(year, 1, 1)

    # if the first day is 4 (Thursday) later than or is Thursday, count this week as week 1 of the year
    if first_day_of_year.weekday() > 3:
        first_day_of_year = first_day_of_year + datetime.timedelta(7 - first_day_of_year.weekday())
    else:  # else shift the date to next Monday
        first_day_of_year = first_day_of_year - datetime.timedelta(first_day_of_year.weekday())

    # add (week_number-1)*7 days + (day_of_week) days
    target_date = first_day_of_year + datetime.timedelta(days=((week - 1) * 7) + day_of_week)

    print("Week {} of {} on {} is: {}".format(week, year, week_day, target_date))
    return target_date

#meetingdate("Week 6 of February 2023","Thursday")