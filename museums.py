import requests, json

#r = requests.get("https://api.yelp.com/v3/businesses/search?location=10118", headers={'Authorization': 'Bearer wqKhAUDTo6BP_rEQ-E0HKR4To7lOm_b6oMC3S7BJfnI5gnyAgNPF4a5OGEw8OLe_1w1nA58qPVWwxazNiECvGsoFJGUqVcjqZQRvxQVNj9_LCOreKs6pxJdR_7CrXHYx'})

r = requests.get("https://api.yelp.com/v3/businesses/search?&location=New York&categories=museums", headers={'Authorization': 'Bearer wqKhAUDTo6BP_rEQ-E0HKR4To7lOm_b6oMC3S7BJfnI5gnyAgNPF4a5OGEw8OLe_1w1nA58qPVWwxazNiECvGsoFJGUqVcjqZQRvxQVNj9_LCOreKs6pxJdR_7CrXHYx'})
#r = requests.get("https://api.yelp.com/v3/businesses/search?offset=20&location=New York&categories=izakaya", headers={'Authorization': 'Bearer wqKhAUDTo6BP_rEQ-E0HKR4To7lOm_b6oMC3S7BJfnI5gnyAgNPF4a5OGEw8OLe_1w1nA58qPVWwxazNiECvGsoFJGUqVcjqZQRvxQVNj9_LCOreKs6pxJdR_7CrXHYx'})

# after professor's help, i was able to edit a header and add criterias like using "?location=10118
# wqKhAUDTo6BP_rEQ-E0HKR4To7lOm_b6oMC3S7BJfnI5gnyAgNPF4a5OGEw8OLe_1w1nA58qPVWwxazNiECvGsoFJGUqVcjqZQRvxQVNj9_LCOreKs6pxJdR_7CrXHYx
print(r.status_code)

#print(r.text)

# decoding json using json.loads
data = json.loads(r.text)
#print(data)

#from google I learnt use pprint to pretty print dictionaries
from pprint import pprint

#pprint(data)

pprint(data["businesses"])

names=[]
coordinates=[]
n = 0
for i in data["businesses"]:
	print(i["coordinates"])
	i['latitude']=i['coordinates']['latitude']
	i['longitude']=i['coordinates']['longitude']


	n=n+1
	print("\n## This is Museums No. " + str(n) +" #########") 
	#pprint(i["name"])
	#pprint(i["price"])
	if i["rating"] > 4.0: #and i["price"] == "$$":
		print(i["name"])
		#print(i["price"])
		print(i["rating"])
		print(i["coordinates"])
		names.append(i["name"])
		coordinates.append(i["coordinates"])

		print("Here is the detail:")
		#pprint(i)
	else:
		print("Parks '"+i["name"]+"' is not qualified\n")

	
print(names)
#print(coordinates)

#####??????#####quetion no.1: how do i create a dictionary with names and coordinates
#####sounds like building a dataset

import csv

mylist=data["businesses"]
           
fields=[]

#write into a csv file in an "a" mode
with open('yelpdatamuseums.csv', 'a') as csvFile:
	
	#for mydic in mylist:
		#for key, value in mydic.items():
			#print(key, value)
			#fields.append(key)
	#print(fields)	
	fields=['url', 'id', 'review_count','price', 'phone', 'rating', 'coordinates', 'image_url', 'transactions', 'categories', 'location', 'display_phone', 'distance', 'alias', 'is_closed', 'name','latitude','longitude']
	writer = csv.DictWriter(csvFile, fieldnames=fields)
	writer.writeheader()
	writer.writerows(mylist)


csvFile.close()






#print(json.dumps(data), sort_keys=True, indent=4))




# I want to be like a real new yorker
# what does alias mean: another name
# with the help of google, I know that separate the queries with "&"


# pretty printing

