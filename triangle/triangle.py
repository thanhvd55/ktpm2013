#Kiem tra bien dau vao
import ast
import sys
from math import exp, expm1
import math
def KTSaiso(a, b, c) :
        if(a == b) :
                if(math.fabs(c - (a + b)) < (exp(1e-5) - 1)) :
                        return 1
                else :
                        return 0
        elif(c == b) :
                if(math.fabs(a - (c + b)) < (exp(1e-5) - 1)) :
                        return 1
                else :
                        return 0
        elif(c == a) :
                if(math.fabs(b - (a + c)) < (exp(1e-5) - 1)) :
                        return 1
                else :
                        return 0

def CheckType(a, b, c) :
        if(a > math.pow(2,32) or a > math.pow(2,32) or a > math.pow(2,32)) :
                return "Overflow:"
	elif(not isinstance(a, float) or  not isinstance(b, float) or not isinstance(c, float)) :
		return "Not correct type: float"
	elif(a <= 0 or b <= 0 or c <= 0 or (a + b) <= c or (a + c) < b or (b + c) <= a ) :
		return "Not correct type: triangle"
	elif ( (a == b) and (KTSaiso (pow(a, 2), pow(b, 2), pow(c, 2)))) :
                return "Tam giac vuong can: Tai C"
        elif ( (c == b) and (KTSaiso (pow(a, 2), pow(b, 2), pow(c, 2)))) :
                return "Tam giac vuong can: Tai B"
	elif ( (a == c) and (KTSaiso (pow(a, 2), pow(b, 2), pow(c, 2)))) :
                return "Tam giac vuong can: Tai A" 
	elif ( (pow(a, 2) + pow(b, 2) == pow(c, 2)) ) :
                return "Tam giac vuong A"
	elif ( (pow(b, 2) + pow(c, 2) == pow(a, 2)) ) :
                return "Tam giac vuong B"
        elif ( (pow(c, 2) + pow(a, 2) == pow(b, 2)) ) :
                return "Tam giac vuong C"
	elif( (a == b) and (a == c) ) :
		return "Tam giac deu"
	elif (a == b) :
                return "Tam giac can A"
        elif (a == c) :
                return "Tam giac can B"
        elif (b == c) :
                return "Tam giac can C"
	else :
                return "Tam giac thuong"
 
