package recfun

import scala.collection.mutable.ArrayBuffer

object RecFun extends RecFunInterface {

  def main(args: Array[String]): Unit = {
    /*
    println("Pascal's Triangle")
    for (row <- 0 to 10) {
      for (col <- 0 to row)
        print(s"${pascal(col, row)} ")
    }
    */
    val res = balance("t(hi(s))".toList)
    println(res)
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
    if (!chars.isEmpty) {
      val left = countPleft(chars)
      val right = countPright(chars)
      if (left == right) {
        true
      } else {
        false
      }
    } else {
      false
    }
  }

  def countPright(chars: List[Char]): Int = {
    if (chars.isEmpty) {
      0
    }
    else if (chars.head == '(') {
      countPright(chars.tail) + 1
    } else {
      countPright(chars.tail) 
    }
  }

  def countPleft(chars: List[Char]): Int = {
    if (chars.isEmpty) {
      0
    }
    else if (chars.head == ')') {
      countPleft(chars.tail) + 1
    } else {
      countPleft(chars.tail) 
    }
  }
  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = ???
}
