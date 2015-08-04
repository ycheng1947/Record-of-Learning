def repeat(s,exclaim):
	print ('aaa')
	result = s+s+s
	if exclaim:
		result = result+'!!!'
	return result
# def main():
if __name__ == "__main__":
	print repeat('Year',True)
	print repeat('Oh',False)
	print ('aaa')