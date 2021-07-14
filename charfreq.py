def characters(string):
	dict={}
	for x in string:
		keys=dict.keys()
		if x in keys:
			dict[x]+=1
		else:
			dict[x]=1
		return dict
print(characters("mashupstack"))

