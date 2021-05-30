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
    println("10, List(2,5)",changer(10,List(1,2,5),0))
    println("4, List(2,4)",changer(4,List(1,2,4),0))
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
        return changer(money,coins.tail,c+1)
      } else {
        val resModulo = floorMod(money,coins.head)
        if (floorMod(money,resModulo + coins.head) == 0) {
          return changer(money,coins.tail,c+1)
        } else {
          if (coins.contains(floorMod(money,resModulo + coins.head))) {
            return changer(money,coins.tail,c+1)
          } else {
            return changer(money,coins.tail,c)
          }
        }
        return changer(money,coins.tail,c)
      }
    } else {
      return c
    }
  }

  def countChange(money: Int, coins: List[Int]): Int = {
    if (money == 0) {
      return 0
    } else {
      if (coins.isEmpty) {
        return 0
      } else {
        changer(money,coins,0)
      }
    }
    
  }
}
