

dict={"name":"python","english":33,"math":35}


def traverse():
	# print "xxx for in "
	# for i in dict:
	# 	print "dict[%s] = "%i,dict[i]

	# print "###items"
	# for (k,v) in dict.items():
	# 	print "dict[%s] = "%k,v

	print "###iteritems"
	for k,v  in dict.iteritems():
		print "dict[%s] = "%k,v

if __name__ == '__main__':
	traverse()

