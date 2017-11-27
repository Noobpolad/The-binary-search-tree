class theBinarySearchThree:

	def __init__(self,value):
		self.setValue(value)
		self.setParent(None) 
		self.setLeft(None)
		self.setRight(None)

	def getLeft(self):
		return self._left

	def setLeft(self,value):
		self._left = value		

	def getRight(self):
		return self._right
			
	def setRight(self,value):
		self._right = value
	
	def getParent(self):
		return self._parent

	def setParent(self,value):
		 self._parent = value	

	def setValue(self,value):
		self._v = int(value)	

	def getValue(self):
		return self._v		
 
class operationsWithBST:

	def __init__(self):
		self._root = None

	def insert(self,value):
		if self._root != None:
			cur = theBinarySearchThree(value)
			new = self._root
			while 1:
				if cur.getValue() > new.getValue() and new.getRight() == None:
					new.setRight(cur)
					cur.setParent(new)
					break
				elif cur.getValue() > new.getValue() and new.getRight() != None:
					new = new.getRight()	

				if cur.getValue() < new.getValue() and new.getLeft() == None:
					new.setLeft(cur)
					cur.setParent(new)
					break
				elif cur.getValue() < new.getValue() and new.getLeft() != None:
					new = new.getLeft()		
		else:
			self._root = theBinarySearchThree(value)
		
	def search(self,element):
			new = self._root
			found = False
			while new != None:
				if element > new.getValue():
					new = new.getRight()
				elif element < new.getValue():
					new = new.getLeft()	 
				else:
					print("The element " + str(element) + " exists in the tree")
					found = True
					break
			if found == False:
				print("The element doesn't exist in the tree")		

	def delete(self,element):
			new = self._root
			while 1:
				if element > new.getValue():
					new = new.getRight()
				elif element < new.getValue():
					new = new.getLeft()
				else:
					break	

			if element == new.getValue() and element <= self._root.getValue():	
				self.DNFLS(new)
					
			elif element == new.getValue() and element >= self._root.getValue():
				self.DNFRS(new)

	#Delete the node from the left subtree or root

	def DNFLS(self,new):		
		new = self._root
		while 1:
			if new.getRight() != None and new.getLeft() == None:
				new.setValue(new.getRight().getValue())
				if new.getRight().getLeft() != None:
					new.getRight().getLeft().setParent(new)
					new.setLeft(new.getRight().getLeft())

				if new.getRight().getRight() != None:	
					new.getRight().getRight().setParent(new)
					new.setRight(new.getRight().getRight())	
				else:
					new.setRight(None)
				break

			elif new.getLeft() != None and new.getRight() == None:
				new.setValue(new.getLeft().getValue())	
				if new.getLeft().getRight() != None:	
					new.getLeft().getRight().setParent(new)
					new.setRight(new.getLeft().getRight())	

				if new.getLeft().getLeft() != None:
					new.getLeft().getLeft().setParent(new)
					new.setLeft(new.getLeft().getLeft())
				else:
					new.setLeft(None)	
				break

			elif new.getLeft() != None and new.getRight() != None:
				if new.getRight().getLeft() == None:
					new.setValue(new.getRight().getValue())
					if new.getRight().getRight() == None:
						new.setRight(None)
						break
					else:
						new.getRight().getRight().setParent(new)
						new.setRight(new.getRight().getRight())	
						break

				elif new.getRight().getLeft() != None:	
					cur = new.getRight().getLeft()
					while 1:
						if cur.getLeft() != None:
							cur = cur.getLeft()
						elif cur.getLeft() == None and cur.getRight() == None:
							new.setValue(cur.getValue())
							cur.getParent().setLeft(None)
							break	
						elif cur.getLeft() == None and cur.getRight() != None:	
							new.setValue(cur.getValue())
							cur.getRight().setParent(cur.getParent())
							cur.getParent().setLeft(cur.getRight())
							break	
							
			elif new.getLeft() == None and new.getRight() == None and new.getParent().getLeft() == new:
				new.getParent().setLeft(None)
				break

			elif new.getLeft() == None and new.getRight() == None and new.getParent().getRight() == new:	
				new.getParent().setRight(None)
				break

	#Delete the node from the right subthree or root
	def DNFRS(self,new):
		while 1:			
			if new.getRight() != None and new.getLeft() == None:
				new.setValue(new.getRight().getValue())
				if new.getRight().getLeft() != None:
					new.getRight().getLeft().setParent(new)
					new.setLeft(new.getRight().getLeft())	

				if new.getRight().getRight() != None:	
					new.getRight().getRight().setParent(new)
					new.setRight(new.getRight().getRight())	
				else:
					new.setRight(None)
				break

			elif new.getLeft() != None and new.getRight() == None:
				new.setValue(new.getLeft().getValue())	
				if new.getLeft().getRight() != None:	
					new.getLeft().getRight().setParent(new)
					new.setRight(new.getLeft().getRight())
						
				if new.getLeft().getLeft() != None:
					new.getLeft().getLeft().setParent(new)
					new.setLeft(new.getLeft().getLeft())
				else:
					new.setLeft(None)	
				break

			elif new.getLeft() != None and new.getRight() != None:
				if new.getRight().getLeft() == None:
					new.setValue(new.getRight().getValue())
					if new.getRight().getRight() == None:
						new.setRight(None)
						break
					else:
						new.getRight().getRight().setParent(new)
						new.setRight(new.getRight().getRight())	
						break

				elif new.getRight().getLeft() != None:	
					cur = new.getRight().getLeft()
					while 1:
						if cur.getLeft() != None:
							cur = cur.getLeft()
						elif cur.getLeft() == None and cur.getRight() == None:
							new.setValue(cur.getValue())
							cur.getParent().setLeft(None)
							break	
						elif cur.getLeft() == None and cur.getRight() != None:	
							new.setValue(cur.getValue())
							cur.getRight().setParent(cur.getParent())
							cur.getParent().setLeft(cur.getRight())
							break

			if new.getLeft() == None and new.getRight() == None and new.getParent().getLeft() == new:
				new.getParent().setLeft(None)
				break

			elif new.getLeft() == None and new.getRight() == None and new.getParent().getRight() == new:	
				new.getParent().setRight(None)
				break		

	def printInorder(self):	
		self.inorder(self._root)			

	def inorder(self,root):
		if root != None:
			self.inorder(root.getLeft())
			print(root.getValue())
			self.inorder(root.getRight())

	def printPostorder(self):
		self.postorder(self._root)

	def postorder(self,root):
		if root != None:
			self.postorder(root.getLeft())
			self.postorder(root.getRight())	
			print(root.getValue())	

	def printPreorder(self):
		self.preorder(self._root)

	def preorder(self,root):
		if root != None:
			print(root.getValue())
			self.preorder(root.getLeft())
			self.preorder(root.getRight())	