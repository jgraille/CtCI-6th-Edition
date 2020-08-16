
class Node():
  """
  Credits: w-hat ctci-solutions/ch-02-linked-lists/01-remove-duplicates.py
  """

  def __init__(self, data, following):
    self.data = data
    self.following = following


def display(l):
  print(l.data)
  while l.following is not None:
    l.data = l.following.data
    print(l.data)
    l.following = l.following.following


def removedups(mylinkedlist):
  l = mylinkedlist
  ll = [l.data]
  while l.following is not None:
    if l.following.data in ll:
      if l.following.following is not None:
        l.following = l.following.following
      else:
        l.following = None
    else:
      ll.append(l.following.data)
      l = l.following
  return l


def main():
  mylinkedlist = Node(1,Node(2,Node(2,Node(4,None))))
  print(type(mylinkedlist.following))
  #display(mylinkedlist)
  res = removedups(mylinkedlist)
  display(res)

if __name__=='__main__':
  main()



