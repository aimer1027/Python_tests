from 	threading import Thread

import 	logging  
from 	logging   	      import handlers
from 	logging.handlers import RotatingFileHandler
from 	logging 	      import Formatter

from 	time 	      import sleep
import 	time


LOG_LEVEL = {
'default'  	:logging.DEBUG,
'debug'		:logging.DEBUG,
'info'		:logging.INFO,
'warning'	:logging.WARNING,
'error'		:logging.ERROR,
'critical'	:logging.CRITICAL  }

LOG_FILENAME	   = ''
LOG_BACKUP_COUNTER = 3
LOG_TYPE           = 'default'
LOG_MAX_SIZE  = 1024*1024*4 # bits = 0.5MB each log file


def InitLogger(log_file_name, logger):
    str_time 	 =  time.strftime("%Y%m%d_%H%M%S")
    LOG_FILENAME =  str_time+'_'+log_file_name
    #print(LOG_FILENAME)
    
    handler = RotatingFileHandler( LOG_FILENAME,maxBytes = LOG_MAX_SIZE, backupCount = LOG_BACKUP_COUNTER)
   
    # method indefault 
    # handler = FileHandler( LOG_FILENAME)
  
    # set log file output message format 
    fmt = '[ %(asctime)s ]--[ %(filename)s:%(lineno)s ]--[%(name)s]--[%(levelname)s]--[ %(message)s ]'
 
    formatter = Formatter (fmt)
   
    handler.setFormatter( formatter )
  
    logger.addHandler(handler)
   
    logger.setLevel(LOG_LEVEL.get(LOG_TYPE.lower()))

    
    # after set every parameters , return logger 
    return logger


#define a thread writer class
class log_writter(Thread):
      def __init__(self,threadName,file_name):
	  
	  self.log_file_name = file_name

	  Thread.__init__(self,name = threadName)
	  
	  logger = logging.getLogger(self.log_file_name)
	
	  self.logger = InitLogger(self.log_file_name,logger)
	  
	  
    
      def run(self):
	  
	  global i

	  self.logger.info(self.log_file_name)
 
	  while i in range(10):
		print '**** log writer '+self.log_file_name+' test ******'
		
		self.logger.info   ('hello aimer')
		
		self.logger.debug  ('hello kokia')
	
		self.logger.warning ('hello kylin-zhang')
	
		i  += 1

		time.sleep (3)
		
	  print('end of log file test '+ self.log_file_name )
          



i = 0

threadCounter = 1024

for  j in range(threadCounter):

   # s is used for thread and log file no.
   s = 'thread'
   s +='_'+str(j) 
   
   print ( s )
   
   log_file = str(j)+'_mylog.log'
   my_logger = log_writter( s , log_file) 
   my_logger.start () 


