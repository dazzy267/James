#creating a new list
cities = ["new york city",  "mountain veiw", "chicago", "los angeles"]
capitalized_cities = []
for city in cities:
	capitalized_cities.append(city.title())
print(capitalized_cities)
#How to work with factorial (!)
number = 6
current = 1
product = 1
while current <= number:
	product *= current
	current += 1
	print(product)
	
product = 1
number = 6
	
for i in range(1, number + 1):
	product *= i
	print(product)
	
card_deck = [4,11,8,5,13,2,8,10]
hand =[]
while sum(hand) <= 17:
	hand.append(card_deck.pop())
	print(sum(hand))
	
#supoose you want to count by until you reach a final number
start_num = 0  #provide some start number
end_num = 50 #provide some end number that you stop when hit
count_by = 5 #provide some number to count by

#write  a while loop that uses breal_num as the on going number to check against end_,num
result = start_num
while result <= end_num:
	result += count_by
	print(result)

for i in range(5,50,5):
	print(i)
	
#count by check. in addition to the above,what would happen if some9ne gives a start_num that is greater than emd_num.if this is the case, set result to "oops".otherwise,set result to the value of break_num
start_num = 0
end_num = 20
count_by = 4
if start_num > end_num:
	result = "Oops"
else:
	break_num = start_num
	while break_num  > end_num:
		break_num += count_by
		result = break_num
print(result)



#Nearest square. write a while loop that finds the largest square mumber less than an integer limit
limit = 40
num = 1
while (num +1)**2 < 40:
	num +=1
	nearest = num**2
print(nearest)
#from the range of __ iterate 
for i in range(1,7):
	i **= 2
	print(i)
	
num_list = [422,136,524,85,96,719,85,92,10,17,312,542,87,23,86,191,116,35,173,45,149,59,84,69,113,166]
count_num = 0
list_sum = 0
i = 0
len_num_list = len(num_list)
while  (count_num<5)and (i < len_num_list):
	if num_list[i] % 2 != 0:
		list_sum += num_list[i]
		count_num += 1
	i += 1
print(i,list_sum,count_num)

#using break and continue
manifest = [('banana', 15), ('matresses', 24),('dog kennels',42), ('machine', 120),('cheeses',5)]
weight = 0
item = []
for cargo in manifest:
	if weight < 100:
		item.append(cargo[0])
		weight += cargo[1]
	else:
		break
print(weight)
print(item)

fruits = ["orange", "strawberry",  "apple"]
foods = ["apple", "apple", "humus",  "toast"]
fruit_count = 0
for food in foods:
	if food not in fruits:
		print('not a fruit')
		continue
	else:
	   fruit_count += 1
	   print("found a fruit")
		
print("Total fruit: ", fruit_count)

weight = 0
item = []
print(manifest)
for cargo in manifest:
	if weight > 100:
		break
	elif weight + cargo[1] > 100:
		continue
	else:
		item.append(cargo[0])
		weight += cargo[1]

print(item)
print(weight)

#break the string
headlines = ["Local Bear Eaten by Man", "Legislature Announce New Laws", "Peasant Discovers Violence Inherent in System", "Cat Rescues Fireman Stuck in Tree", "Brave Knight Runs Away", "Papperbok Review: Totally Triffic"]


print(int(5.7))
news_tickers = ""
for headline in headlines:
		 news_tickers += headline + " "
		 if len(news_tickers) >= 140:
		 	news_tickers = news_tickers[:140]
		 	break
print(news_tickers)
	
check_prime = [26,39,51,53,57,79,86]
for num in check_prime:
		for i in range(2,num):
			if (num % i) == 0:
				print('{} is not a prime number, because {} is a factor of {}'.format(num,i,num))
				break
			if i == num -1:
				print('{} is a prime number'.format(num))
print('\n METHOD 2')
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
	print('current weight: {}'.format(weight))
	if weight >= 100:
		break
	elif weight + cargo_weight > 100:
		print(" skipping {} ({})".format(cargo_name, cargo_weight))
		continue
	else:
		print(" adding {}  ({})".format(cargo_name, cargo_weight))
		items.append(cargo_name)
		weight += cargo_weight
print('\nFinal weight : {}'.format(weight))
print("final Items:  {}".format(items))

print(cities)

x_coord = [23,53,2,-12,95,103,14,-5]
y