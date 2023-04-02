import random

class HashTable:
    def __init__(self):
        self.bucket_count = 500
        self._multiplier = 1234
        self._prime = random.randint(0,200)
        self.buckets = [[] for _ in range(self.bucket_count)]

    def _hash_func(self, query):
        ans = 0
        for c in reversed(query):
            ans = (ans * self._multiplier + ord(c) % self._prime)
        return ans % self.bucket_count

    def add(self, string, string2):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket[i] = (string, string2)
                return
        bucket.append((string, string2))

    def delete(self, string):
        hashed = self._hash_func(string)
        bucket = self.buckets[hashed]
        for i in range(len(bucket)):
            if bucket[i][0] == string:
                bucket.pop(i)
                break

    def find(self, string):
        hashed = self._hash_func(string)
        for elem in self.buckets[hashed]:
            if elem[0] == string:
                return elem[1]
        return "not found"

if __name__ == '__main__':
        result = []
        n = int(input())
        hash_table = HashTable()  
        for query in range(n):
            query = input().split()
            if query[0] == 'add':
                hash_table.add(query[1], query[2])
            elif query[0] == 'find':
                result.append(hash_table.find(query[1]))
            elif query[0] =='del':
                hash_table.delete(query[1])

        for rez in result:
            print(rez)
