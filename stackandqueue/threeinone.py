
class ThreeStacks:

  def __init__(self,array,x,y,z):
    self.array = array
    self.len_array = len(array)
    self.x = x
    self.y = y
    self.z = z
    self.sizestack = [self.x,self.y,self.z] 

  @property
  def sizestack(self):
    return self._sizestack
  @sizestack.setter
  def sizestack(self):
    if sum([self.x,self.y,self.z]) != self.len_array:
      raise TypeError("Sizes values can't match the initial size")
    self._sizestack = [self.x,self.y,self.z]


def main():
  stacks = ThreeStacks([1,2,3,10,11,12,13],2,3,4)


if __name__ == '__main__':
  main()