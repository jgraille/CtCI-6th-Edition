
class ThreeStacks:

  def __init__(self,array,x,y,z):
    self.array = array
    self.len_array = len(array)
    self.sizestack = [x,y,z] 

  @property
  def sizestack(self):
    return self._sizestack
  @sizestack.setter
  def sizestack(self,sizestack):
    if sum(sizestack) != self.len_array:
      raise TypeError("Sizes values can't match the initial size")
    self._sizestack = sizestack


def main():
  stacks = ThreeStacks([1,2,3,10,11,12,13],2,1,4)


if __name__ == '__main__':
  main()