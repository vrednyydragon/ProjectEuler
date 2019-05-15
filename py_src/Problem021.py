# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b
# are an amicable pair and each of a and b are called amicable numbers.
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
#  therefore d(220) = 284.
# The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
# Evaluate the sum of all the amicable numbers under 10000.
class AmicableNumbers():

    def FindDivisors(self, input_data):
        assert 0 < int(input_data), "Вводимые данные должны быть числами больше 0 числами и целыми!!!"
        number = int(input_data)
        numb_B = 0
        numb_C = 0
        divisors_A = []
        divisors_B = []
        for numb_A in range(number, 0, -1):
            #print("numb_A = "+str(numb_A))
            numb_B = 0
            numb_C = 0
            divisors_A = []
            divisors_B = []
            for i in range (1, int(numb_A/2+1)):
                    if numb_A%i == 0:
                        # print (i)
                        divisors_A.append(i)
            for i in divisors_A:
                numb_B += i
            # print(divisors_A)
            # print(numb_B)
            for k in range (1, int(numb_B/2+1)):
                    if numb_B%k == 0:
                        # print (i)
                        divisors_B.append(k)
            # print(divisors_B)
            for x in divisors_B:
                numb_C += x
            # print(numb_C)
            #print("numb_B = " + str(numb_B))
            #print("numb_C = " + str(numb_C))
            if numb_A == numb_C and numb_A!= numb_B:
                print("Дружественная пара найдена: " + str(numb_A) +":" + str(numb_B))

            # else:
            #     print('нет никакой дружественной пары')
            return numb_A, numb_B



if __name__ == "__main__":
    n = AmicableNumbers()
    print(n.FindDivisors(10000))
    # print(n.GeneratorNumb(220))
