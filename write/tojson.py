import json
from datetime import datetime
import os
 
Dictionary ={(1, 2, 3):'Welcome', 2:'to',
            3:'Geeks', 4:'for',
            5:'Geeks'}
 
 
# Our dictionary contains tuple
# as key, so it is automatically
# skipped If we have not set
# skipkeys = True then the code
# throws the error
json_string = json.dumps(Dictionary, skipkeys = True)
curr_timestamp = int(datetime.timestamp(datetime.now())) 
f = open(f'./_{curr_timestamp}.json', "x")
f.write(json_string)
