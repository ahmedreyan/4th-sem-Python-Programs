def display_hash(hashtable):
    for i in range(len(hashtable)):
         print(i)
         for j in hashtable[i]:
             print("-->")
             print(j)
hashtable=[[]for _ in range(10)]
def hashing(keyvalue):
     return keyvalue%len(hashtable)
def insert(hashtable,keyvalue,value):
     hash_key=hashing(keyvalue)
     hashtable[hash_key].append(value)
insert(hashtable,10,"allahabad")
insert(hashtable,25,"mumbai")
insert(hashtable,20,"mathura")
insert(hashtable,9,"delhi")
insert(hashtable,21,"punjub")
insert(hashtable,21,"noida")
display_hash(hashtable)
