# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

class NumbersIntoWords():

    def recWordSearch(self, in_num):
        list = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven',
                8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
                20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy',
                80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}
        if in_num[0] == '0':
            if len(in_num) == 1:
                return ''
            return '' + self.recWordSearch(str(in_num[1::]))
        if len(in_num) == 4:
            return list[int(in_num[0])] + list[1000] + self.recWordSearch(str(in_num[1::]))
        if len(in_num) == 3:
            return list[int(in_num[0])] + list[100] + self.recWordSearch(str(in_num[1::]))
        if len(in_num) == 2:
            if int(in_num) >= 20:
                return list[int(in_num[0]) * 10] + self.recWordSearch(str(in_num[1::]))
            elif int(in_num) < 20 and int(in_num) > 9:
                return list[int(in_num)]
            else:
                return '' + self.recWordSearch(str(in_num[1::]))
        if len(in_num) == 1:
            return list[int(in_num[0])]

    def runrec(self,input_data):
        # assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        rez_str = self.recWordSearch(str(input_data))
        # print(rez_str)
        # print(len(rez_str))
        return len(rez_str)

    def HowManyLetters(self, input_data):
        assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        number = int(input_data)
        sum_letters = 0
        for i in range (1, number+1):
            sum_letters += self.runrec(i)
        # print(sum_letters)
        return sum_letters

if __name__ == "__main__":
    # a = input("Введите число: ")
    #print(NumbersIntoWords.HowManyLetters(5657))
    n = NumbersIntoWords()
    # print(n.runrec(5))
    print(n.HowManyLetters(100))