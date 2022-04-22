from ast import Add
from asyncio.windows_events import NULL
from decimal import DivisionUndefined
import unittest
from unittest import mock
from unittest.mock import patch
from calculatorApp import *
import calculatorApp


class TestCalculate(unittest.TestCase):
    def setUp(self):
        print("Setup .. ")

   #add : 
    def test_Add(self):
        self.assertEqual(add(2,3), 5)
        
    # subtract :    
    def test_subtract(self):
        self.assertEqual(subtract(2,2), 0)  
        
    # multiply : 
    def test_multiply(self):
        self.assertEqual(multiply(5,2), 10)
        
        
    #divide 
    def test_Divide1(self):
        self.assertRaises(ZeroDivisionError, divide,5,0)    

    def test_Divide2(self):
        self.assertEqual(divide(0,10), 0)

    def test_Divide3(self):
        self.assertEqual(divide(10,2), 5)
   
   
   #is_Exit :
    def test_isExit1(self):
        self.assertEqual(isExit("no"), True)
   
    def test_isExit2(self):
        self.assertEqual(isExit("yes"), False) 
        
    def test_isExit3(self):
        self.assertRaises(ValueError, isExit, "test") 
        
        
        
    # check user 
    def test_checkUserInput1(self):
        self.assertRaises(ValueError, check_user_input, "")   
    
    def test_checkUserInput2(self):
        self.assertEqual(check_user_input(5), 5)
    
    def test_checkUserInput3(self):
        self.assertEqual(check_user_input("6.6"),6.6) ###################
        
    def test_checkUserInput4(self):
        self.assertRaises(ValueError, check_user_input, "test")    
        
    
        
        
    #calculate :
    
    def test_checkCalculate1(self):
        self.assertRaises(ZeroDivisionError, calculate ,"4",'5','0') ################################
        
    def test_checkCalculate2(self):
        self.assertRaises(Exception, calculate, "6",1,2)
      
    def test_checkCalculate3(self):
        with mock.patch('calculatorApp.add', return_value = 6):
            result = calculate('1',2,4)
        self.assertEqual(result, 6)
        
    def test_checkCalculate4(self):
        with mock.patch('calculatorApp.subtract', return_value = 5):
            result = calculate('2',10,5)
        self.assertEqual(result, 5)
        
    def test_checkCalculate5(self):
        with mock.patch('calculatorApp.multiply', return_value = 25):
            result = calculate('3',5,5)
        self.assertEqual(result, (5,'*',5,'=',25))
        
    def test_checkCalculate6(self):
        with mock.patch('calculatorApp.divide', return_value = 1):
            result = calculate('4',5,5)
        self.assertEqual(result, (5,'/',5,'=',1))
            
    def test_checkCalculate7(self):
        self.assertRaises(ValueError,calculate ,"4", NULL, 5)
        

 
if __name__ == '__main__':
	unittest.main()
 
