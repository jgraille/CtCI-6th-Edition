class Node:

  def __init__(self,value,following):
    self.value = value
    self.following = following

def display(l):
  print(l.value)
  while l.following is not None:
    l.value = l.following.value
    print(l.value)
    l.following = l.following.following
  
def size(l):
  size = 1
  while l.following is not None:
    size += 1
    l.following = l.following.following
  return size 

def kthtolast(l, k):
  si = size(l)
  i = 0
  head1 = l.value
  head2 - l.following.value
  print(head1)
  print(head2)

def main():
  linkedlist = Node(3,(Node(2,Node(1,Node(9,None)))))
  kthtolast(linkedlist,5)

if __name__ == '__main__':
  main()
