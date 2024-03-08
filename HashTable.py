# Class containing the Hash Table to be used in Main.py
class HashTable:
    def __init__(self, initial_capacity=40):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Referenced code from C950 Webinar 1 - W-1_ChainingHashTable_zyBooks_Key-Value.py
    # Method that updates items or inserts them into the Table
    def insert(self, key, item):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Updates the key if it already exists in the bucket
        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                kv_pair[1] = item
                return True
        # Inserts the item at the end of the bucket list if not found
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Method that searches for items in the Table
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv_pair in bucket_list:
            if kv_pair[0] == key:
                return kv_pair[1]
        return None

    # Method that deletes an item from the Table
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # Removes the item from the bucket list if it exists
        if key in bucket_list:
            bucket_list.remove(key)
