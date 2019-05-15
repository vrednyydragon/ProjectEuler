# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# datetime.isoweekday() - день недели в виде числа, понедельник - 1, воскресенье - 7.
# date(year, month, day)
import datetime
from datetime import date
import calendar

class DaysYears():

    def WhatDay(self, input_data1, input_data2, input_data3):
        data1 = int(input_data1)
        data2 = int(input_data2)
        day_of_week = int(input_data3)
        sum_day = 0
        days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",
                5:"Friday", 6:"Saturday", 7:"Sunday"}
        # kwargs**
        for yy in range(data1, data2):
            for mm in range(1, 13):
                d = datetime.datetime(yy, mm, 1).isoweekday()
                if d == day_of_week:
                    sum_day += 1
                    # print(d)
                    # print(sum_day)
                    # print(days[d])
                    
        # print('Столько ' + str(days[day_of_week]) + ' выпало на первое число месяца в двадцатом веке')
        print('Столько ' + str(calendar.day_name[day_of_week-1]) + ' выпало на первое число месяца в двадцатом веке')
        return sum_day


if __name__ == "__main__":
    # print(Sequence.GeneratingOfSequence(13))
    n = DaysYears()
    print(n.WhatDay(1901, 2001, 7))