class SQueue(object):
	def __init__(self, init_len=8):
		self.__elem = [0] * init_len
		self.__len = init_len
		self.__head = 0
		self.__num = 0
	def __extend(self):
		old_len = self.__len
		self.__len *= 2
		new_elems = [0] * self.__len
		for i in range(old_len):
			new_elems[i] = self.__elem[(self.__head + i) % old_len]
		self.__elem, self.__head = new_elems, 0
	def is_empty(self):
		return self.__num == 0
	def peek(self):
		if self.__num == 0:
			raise ValueError
		return self.__elem[self.__head]
	def enqueue(self, e):
		if self.__num == self.__len:
			self.__extend()
		self.__elem[(self.__head + self.__num) % self.__len] = e
		self.__num += 1
	def dequeue(self):
		if self.__num == 0:
			raise ValueError
		e = self.__elem[self.__head]
		self.__head = (self.__head + 1) % self.__len
		self.__num -= 1
		return e
    
n = int(input())
A = SQueue()
B = SQueue()
C = SQueue()
for i in range(n):
    new=input().split()
    new_num = new[0]
    new_class = new[1]
    if new_class=='A':
        A.enqueue(new_num)
    elif new_class=='B':
        B.enqueue(new_num)
    elif new_class=='C':
        C.enqueue(new_num)

while not A.is_empty():
    print(A.dequeue())
while not B.is_empty():
    print(B.dequeue())
while not C.is_empty():
    print(C.dequeue())    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    