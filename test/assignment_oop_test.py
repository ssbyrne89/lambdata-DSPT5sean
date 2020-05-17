#assignment_oop_test.py


import unittest
from pandas import DataFrame

from my_lambdata.assignment_oop import DataProcessor

#OBJECTIVE: test the add_state_names() function from the my_lambdate/assignment.py file

class TestDataProcessor(unittest.TestCase):

    def test_add_state_names_oop(self):
        
        df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
        processor = DataProcessor(df)
        self.assertEqual(list(processor.df.columns), ['abbrev'])

        processor.add_state_names()

        
        self.assertEqual(list(processor.df.columns), ["abbrev", "name"])
        self.assertEqual(processor.df.iloc[0]['abbrev'], "CA")
        self.assertEqual(processor.df.iloc[0]['name'], "Cali")



if __name__ == '__main__':
    unittest.main()