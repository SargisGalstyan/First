print("Hello world")
thisDict = {
     'word': 'Econometrics',
    "sentence": 'If the implementation is easy to explain, it may be a good idea.',
    'big_list': ["python", 3, "anaconda", 3.6, "jupyter", 10, "lessons", "many", 99],
    "empty_list": []
}

# exercise 1, 2

if not thisDict['word'].isupper():
    thisDict['word'] ="Applied_"+ thisDict['word'].upper()

# exercise 3

thisDict['sentence'].replace("easy", "hard")


# exercise 4

for i in thisDict['big_list']:
    if type(i) == str:
        print(i[0])



# exercise 5

sum = 0
for i in thisDict['big_list']:
    if type(i) == int:
        sum+= i
sum1 = 0
thisDict['big_list'].remove(thisDict['big_list'][-1])
thisDict['big_list'].append(87)
for item in thisDict['big_list']:
    if type(item) == int:
        sum1+= item
print(sum1)

# exercise 6

thisDict['big_list'][7] = "Bugatti"
thisDict

