import unittest

class Node:
  def __init__(self,val,adjacent=None):
    self.val = val
    self.adjacent = adjacent
    self._marked = False
  
  @property
  def marked(self):
    return self._marked

  @marked.setter
  def marked(self,value):
    if isinstance(value,bool):
      self._marked = value
    else:
      raise TypeError("Value is not a boolean")

  def addEdge(self,node):
    self.adjacent += [node]

class Queue:
  def __init__(self,listQueue=None):
    self.listQueue = listQueue
  def addElement(self,val):
    self.listQueue.append(val)
    return self.listQueue
  def removeElement(self):
    if self.listQueue:
      return self.listQueue.pop(0)

def routebtwNodes(start,end):
  if start == end:
    return True
  thequeue = Queue([])
  node_s = start
  node_s.marked = True
  thequeue.addElement(node_s)
  while thequeue.listQueue:
    node_r = thequeue.removeElement()
    if node_r.adjacent != None:
      for r in node_r.adjacent:
        if r.marked == False:
          if r.val == end.val:
            return True
          else:
            thequeue.addElement(r)
          r.marked = True
  return False

def resetMarked(nodes):
  for i in nodes:
    i.marked = False

class Test(unittest.TestCase):
  
  def test_routebtwNodes(self):
    node_c = Node('C')
    node_d = Node('D')
    node_b = Node('B', [node_c])
    node_a = Node('A',[node_d,node_b])
    node_e = Node('E',[node_a])
    node_b.addEdge(node_a)
    nodes = [node_a,node_b,node_c,node_d,node_e]
    testCases = [[node_e,node_e,True],
                 [node_a,node_b,True],
                 [node_b,node_a,True],
                 [node_e,node_c,True],
                 [node_d,node_c,False]
                 ]
    for case in testCases:
      print('(node_' + case[0].val + ',node_' + case[1].val + ')' + ' ' + str(case[2]))
      self.assertEqual(routebtwNodes(case[0],case[1]),case[2])
      resetMarked(nodes)
  

if __name__ == '__main__':
  unittest.main()