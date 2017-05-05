END = 0

class Attribute(object):
	def __init__(self, attribute, value):
		self.attribute = attribute
		self.value = value

class Element(object):
	def __init__(self, tag, message=None):
		self.tag = tag
		self.message = message
		self.attributes = []

def get_xml_encoding(elements):	
	mapping = {}
	i = 1
	for e in elements:
		mapping[e.tag] = i
		i += 1
	elements.reverse()
	for e in elements:
		for a in e.attributes:
			mapping[a.attribute] = i
			i += 1
	print(mapping)

	elements.reverse()
	encoding = []
	for e in elements:
		encoding.append(mapping[e.tag])
		for a in e.attributes:
			encoding.append(mapping[a.attribute])
			encoding.append(a.value)
		encoding.append(END)
		if e.message:
			encoding.append(e.message)
			encoding.append(END)
	return encoding

last_name = Attribute('lastName', 'McDowell')
state = Attribute('state', 'CA')
first_name = Attribute('firstName', 'Gayle')

family = Element('family')
family.attributes.append(last_name)
family.attributes.append(state)
person = Element('person', 'Some Message')
person.attributes.append(first_name)
elements = [family, person]
print(get_xml_encoding(elements))

# '<family lastName="McDowell" state="CA">\n<person firstName="Gayle">Some Message</person>\n</family>'
# 1 4 McDowell 5 CA 0 2 3 Gayle 0 Some Message 0 

# mapping = {
# 	'family': 1,
# 	'person': 2,
# 	'firstName': 3,
# 	'lastName': 4,
# 	'state': 5
# }
