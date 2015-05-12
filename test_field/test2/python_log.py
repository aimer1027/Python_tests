import threading

import time 

import logging

import logging.handlers

LEVELS={
	'notset':logging.DEBUG,
	'debug':logging.DEBUG,
	'info':logging.INFO,
	'warning':logging.WARNING,
	'error':logging.ERROR,
	'critical':logging.CRITICAL}

LOG_FILENAME = 'test.log'

LOG_BACKUPCOUNT = 5 

LOG_LEVEL = 'notset'

def InitLog(file_name,logger):
    LOG_FILENAME = file_name

    handler = logging.handlers.RotatingFileHandler(LOG_FILENAME,maxBytes=10*1024*1024,backupCount=LOG_BACKUPCOUNT )
    
    #handler = logging.FileHandler(LOG_FILENAME)
    
    #formatter = logging.Formatter ( "[%(asctime)s ][%(levelname) ] %(message)s\n")
	
    formatter = logging.Formatter("[ %(asctime)s ][ %(levelname)s ] %(message)s\n")  
	
    handler.setFormatter(formatter)
  
    #logger = logging.getLogger()
	
  
    logger.addHandler(handler)
	
    logger.setLevel(LEVELS.get(LOG_LEVEL.lower()))  # will get corresponding logging.xxx 
	
    return logger 


class t1(threading.Thread):   # here is how to define a class
    
      def __init__(self,threadName):   # here is how to define a method inside class
	  
	  threading.Thread.__init__(self,name = threadName)


	  logger1 = logging.getLogger("thread.a")
	
	  self.logger = InitLog("thread1.log " ,logger1)

      def run (self):
  	  global i
	
	  self.loggger.info("test1")
	
	  while True:			# here is how to use cycle
		
		print '************** hello t1 *************************'
		
		self.logger.info("****** hello t1 *********** ")
	
		self.logger.debug("t1 debug")
	
		self.logger.warning("t1 warning") 
	
		self.logger.error("t1 error")

		i += 1
		
		print i
	
		if i > 10:
		   
		   break
		
		time.sleep(3)
	
	  self.logger.info("test1 over")
		

class t2(threading.Thread):
    
      def __init__(self,threadName):
	  
	  threading.Thread.__init__(self,name = threadName )
	  
	  logger2 = logging.getLogger("thread.b")
	
	  self.logger = InitLog("thread2.log", logger2)
	
	  print "self.logger = %s" %self.logger
	
	  None 

      def run(self):
	
	  global i
	
	  self.logger.info("test2")
	
	  while True:
	
		print 'hello t2'
	
		self.logger.info("hello t2")
	
		self.logger.debug("t2 debug")
	
		self.logger.warning("t2 warning")
	
		self.logger.error("t2 error")
	
		i += 1
	
		print i
	
		if i > 10:  # if i > 10 
		
		   break
		
		time.sleep(5) # here is why import time
		
	  self.logger.info("test2 over")

i = 0 


p1 = t1('p1')

p1.start()

p2 = t2('p2')

p2.start()









