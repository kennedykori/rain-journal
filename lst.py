from create import Journal

def view_last():
	if type(Journal.last) is dict:
		for k,v in Journal.last.items():
			print("\tTitle : " + k)
			print("\t\t" + str(v))
	else:
		print(Journal.last)

def list_all():
	for k, v in Journal.journal.items():
		print("Journal : " + k)
		if type(v) is dict and len(v) > 0:
			for k1, v1 in v.items():
				print("\tTitle : " + k1 + "\n")
				if type(v1) is list:
					for index in range(len(v1)):
						print("\t\t" + v1[index])

				else:
					print("\t\t" + str(v1))

