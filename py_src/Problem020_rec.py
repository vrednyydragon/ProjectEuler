# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

class Factorial():

    def SumOfDigits(self, input_data):
        assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        number = str(self.recFactorial(input_data))
        sum = 0
        for n in range (len(number)):
            # print(number[n])
            sum += int(number[n])
        # print(sum)
        print(number)
        return sum

    def recFactorial(self, input_data):
        n = int(input_data)
        if n == 0:
            return 1
        return self.recFactorial(n - 1) * n


if __name__ == "__main__":
    n = Factorial()
    print(n.SumOfDigits(10))
    # print(n.recFactorial(10))
