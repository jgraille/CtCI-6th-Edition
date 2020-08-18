import difflib
import re
import unittest

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
  print(dic)
  if abs(dic['-'] - dic['+']) > 1 or (dic['-'] == dic['+'] and dic['-'] > 1) or (abs(dic['-'] - dic['+']) == 1 and dic['-'] != 0 and dic['+'] != 0):
    return False
  else:
    return True

# https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/Chapter1/5_One%20Away/OneAway.py
class Test(unittest.TestCase):
    '''Test Cases'''
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
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = OneAway(test_s1, test_s2)
            self.assertEqual(actual, expected)
def main():
  print(OneAway('pale', 'pkle'))
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