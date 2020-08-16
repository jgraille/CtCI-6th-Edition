"""
Iterator objects are used to abstract a container of data to make it behave like an interable object.
"""

def eval(string1,string2):
    return sum(1 for i,j in zip(string1,string2) if (i==j))

def main():
    target = "Chocolat"
    print(len(target))
    print(eval(target,"Ch3tl"))

if __name__ == '__main__':
    main()



