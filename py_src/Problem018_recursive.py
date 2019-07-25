class cChainNode():
    value = -1
    x = -1
    y = -1
    fullChainSum = 0

    def __init__(self, in_value, in_x, in_y):
        self.value = in_value
        self.x = in_x
        self.y = in_y

    def print(self):
        print("value = <" + str(self.value) + "> x = <" + str(self.x) + "> y = <" + str(self.y) + "> Sum = <" + str(self.fullChainSum) + ">")

    def increase(self, val):
        self.fullChainSum += val


class Problem018_recursive():
    testARR1 = [[3]
                , [7, 4]
                , [2, 4, 6]
                , [8, 5, 9, 3]]

    testARR2 = [[75]
        , [95, 64]
        , [17, 47, 82]
        , [18, 35, 87, 10]
        , [20, 4, 82, 47, 65]
        , [19, 1, 23, 75, 3, 34]
        , [88, 2, 77, 73, 7, 63, 67]
        , [99, 65, 4, 28, 6, 16, 70, 92]
        , [41, 41, 26, 56, 83, 40, 80, 70, 33]
        , [41, 48, 72, 33, 47, 32, 37, 16, 94, 29]
        , [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14]
        , [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57]
        , [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48]
        , [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31]
        , [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

    triangle_data = testARR2

    def prepChainObjList(self):
        to_ret = []
        for x in range(len(self.triangle_data)):
            single_nodelist = []
            for y in range(len(self.triangle_data[x])):
                c = cChainNode(self.triangle_data[x][y], x, y)
                single_nodelist.append(c)
                # c.print()
            to_ret.append(single_nodelist)
        #print(to_ret)
        return to_ret

    def calcChainObjList(self, objlist, x, y):
        to_ret = 0
        xExitCondition = len(objlist)
        if (x == xExitCondition):
            return 0
        yExitCondition = len(objlist[x])
        if (y == yExitCondition):
            return 0

        max_val = 0
        max_val = objlist[x][y].value + max(self.calcChainObjList(objlist, x + 1, y),
                                            self.calcChainObjList(objlist, x + 1, y + 1))
        objlist[x][y].increase(max_val)
        return max_val

    def printChainObjList(self,objlist):
        # get max len from last element of triangle
        maxstrlen = len(self.triangle_data[len(self.triangle_data) - 1])
        maxstrlen = (maxstrlen - 1) * 2

        for x in range(len(objlist)):
            str2print = ""
            singleRowlist = []
            for y in range(len(objlist[x])):
                singleRowlist.append(objlist[x][y].fullChainSum)

            z = singleRowlist.index(max(singleRowlist))

            for j in range(len(self.triangle_data[x])):
                if j == z:
                    str2print += "[" + str(self.triangle_data[x][j]) + "]"
                else:
                    str2print += " " + str(self.triangle_data[x][j])
            str2print = " " * (maxstrlen - len(self.triangle_data[x])) + str2print
            print(str2print)

    def runCalcUsingObj(self):
        TriangleObjList = self.prepChainObjList()
        max_val = self.calcChainObjList(TriangleObjList, 0, 0)
        print("max sum " + str(max_val))
        self.printChainObjList(TriangleObjList)

    def main(self):
        print("Start")
        # obj
        self.triangle_data = self.testARR1
        self.runCalcUsingObj()
        self.triangle_data = self.testARR2
        self.runCalcUsingObj()
        print("end")


if __name__ == "__main__":
    n = Problem018_recursive()
    n.main()