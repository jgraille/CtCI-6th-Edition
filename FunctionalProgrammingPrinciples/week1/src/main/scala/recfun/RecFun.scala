package recfun

import scala.collection.mutable.ArrayBuffer
import java.lang.Math.floorMod

object RecFun extends RecFunInterface {

  def main(args: Array[String]): Unit = {
    /*
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(s"${pascal(col, row)} ")
    }
    val res = balance("toto".toList)
    println(res)
    */
    println(changer1(4,List(1,2),0))
    println(changer1(300,List(5,10,20,50,100,200,500),0))
  }

  /**
   * Exercise 1
   */
  def pascal(c: Int, r: Int): Int = {
    if (c == 0 || c == r) 1
    else {
      pascal(c-1,r-1) + pascal(c,r-1)
    }
  }

  /**
   * Exercise 2
   */
  def balance(chars: List[Char]): Boolean = {
    def check(chars: List[Char], c: Int): Boolean = {
      if (chars.isEmpty) {
        true
      } else {
        if (chars.head == '(') {
          check(chars.tail,c+1)
        } else {
          if (chars.head == ')') {
            c>0 && check(chars.tail,c-1)
          } else {
            check(chars.tail,c)
          }
        }
      }
    }
    check(chars,0)
  }
  /**
   * Exercise 3
   */
  def changer(money: Int, coins: List[Int], c: Int): Int = {
    if (!coins.isEmpty) {
      if (floorMod(money,coins.head) == 0) {
        changer(money,coins.tail,c+1)
      } else {
        if (coins.contains(floorMod(money,coins.head + coins.tail.head)) && !coins.tail.isEmpty) {
          changer(money,coins,c+1)
        }
        if (floorMod(money,floorMod(money,coins.head) + coins.head) == 0) {
          changer(money,coins.tail,c+1)
        } else {
          if (coins.contains(floorMod(money,floorMod(money,coins.head) + coins.head))) {
            changer(money,coins.tail,c+1)
          } else {
            changer(money,coins.tail,c)
          }
        }
        changer(money,coins.tail,c)
      }
    } else {
      c
    }
  }
  def changer1(money: Int, coins: List[Int], c: Int): Int = {
    if (coins.isEmpty || money <= 0) {
      c
    } else {
      if (money < coins.head) { 
        changer1(money,coins.tail,c)
      } else if (floorMod(money,coins.head) == 0) {
        if (!coins.tail.isEmpty){
          if (coins.contains(floorMod(money,coins.head + coins.tail.head))) {
            changer1(money,coins.tail,c+2)
          } else {
            changer1(money,coins.tail,c+1)
          }
        } else {
          c + 1
        }
      } else if (floorMod(money,floorMod(money,coins.head) + coins.head) == 0) {
        changer1(money,coins.tail,c+1)
      }
      else if (coins.contains(floorMod(money,floorMod(money,coins.head) + coins.head))) {
        changer1(money,coins.tail,c+1)
      } else {
        changer1(money,coins.tail,c)
      }
    }
  }

  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0) {
      0
    } else {
      if (coins.isEmpty) {
        0
      } else {
        changer(money,coins,0)
      }
    }
    
  }
}

