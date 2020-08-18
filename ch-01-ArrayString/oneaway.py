import difflib
import re
import unittest
import datetime
import random
import string

random.seed(9001)

def one_edit_replace(s1, s2):
  edited = False
  for c1, c2 in zip(s1, s2):
      if c1 != c2:
          if edited:
              return False
          edited = True
  return True 

def one_edit_insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            if edited:
                return False
            edited = True
            j += 1
        else:
            i += 1
            j += 1
    return True

def one_away(s1, s2):
  if len(s1) == len(s2):
      return one_edit_replace(s1, s2)
  elif len(s1) + 1 == len(s2):
      return one_edit_insert(s1, s2)
  elif len(s1) - 1 == len(s2):
      return one_edit_insert(s2, s1)
  return False


def find(val):
  res = re.search(r"(-|\+)", val)
  if res != None:
    return res.group(0)
  else:
    return None

def OneAway(string1,string2):
  d = difflib.Differ()
  resMatch = list(filter(lambda x: x != None, list(map(find,list(d.compare(string1,string2))))))
  dic = {'-':resMatch.count('-'), '+':resMatch.count('+')}
  if abs(dic['-'] - dic['+']) > 1 or (dic['-'] == dic['+'] and dic['-'] > 1) or (abs(dic['-'] - dic['+']) == 1 and dic['-'] != 0 and dic['+'] != 0):
    return False
  else:
    return True

class Gen:
    def __init__(self):
        self.size = random.randint(50,100)
        self.string = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(self.size))

# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py
class Test(unittest.TestCase):
    '''Test Cases'''
    a = Gen().string
    b = Gen().string
    print(a)
    print(b)
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False),
        (a,b,False),
    ]

    def test_one_away1(self):
      start = datetime.datetime.now()
      for [test_s1, test_s2, expected] in self.data:
        actual = one_away(test_s1, test_s2)
        self.assertEqual(actual, expected)
      time = datetime.datetime.now() - start
      print(time)

    def test_one_away2(self):
      start = datetime.datetime.now()
      for [test_s1, test_s2, expected] in self.data:
        actual = OneAway(test_s1, test_s2)
        self.assertEqual(actual, expected)
      time = datetime.datetime.now() - start
      print(time)
      
def main():
  unittest.main()
  '''
  a = 'doretdeplatine'
  # remove case
  deletionOne = 'doretdeplatin'
  deletionSeveral = 'doretdeplati' 
  # insert case 
  insertOne = 'doretdeplatine1'
  insertSeveral = 'doreetdeplatine12'
  # repalce case
  replaceOne = 'boretdeplatine'
  replaceSeveral = 'boretdeplat1ne'
  print(a,deletionOne,'->',OneAway(a,deletionOne))
  print(a,deletionSeveral,'->',OneAway(a,deletionSeveral))
  print(a,insertOne,'->',OneAway(a,insertOne))
  print(a,insertSeveral,'->',OneAway(a,insertSeveral))
  print(a,replaceOne,'->',OneAway(a,replaceOne))
  print(a,replaceSeveral,'->',OneAway(a,replaceSeveral))
  print(a,a,'->',OneAway(a,a))
  '''

if __name__ == '__main__':
  main()