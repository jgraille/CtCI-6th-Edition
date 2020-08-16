
class ThreeStacks:

  def __init__(self,array,x,y,z):
    self.array = array
    self.sizestack = [x,y,z]
    self.one = self.create(0,self.sizestack[0])
    self.two = self.create(self.sizestack[0], self.sizestack[1])
    self.three = self.create(self.sizestack[0] + self.sizestack[1],self.sizestack[2])

  @property
  def sizestack(self):
    return self._sizestack
  @sizestack.setter
  def sizestack(self,sizestack):
    if sum(sizestack) != len(self.array):
      raise TypeError("Sizes values can't match the initial size")
    self._sizestack = sizestack

  def create(self,start,stop):
    l = []
    for x in range(start,start + stop,1):
      l.append(self.array[x])
    return l
  
  def Pop(self):
    if self.three:
      self.three.pop()
      return self.three
    else:
      None

class ThreeStackss():
  def __init__(self):
    self.array = [None, None, None]
    self.current = [0, 1, 2]
  
  def push(self, item, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    #print(len(self.array)) 3
    print(item)
    while len(self.array) <= self.current[stack_number]:
      self.array += [None] * len(self.array)
    self.array[self.current[stack_number]] = item
    self.current[stack_number] += 3
    print('increm+3:',self.current[stack_number])
  
  def pop(self, stack_number):
    if not stack_number in [0, 1, 2]:
      raise Exception("Bad stack number")
    if self.current[stack_number] > 3:
      self.current[stack_number] -= 3
    item = self.array[self.current[stack_number]]
    self.array[self.current[stack_number]] = None
    return item

  

def main():
  stacks = ThreeStacks([1,2,3,10,11,12,13],2,1,4)
  print(stacks.one)
  print(stacks.two)
  print(stacks.three)
  other = ThreeStackss()
  other.push(1,0)
  other.push(2,1)
  other.push(6,0)
  other.push(4,0)
  other.push(3,1)





if __name__ == '__main__':
  main()