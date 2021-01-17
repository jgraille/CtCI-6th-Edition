package example

object Lists extends App {

  /**
   * This method computes the sum of all elements in the list xs. There are
   * multiple techniques that can be used for implementing this method, and
   * you will learn during the class.
   *
   *  - `xs.isEmpty: Boolean` returns `true` if the list `xs` is empty
   *  - `xs.head: Int` returns the head element of the list `xs`. If the list
   *    is empty an exception is thrown
   *  - `xs.tail: List[Int]` returns the tail of the list `xs`, i.e. the the
   *    list `xs` without its `head` element
   *
   * @param xs A list of natural numbers
   * @return The sum of all elements in `xs`
   */
  def sum(xs: List[Int]): Int = {
    xs match {
      case Nil => 0
      case x :: xss => x + sum(xss)
      // a list with at least one element. x is bound to the head,
      // xss to the tail. xss could be Nil or some other list.
    }
  }

  /**
   * This method returns the largest element in a list of integers. If the
   * list `xs` is empty it throws a `java.util.NoSuchElementException`.
   *
   * You can use the same methods of the class `List` as mentioned above.
   *
   * @param xs A list of natural numbers
   * @return The largest element in `xs`
   * @throws java.util.NoSuchElementException if `xs` is an empty list
   */
  def compare(x: List[Int]): Int = {
    if (x(0) > x(1)) {
      x(0)
    } else {
      x(1)
    }
  }
  /**
  def maxBis(xs: List[Int]): Int = {
    if (xs.isEmpty) {
      return 0
    } else if (xs.length == 2) {
      return compare(xs)
    } else {
      return max(xs.tail)
    }
  }
  */
  def max(xs: List[Int]): Int = {
    xs match {
      case Nil => 0
      case x :: Nil => x
      case xs @ (_::_::Nil) => compare(xs)
      case _ => max(xs.tail)
    }
  }
}
