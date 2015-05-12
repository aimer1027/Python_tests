from hashlib import sha1   # sha1() method 
from random  import randint # randint method

import logging

# here we test our logger 
from myLogger import InitLogger

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
  # here is the test of myLogger.py 
   
    log_file_name = 'node_id.log' 
    
    mylogger = logging.getLogger(log_file_name)
    mylogger = InitLogger(log_file_name , mylogger)    
  
    mylogger.info('node id :'+hash.digest())


  # return hash's binary value 
    return hash.digest ()

# test method 
get_node_id()
