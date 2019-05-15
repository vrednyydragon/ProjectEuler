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

class DaysYears():

    def DayOfWeek(self, y, m, d):  # 1991 03 03 -  Sunday
        months = {1: '31', 2: '28', 3: '31', 4: '30', 5: '31', 6: '30', 7: '31',
                  8: '31', 9: '30', 10: '31', 11: '30', 12: '31'}
        years_day = 0
        sum_days = 0

        for yy in range(1900, y):
            # if (yy % 4 > 0 and  yy % 400 > 0):
            #     print(str(yy) + " - " + str(365))
            #     years_day = 365
            # else:
            #     print(str(yy) + " - " + str(366))
            #     years_day = 366
            # VV
            if (yy % 4 == 0 and yy % 100 > 0) or (yy % 4 == 0 and yy % 100 == 0 and yy % 400 == 0):
                #print(str(yy) + " - " + str(366))
                years_day = 366
            else:
                #print(str(yy) + " - " + str(365))
                years_day = 365


            sum_days += years_day
        #print(sum_days)
        for mm in range(1, 13):
            if mm == m:
                break
            if mm == 2 and y % 4 == 0:
                sum_days += 1
            sum_days += int(months[mm])
        #print(sum_days)
        sum_days += d
        #print(sum_days)

        to_ret = sum_days % 7
        if to_ret == 0:
            to_ret = 7

        return to_ret

    def WhatDay(self, input_data1, input_data2, input_data3):
        data1 = int(input_data1)
        data2 = int(input_data2)
        day_of_week = int(input_data3)
        sum_day = 0
        days = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday",
                5:"Friday", 6:"Saturday", 7:"Sunday"}
        # months = {1:'january', 2:'february', 3:'march', 4:'april', 5:'may', 6:'june', 7:'july',
        #           8:'august', 9:'september', 10:'october', 11:'november', 12:'december'}
        for yy in range(data1, data2):
            for mm in range(1, 13):
                #d = datetime.datetime(yy, mm, 1).isoweekday()
                d = self.DayOfWeek(yy, mm, 1)
                if d == day_of_week:
                    sum_day += 1
        print(days[day_of_week])
        return sum_day



if __name__ == "__main__":
    # print(Sequence.GeneratingOfSequence(13))
    n = DaysYears()
    print(n.WhatDay(1901, 2001, 7))
    # print(n.DayOfWeek(1987, 12, 17))