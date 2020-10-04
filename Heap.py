class Heap:
	def __init__(self):
		self.size = 0
		self.heap = []
	
	def insert(self, edge):
		self.heap.append(edge)
		self.size += 1
		k = len(self.heap) - 1
		while(k > 0):
			p = (k-1)//2
			current = self.heap[k]
			parent = self.heap[p]

			if (current.f < parent.f):
				self.heap[p] = current
				self.heap[k] = parent
				k = p
			else:
				break
	
	def delete(self):
		if (len(self.heap) == 0):
			return -1
		if (len(self.heap) == 1):
			self.size = self.size-1
			return self.heap.pop()

		hold = self.heap[0]
		self.heap[0] = self.heap.pop()
		k = 0
		l = 2*k+1
		while (l < len(self.heap)):
			min = l
			r = l + 1
			if (r < len(self.heap)):
				if (self.heap[r].f < self.heap[l].f):
					min += 1 
			if (self.heap[k].f > self.heap[min].f):
				temp = self.heap[k]
				self.heap[k] = self.heap[min]
				self.heap[min] = temp
				k = min
				l = 2*k+1
			else:
				break
		self.size-=1
		return hold

	def printHeap(self):
		print("[ ", end = "")

		for i in range(len(self.heap)):
			print(self.heap[i].f, self.heap[i].vnum, "", end = "")
		
		print("]")

