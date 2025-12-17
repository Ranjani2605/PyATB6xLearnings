
print(hash(40))

print(hash(16.5))

# hash will not suuport list and dic
#print(hash([1,5,3]))
#print(hash({"a" : 1}))

#set
words = ["apple", "bannan", "organge", "Orange", "apple"]
unique_hash = set(hash(word) for word in words)
print(unique_hash)

data1 = (1, 2, 3)
data2 = (4, 5, 6)

if hash(data1) == hash(data2):
    print("Data is the same")

records = [(101, "Alice"), (102, "Bob"), (103, "Alice"), (104, "Bob")]

seen = set()
for record in records:
    h = hash(record)
    if h in seen:
        print(f"Duplicate found: {record}")
    else:
        seen.add(h)
        print(seen)
