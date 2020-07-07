

def palindrome(s):
  dic = {}
  i = 0
  for i in s:
    if i in dic:
      dic[i] = dic[i] + 1
    else:
      dic[i] = 1
  count = {'odd': 0 }
  for key,value in dic.items():
    if value % 2 == 1:
      count['odd'] += 1
  if count['odd'] == 1:
    print('palindrome')
  else:
    print('not a palindrome') 

def main():
  s = "tactcoa"
  palindrome(s)
  palindrome("tortue")

if __name__ == '__main__':
  main()