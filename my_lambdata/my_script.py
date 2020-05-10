
#my_script.py

from pandas import DataFrame
#from my_mod import enlarge #this works but...
from my_lambdata.my_mod import enlarge #this is the more reliable way to import
## especially with the __init__.py file



print("HELLO")

df = DataFrame({"a": [1,2,3], "b":[4,5,6]})
print(df.head())

x = 11
print(enlarge(x))