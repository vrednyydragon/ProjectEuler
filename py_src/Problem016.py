#2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#What is the sum of the digits of the number 2**1000?
class Degree():

    def SumOfDigits(self, input_data):
        assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        n = int(input_data)
        numb = str(2**n)
        sum_numb = 0
        print(numb)
        for x in numb:
            sum_numb += int(x)
        print(sum_numb)
        return sum_numb
if __name__ == "__main__":
    a = input("Введите степень числа: ")
    n = Degree()
    print(n.SumOfDigits(a))