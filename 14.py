SIZE = 10
hash_table = [None] * SIZE
def hash_func(key):
    return key % SIZE

def insert(roll, name):
    key = hash_func(roll)
    for i in range(SIZE):
        idx = (key + i) % SIZE
        if hash_table[idx] is None or hash_table[idx][0] == roll:
            hash_table[idx] = (roll, name)
            print(f"Inserted at index {idx}")
            return
    print("Hash Table is full!")
def search(roll):
    key = hash_func(roll)
    for i in range(SIZE):
        idx = (key + i) % SIZE
        if hash_table[idx] is None:
            break
        if hash_table[idx][0] == roll:
            print(f"Found {hash_table[idx][1]} at index {idx}")
            return
    print("Record not found!")
def delete(roll):
    key = hash_func(roll)
    for i in range(SIZE):
        idx = (key + i) % SIZE
        if hash_table[idx] is None:
            break
        if hash_table[idx][0] == roll:
            hash_table[idx] = None
            print(f"Deleted record at index {idx}")
            return
    print("Record not found!")
def display():
    for i, record in enumerate(hash_table):
        print(i, ":", record)

insert(11, "BK")
insert(21, "Random")
insert(35, "HAL")
display()
search(21)
delete(21)
display()
