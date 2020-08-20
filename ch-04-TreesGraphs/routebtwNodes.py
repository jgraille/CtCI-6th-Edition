class Node:
  def __init__(self,n,adjacent=None):
    self.n = n
    self.adjacent = adjacent

class Queue:
  def __init__(self,listQueue=None):
    self.listQueue = listQueue
  def addElement(self,val):
    self.listQueue.append(val)
    return self.listQueue
  def removeElement(self):
    if self.listQueue:
      self.listQueue.pop(0)
    return self.listQueue

    

                                                                                                                                                    
def main():
  G = { "a" : ["d"],
        "b" : ["c"],
        "c" : ["b", "c", "d", "e"],
        "d" : ["a", "c"],
        "e" : ["c"],
        "f" : []
      }
  g = { "F" : ["I"],
        "B" : ["J"],
        "G" : ["D","H"],
        "C" : ["G"],
        "A" : ["B","C","D"],
        "E" : ["F","A"],
        "D" : ["A"]
        }
queue = Queue([])
queue.removeElement()
queue.addElement(4)
print(queue.listQueue)

if __name__ == '__main__':
  main()