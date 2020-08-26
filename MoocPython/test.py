import os 
class Counter:
    Count = 0   # This represents the count of objects of this class
    def __init__(self, name):
        self.name = name
        print(name, 'created')
        Counter.Count += 1
    def __del__(self):
        print(self.name, 'deleted')
        Counter.Count -= 1
        if Counter.Count == 0:
            print('Last Counter object deleted')
        else:
            print(Counter.Count, 'Counter objects remaining')



def main():
  x = Counter("First")
  y = Counter("Second")
  del x
  del y
# retrieve all python files 
pythonFiles = [os.path.join(i) for root,dirs,files in os.walk(".") for i in files
              if i.endswith(".py")]
print(pythonFiles)


if __name__ == '__main__':
  main()