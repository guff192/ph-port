import requests
med = requests.get("https://api.pharm-portal.ru/api/grls?perPage=500")
#print(str(med.json()))
json = str(med.json()).encode("ascii", "ignore").decode("ascii")
print(json)


with open("head.json", "w") as head:
	head.write(json)
'''
		for key, value in drug.items():
			if key != 'id':
				head.write(str(key) + ': ' + str(value) + ',')
		head.write('\n')
'''

