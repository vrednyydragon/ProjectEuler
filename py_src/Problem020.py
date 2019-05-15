# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!
class Factorial():

    def SumOfDigits(self, input_data):
        assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        number = int(input_data)
        multiply = 1
        sum = 0
        for i in range(1, number+1):
            multiply *= i
        print(multiply)
        multiply = str(multiply)
        for n in range (len(multiply)):
            # print(multiply[n])
            sum += int(multiply[n])
        # print(sum)
        return sum
if __name__ == "__main__":
    n = Factorial()
    print(n.SumOfDigits(1))