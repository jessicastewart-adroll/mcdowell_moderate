ones_teens = [None, 
'One', 
'Two',
'Three',
'Four',
'Five',
'Six',
'Seven',
'Eight',
'Nine',
'Ten',
'Eleven',
'Twelve',
'Thirteen',
'Fourteen',
'Fifteen',
'Sixteen',
'Seventeen',
'Eightteen',
'Nineteen']

tens = [None,
None,
'Twenty',
'Thirty',
'Fourty',
'Fifty',
'Sixty',
'Seventy',
'Eighty',
'Ninety']


def handle_triple(digit):
	result = []
	if len(digit) == 3:
		if int(digit[0]) != 0:
			if ones_teens[int(digit[0])]:
				result.extend([ones_teens[int(digit[0])], 'Hundred'])
		digit = digit[1:]
	
	if len(digit) == 2:
		if int(digit[0]) == 1:
			if ones_teens[int(digit[0])]:
				result.append(ones_teens[int(digit[:])])
			return result
		else:
			if tens[int(digit[0])]:
				result.append(tens[int(digit[0])])
		digit = digit[1:]

	if digit:
		if ones_teens[int(digit[0])]:
			result.append(ones_teens[int(digit[0])])

	return result

def convert_to_English(integer):
	digits = str(integer)
	result = []

	if len(digits) > 6:
		r = handle_triple(digits[:-6])
		if r:
			result.extend(r)
			result.append('Million')
		digits = digits[-6:]

	if len(digits) > 3:
		r = handle_triple(digits[:-6])
		if r:
			result.extend(r)
			result.append('Thousand')
		digits = digits[-3:]	

	if len(digits) > 1:
		result.extend((handle_triple(digits)))

	print(' '.join(result))

convert_to_English(689070001)
