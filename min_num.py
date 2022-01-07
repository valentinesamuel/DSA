def find_min_num(numberList):
      min_num = 0 # O(1)
      for number in numberList:
            if number < min_num: # O(n^2)
                  min_num = number # O(n^2)
      print(min_num)
# T(n) = 1 + 2(n^2)
# O(n^2)


def find_min(numberList):
      min_num=numberList[0] # O(1)
      for index in range(len(numberList)):
            if numberList[index] < min_num: # O(n)
                  min_num = numberList[index] # O(1)
      return min_num
# T(n) = 2 + O(n)
# O(n)


numlist = [5, 2, 6, 8,1,3,9,-4,0]
find_min_num(numlist)
print(find_min(numlist))