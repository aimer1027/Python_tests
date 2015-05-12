from hashlib import sha1   # sha1() method 
from random  import randint # randint method

# here we define a method with name of get_node_id
# it will return a sha1 data with length = 20bytes = 8*20 = 160 bits
# it's namespace length = 20bytes = 160 bits  ,which means we could 
# get a unique node id from 2^160 ids 

def get_node_id():
    hash = sha1()
  # print hash just for test
  # print ( hash)
    s    = ""
    
    # we try to get a string with length of 20 bytes
    # and each byte in string is a random integer varied from 0 to 255
    for i in range(20):
        s += chr(randint(0,255))
   
    hash.update(s)     # insert s string into hash dict

  # print hash just for test
  # print ( hash )
  # print ( s ) 
    
   #return hash's binary value 
    return hash.digest ()

# test method 
print ( get_node_id())
