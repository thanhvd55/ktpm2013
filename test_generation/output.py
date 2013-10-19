#Ho va ten: Vu Duc Thanh
#Lop: 		K55C-CLC
#MSSV: 		10020322

from input import main
import random 
from itertools import *
import unittest

#Kiem tra xem doan co hop le hay ko
#Cac truong hop error cuang doan la: [a, b] [c, d]
#1. a >= b
#2. c <= b
def checkErrorArray(str):
	#Kiem tra a co lon hon hoac bang b hay ko ?
	for i in range(len(str)):
		if(str[i][0] >= str[i][1]):
			return 0
	
	#Kiem tra b co lon hon hoac bang c hay ko ?
	for i in range(len(str)):
		initValue = str[i][1]
		for j in range(i + 1, len(str)):
			if (initValue >= str[j][0] and str[i][0] <= str[j][1]):
				return 0
	return 1
	
#Tim kiem cac doan:Vidu a[1;2][3;4] tra ve: mang 2 chieu [1, 2] [3, 4]
#Nieu loi: raise exception
#Khong loi: return ve mang input Random viD: [1, 3] [4, 10]: co the tra ve [2, 5]
def findSegment(str):
	var1 = "["
	var2 = ";"
	var3 = "]"
	myArray = [[0 for j in range(2)] for i in range(str.count(";"))]
	x1 = x2 = x3 = x4 = ""
	i = j = 0
	for exact in str:
		if(x2 != "" and exact != var2):
			x1 += exact
		if(x3 != "" and exact != var3):
			x4 += exact
		#Lay gia tri thu 2 cua doan
		#viD [2,3] thi tra ve -> 3
		if(exact == var3):
			myArray[i][j] = int(x4)
			i = i + 1
			j = 0
			x1 = x2 = x3 = x4 = ""	
			
		#Lay gia tri dau ten cua doan
		#viD [2,3] thi tra ve -> 2
		if(exact == var2):
			myArray[i][j] = int(x1)
			j = j + 1
			x3 = var2
			x1 = x2 = ""
		if(exact == var1):
			x2 = var1
	if( checkErrorArray(myArray) == 0):
		raise Exception('wrong input')
	#Tao cac gia tri random tu cac doan
	else:
		listRandom = []
		i = 0
		for list in range(len(myArray)):
			listRandom.append(random.randint(myArray[i][0], myArray[i][1]))
			i = i + 1	
		return listRandom


#Doc input.py
a = main.__doc__

#Chuan hoa docstring: xoa ["\t", "\r", ":", " "]
xx = ["\t", "\r", ":", " "]
for exact1 in xx:
	a = a.strip(exact1).replace(exact1, "")
a = a.split()
myList = [0 for i in range(len(a))]
#Cap phat bo nho cho tung bien
findChar = ";"
i = 0

#Dat gia tri cho myList la mang chua cac gia tri bien a, b, c
for exact2 in a:
	#print exact2
	myList[i] = findSegment(exact2)
	i = i + 1
	

class DynamicTest(unittest.TestCase):
    pass
def test_generator(a):
    def test(self):
        self.assertEqual("pass" , main(*a))
    return test

if __name__ == '__main__':
	testData = []
	#Tao ra cac ca kiem thu tu bo test
	#Nieu input ton tai(lon hon 0) thi moi tao bo test
	if(len(myList) > 0): 
		x = product(myList[0])
		for i in range(len(myList)):
			if(i < len(myList) - 1):
				x = product(x, myList[i+1])
		
		#bien testCase la 1 bo test
		for item in x:
			testCase = []
			while(len(item) == 2) :
				testCase.append(item[1])
				item = item[0]
			if(len(item) == 1):
				testCase.append(item[0])
			testCase.reverse()
			testData.append(testCase)
	
		i = 0
		for data in testData:
			test_name = 'test_' + str(i)
			i = i + 1
			test = test_generator(data)
			setattr(DynamicTest, test_name, test)
		unittest.main()