## Functionnal Programming Concepts

This note is providing an overview of those key concepts: 
 - #### Immutability
 - #### Expressions 
 - #### Statements
 - #### Pure/Impure functions
 - #### Referential transparency
 - #### Higher order functions
 
 
 #### Immutability
 Mutating an element means changing its value.
 ```
 x = 1
 x = x + 1
 ```
 This `x` value can be overridden in the computer science field.<br>
 Immutability is not changing the state of a variable once assigned.
 
 #### Expressions
 An expression is yielding a value.
 ```
 def sum(x):
  return x + 10
 sum(1)
 ```
 `sum(1)` is an expression because it yields the value 11.
 
 #### Statements
 A statement is a line of code that is doing an action.
 ```
 print("I love R indeed")
 ```
 
 #### Pure/Impure Functions
 ##### Pure
 A pure function can't be altered by anything.
 ```
 def multiply(x,y):
  return(x*y)
 ```
 This function is pure in terms of result. Of course good type of variables are needed for the input but there are no side effects.
 
 ##### Impure
 An impure function doesn't guarantee the same result for the same given inputs.<br>
 In the exemple below, the user have 30 euros on his account. If he buys a 31 euro product, he will get a transaction error. <br>
 Otherwise, if the user had 40 euros on his account, the transaction would have been available.
 ```
def impure(x):
  val = 30 - x
  if (val > 0):
    return val
  else:
    return "Transaction declined"
  
def main():
  print(impure(31))

if __name__ == "__main__":
  main()
 ```
 
 ##### Referential transparency
 
```
def add(x,y):
  return x + y
def multiply(x,y):
  return x*y
add(2,multiply(1,2))
```
The `add(2,multiply(1,2))` call is using some transparency referential.<br> 
It is a "concatenate" version of two actions (the `add()` and the `multiply()`) which gives the same result.
 
