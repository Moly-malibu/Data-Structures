def remove_tail(self):
	if not self.head:
		return None

	if self.head is self.tail:
		value = self.head.get_value()
		self.head = None
		self.tail = None
		return value

	current = self.head

	while current.get_next() is not self.tail:
		current = current.get_next()

	value = self.tail.get_value()
	self.tail = current
	self.tail.set_next(None)
	return value