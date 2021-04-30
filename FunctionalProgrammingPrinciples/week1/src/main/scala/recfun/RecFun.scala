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
    val res = countP("t(hi(s".toList)
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
    if (countPright(chars))
  }

  def countPright(chars: List[Char]): Int = {
    if (chars.isEmpty) {
      0
    } else if (chars.head == '(') {
      return countP(chars.tail) + 1
    } else {
      return countP(chars.tail) 
    }
  }

  def countPLeft(chars: List[Char]): Int = {
    if (chars.isEmpty) {
      0
    } else if (chars.head == '(') {
      return countP(chars.tail) + 1
    } else {
      return countP(chars.tail) 
    }
  }

  /**
   * Exercise 3
   */
  def countChange(money: Int, coins: List[Int]): Int = ???
}
