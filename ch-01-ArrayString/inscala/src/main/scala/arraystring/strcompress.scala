package arraystring
import scala.collection.mutable.ListBuffer
import scala.collection.mutable.Map

object ArrayString {
  def stringcompression(input: String): String = {
    var len : Int = input.length
    var list : ListBuffer[String] = new ListBuffer[String]()
    var dic : scala.collection.mutable.Map[String,Int] = Map()
    var i : Int = 0
    while (i < len) {
      var s : String = input(i).toString
      if (dic.contains(s)) {
        dic(s) = dic(s) + 1
      } else {
        dic += (s -> 1)
      }
      if (i < (len - 1)) {
        if (input(i) != input(i+1)) {
          list += s.concat(dic(s).toString)
          dic.remove(s)
        }
      } else {
        list += s.concat(dic(s).toString)
      }
      i = i + 1
    }
    var ans : String = list.mkString("")
    if (ans.length > len) {
      ans = input
    }
    return ans
  }

  def main(args: Array[String]) {
    val myList : List[String] = List("aabcccccaaa","abc","AAAACTTTTUV")
    val resList = myList.map(stringcompression)
    println(myList)
    println(resList)
   }

}