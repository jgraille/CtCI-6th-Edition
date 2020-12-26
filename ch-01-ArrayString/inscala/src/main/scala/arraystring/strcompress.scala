package arraystring
import scala.collection.mutable.ListBuffer
import scala.collection.mutable.Map

object ArrayString {
  def stringcompression(input: String): Map[Char,Int] = {
      var len : Int = input.length()
      var dic : scala.collection.mutable.Map[Char,Int] = Map()
      var output : ListBuffer[String] = new ListBuffer[String]()
      for (i <- input) {
        if (dic.contains(i)) {
          dic(i) += 1
        } else {
          dic += (i -> 1)
        }
      }
      return dic
  }

  def main(args: Array[String]) {
    val myList : List[String] = List("aabcccccaaa","abc","AACTTTTUV")
    println(stringcompression(myList(0)))
   }

}