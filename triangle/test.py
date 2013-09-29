# Vu Duc Thanh
# 10020322
# K55C-CLC

# Cac truong hop test
# Can tai: A, B, C
# Vuong tai A, B, C
# Vuong can tai: A, B, C
# Tam giac deu
# Input: Am, Overflow, test gia tri trung binh, tam giac thuong, a + b > c, Khong phai la tam giac

import unittest
import math
from triangle import CheckType
class TriangleTestCase(unittest.TestCase):
	
	#Kiem tra tam giac can tai A
	def testTamgiac_Can_TaiA(self):
		self.assertEqual(CheckType(2.0, 2.0, 3.0), "Tam giac can A")

	#Kiem tra tam giac can tai B
	def testTamgiac_Can_TaiB(self):
		self.assertEqual(CheckType(2.0, 3.0, 2.0), "Tam giac can B")

	#Kiem tra tam giac can tai C
	def testTamgiac_Can_TaiC(self):
		self.assertEqual(CheckType(3.0, 2.0, 2.0), "Tam giac can C")
    
	#Kiem tra tam giac deu
	def testTamgiac_Deu(self):
		self.assertEqual(CheckType(2.0, 2.0, 2.0), "Tam giac deu")
        
	#Kiem tra tam giac vuong tai C
	def testTamgiac_Vuong_TaiA(self):
		self.assertEqual(CheckType(3.0, 5.0, 4.0), "Tam giac vuong C")

	#Kiem tra tam giac vuong tai A
	def testTamgiac_Vuong_TaiB(self):
		self.assertEqual(CheckType(4.0, 3.0, 5.0), "Tam giac vuong A")

	#Kiem tra tam giac vuong tai B
	def testTamgiac_Vuong_TaiC(self):
		self.assertEqual(CheckType(5.0, 4.0, 3.0), "Tam giac vuong B")
        
	#Kiem tra tam giac vuong can tai B
	def testTamgiac_VuongCan_TaiB(self):
		self.assertEqual(CheckType(2.0, math.sqrt(2), math.sqrt(2)), "Tam giac vuong can: Tai B")

	#Kiem tra tam giac vuong can tai A
	def testTamgiac_VuongCan_TaiA(self):
		self.assertEqual(CheckType(math.sqrt(2), 2.0, math.sqrt(2)), "Tam giac vuong can: Tai A")

	#Kiem tra tam giac vuong can tai C
	def testTamgiac_VuongCan_TaiC(self):
		self.assertEqual(CheckType(math.sqrt(2), math.sqrt(2), 2.0), "Tam giac vuong can: Tai C")
		
	#Kiem tra dau vao co phai la float hay khong ?
	def testTamgiac_Type_Float(self):
		self.assertEqual(CheckType(2, 2.0, 3.0), "Not correct type: float")
        
	#Kiem tra dau vao co tham so Am hay khong ?
	def testTamgiac_Type_AM_DUONG(self):
		self.assertEqual(CheckType(-2.0, 2.0, 3.0), "Not correct type: triangle")
		
	#Kiem tra dau vao co thoa man 1 tam giac (a + b >= c ) ?
	def testTamgiac_Type(self):
		self.assertEqual(CheckType(1.0, 2.0, 3.0), "Not correct type: triangle")

        #Kiem tra dau vao vs tham so chuan: Tam giac thuong?
	def testTamgiacThuong(self):
		self.assertEqual(CheckType(4.0, 5.0, 6.0), "Tam giac thuong")

        #Kiem tra dau vao cap phat lon hon kieu float cho phep
	def testInputTamgiac_Overflow_Test1(self):
		self.assertEqual(CheckType(math.pow(2,32) + 1, 5.0, 6.0), "Overflow:")

        #Kiem tra dau vao: a > 2^32, b = 0, c is float
	def testInputTamgiac_Overflow_Test2(self):
		self.assertEqual(CheckType(math.pow(2,32) + 1, 0, 6.0), "Overflow:")

	#Kiem tra dau vao thuoc gia tri trung binh 0 > 2^32
	def testInputTamgiac_Overflow_Test2(self):
		self.assertEqual(CheckType(math.pow(2,32)/2, math.pow(2,32)/2, math.pow(2,32)/2), "Tam giac deu")
	
if __name__ == '__main__':
    unittest.main()
