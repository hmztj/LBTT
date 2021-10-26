import unittest
from lbtt_calculator import get_lbtt, TaxBand 

class Test_experiment_main(unittest.TestCase):
    
    # tests against various input values i.e. exact limits, higher than limits, zero, decimals.
    # def test_get_lbtt(self):
        
    #     input_data = [0.0, 145000.0, 250000, 325000, 750000.0, 800000, 140000.0, 150000.0, 300000.0, 450000.0, 156000.093, 144999.99, 145000.00001, 145000.1, 145001]
        
    #     expected_outputs = [0.0, 0.0, 2100.0, 5850.0, 48350, 54350.0, 0.0, 100.0, 4600.0, 18350.0, 220.0, 0.0, 0.0, 0.0, 0.02]

    #     for i in range(0, len(input_data)):
    #         self.assertEqual(get_lbtt(input_data[i]), expected_outputs[i]) 
            
    def test_get_tax(self):
        
        test_band = TaxBand(0, 100, 0.02)
        
        p_value = 100
      
        expected = 2
        
        self.assertEqual(test_band.get_tax(p_value), expected)
        
    def test_value(self):
    
        test_band = TaxBand(100, 200, 0.02)
        
        p_value = 50
        
        expected = 0
        
        self.assertEqual(test_band.get_tax(p_value), expected)
       
    
if __name__ == '__main__':
    unittest.main()