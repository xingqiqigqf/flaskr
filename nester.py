def print_for(each_list):
	for arr in each_list:
		if isinstance(arr,list):
			print_for(arr)
		else:
			print(arr)