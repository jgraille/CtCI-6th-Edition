class Node:
  def __init__(self,value,following):
    self.value = value
    self.following = following

def deleteMiddleNode(l):
  following = l.following
  l.value = following.value
  l.following = following.following


def main():
  linkedlist1 = Node(1,Node(2,Node(3,Node(4,None))))
  deleteMiddleNode(linkedlist1.following.following)
  print(linkedlist1.value)
  print(linkedlist1.following.value)
  print(linkedlist1.following.following.value)

if __name__ == '__main__':
  main()


