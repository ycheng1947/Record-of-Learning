import random
'''
generate random data in dict ,and write into file 
'''

def  generate(file):
	result = open(file,'w+')

	idMap = dict()
	for i in range(100):
		idMap[i]=random.randrange(10,100,2)
		# print "%d,"%i,idMap[i]
	# return idMap

	for k,v in idMap.iteritems():
		print k,v
		line = str(k)+','+str(v)
		result.write(line+'\n')

if __name__ == '__main__':
	generate('D:\\code\\Record-of-Learning\\pythonCode\\dictFile.txt')
