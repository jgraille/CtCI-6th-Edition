import difflib
import re

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
  if abs(dic['-'] - dic['+']) > 1 or (dic['-'] == dic['+'] and dic['-'] > 1):
    return False
  else:
    return True
def main():
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

if __name__ == '__main__':
  main()