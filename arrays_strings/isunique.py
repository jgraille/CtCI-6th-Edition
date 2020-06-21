import random
import string
import datetime

def isunique_1(s):
    # O(n^2)
    i = 0
    duplicated = False
    while i < len(s):
        j = i + 1
        while j < len(s):
            if s[i] == s[j]:
                duplicated = True
            j+=1
        if duplicated:
            return False
        else:
            i+=1
    return True

def isunique_2(s):
    # O(n)
    dic = {}
    for i in s:
        if i in dic:
            return False
        else:
            dic[i] = 1
    return True

def isunique_3(s):
    # O(n)
    l = []
    for i in s:
        if i in l:
            return False
        else:
            l.append(i)
    return True

def isunique_4(string):
    # O(n)
    # https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/1_Is%20Unique/IsUnique.py
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

class Gen:

    def __init__(self):
        self.size = random.randint(0,15)
        self.string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(self.size))


class UniqueTest:

    def __init__(self):
        random.seed(10)
        self.strings = [Gen().string for i in range(10)]
    
    def test_isunique1(self):
        start = datetime.datetime.now()
        res = []
        print(self.strings)
        for i in self.strings:
            res.append(isunique_1(i))
        print(res)
        time = datetime.datetime.now() - start
        print(time)
    
    def test_isunique2(self):
        start = datetime.datetime.now()
        res = []
        print(self.strings)
        for i in self.strings:
            res.append(isunique_2(i))
        print(res)
        time = datetime.datetime.now() - start
        print(time)

    def test_isunique3(self):
        start = datetime.datetime.now()
        res = []
        print(self.strings)
        for i in self.strings:
            res.append(isunique_3(i))
        print(res)
        time = datetime.datetime.now() - start
        print(time)

    def test_isunique4(self):
        start = datetime.datetime.now()
        res = []
        print(self.strings)
        for i in self.strings:
            res.append(isunique_4(i))
        print(res)
        time = datetime.datetime.now() - start
        print(time)
          

def main():
    UniqueTest().test_isunique1()
    UniqueTest().test_isunique2()
    UniqueTest().test_isunique3()
    UniqueTest().test_isunique4()
    

if __name__ == "__main__":
    main()