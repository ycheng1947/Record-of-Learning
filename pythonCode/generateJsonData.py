import random 
def  generate():
	fp = open("D:\\code\\Record-of-Learning\\pythonCode\\test.txt","w")
	for i in range(0,1000):
		a = random.randint(1,10)
		fp.write(str(a)+"\n") 

	fp.close()

if __name__ == '__main__':
	generate()