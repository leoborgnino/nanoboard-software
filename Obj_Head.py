# Head of all the objects of the software.

class Obj_Head(object):

	def __init__(self,com,method):
	        self.__uid 	= 0
        	self.__txfifo   = 0
		self.set_uid(com.reg(method))
		self.set_txfifo(com.txfifo)
	
	def set_uid(self,uid):
		self.__uid = uid

	def set_txfifo(self,txfifo):
		self.__txfifo = txfifo
	
	def send(self,datos):
		self.__txfifo(datos,self.__uid)
		
