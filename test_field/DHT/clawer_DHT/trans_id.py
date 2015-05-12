# method : transfer_id_to_decimal
# this method is used to transfer the node's id (binary) 
#into ordinary decimal number

from hashlib import sha1
from random  import randint

from node_id import get_node_id

def transfer_id_to_dec(nid):
    assert  len(nid) == 20  # node id must be equaled to 20 bytes
 
    #just for test
    #print  ( nid.encode('hex') )
    #print  ( long ( nid.encode('hex'),16)
    
    return  long(nid.encode('hex'),16)


# test method transfer_id_to_dec 
nid = get_node_id()
print ("here we got nid --->" , nid)

dec_id = transfer_id_to_dec(nid)
print ("here we got decimal id ----> " , dec_id)
  



