
"""
Coding Dojo realizado no Instituto Federal de Pernambuco (IFPE) no dia 26/03/2011.

Problema:
Sampling

Link: http://rubyquiz.com/quiz39.html


"""



import unittest
import random

class AmostrasTest(unittest.TestCase):
    def testQuantidadeTres(self):
        self.assertEquals(len(amostra(3,10)), 3)

    def testAmostrasDez(self):
        self.assertTrue(max(amostra(3,10)) <= 10)
    
    def testQuantidadeQuatro(self):
        self.assertEquals(len(amostra(4,15)), 4)
    
    def testAmostraTres(self):
        self.assertTrue( max(amostra(4, 2)) <= 2)
    
    def testAmostraZeroZero(self):
        self.assertEquals( amostra(0, 0), [])
    
    def testAmostraZeroDez(self):
        self.assertEquals( amostra(0, 10), [])
    
    def testAmostraDezZero(self):
        self.assertEquals( len( amostra(10, 0) ), 10)

    def testAmostraInRange(self):
        self.assertTrue(len([ i for i in amostra(3,10) \
                     if i in range(10)]) > 0)


amostra = lambda quantidade,limite:[  random.randint(0,limite)  for i in range(quantidade)  ]
  




if __name__ == '__main__':
    unittest.main()

