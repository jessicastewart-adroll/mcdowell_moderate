### create and parse tree

def xml_encode(elements, attributes):


mapping = {
	1: 'family',
	2: 'person',
	3: 'firstName',
	4: 'lastName',
	5: 'state'
}

class Element(object):
	def __init__(self, tag, attributes):
		self.tag = tag
		self.attribute = attribute
		self.children = []

class Attribute(object):
	def __init__(self, num, tag, value):
		self.num = num
		self.tag = tag
		self.value = value

lastName = Attribute('lastName', 'McDowell')

root = Element('family', )


elements = '<family lastName="McDowell" state="CA"><person firstName="Gayle">Some Message</person></family>'
