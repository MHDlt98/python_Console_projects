text = input("Enter Your Text: \n").title()
for i in ['.' , '?' , '/' , '!' , '<' , '>' , ','] : text = text.replace(i," ")
words_list , counter = list(filter(lambda x : x !="", text.split(" ") )) , dict()
for i in set(words_list) : counter[i] = words_list.count(i)
for i in counter : print(f" {i} : {counter[i]} ")
print("\n Most Repeeted Words : ",list(filter(lambda x : max(counter.values()) in x , counter.items())))