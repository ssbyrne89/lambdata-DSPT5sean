### assignment_test.py

import unittest
from pandas import DataFrame

from my_lambdata.assignment import add_state_names

#OBJECTIVE: test the add_state_names() function from the my_lambdate/assignment.py file

class TestAssignment(unittest.TestCase):

    def test_add_state_names(self):
        
        df = DataFrame({"abbrev":["CA","CO","CT","DC","TX"]})
        self.assertEqual(list(df.columns), ['abbrev'])


        result = add_state_names(df)
        self.assertEqual(list(result.columns), ["abbrev", "name"])
    #after we invoke the function:
    # expect that it has one more columna dn same number of rows
    # expect that certain column names exist before and certain column names exist after


        #breakpoint()
    #self.assertEqual("foo".upper(), "FOO") #> True or False
    #df.columns)



if __name__ == '__main__':
    unittest.main()