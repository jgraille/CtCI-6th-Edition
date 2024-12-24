object PatternRefresh {

    // Simple pattern matching
    val theValue: Double = 0.002
    val verifyTheValue = theValue match {
        case 0.001 => "good value"
        case _ => s"$theValue" + " wrong value" 
    }
    
    println(verifyTheValue)

    // Checking the value of an element at the 4th position
    // no matter the size of the list
    // :: operator to separate head and remaining of the list
    val someStrings: List[String] = List("one","two","three","four","five","six","seven")
    val verifyTheFourthElement1 = someStrings match {
        case _ :: _ :: _ :: "four" :: _ => s"the value four is at the 4th position"
        case _ => "the value four is not at the 4th position"
    }

    val verifyTheFourthElement2 = someStrings match {
        case List(_,_,_,"four",_*) => s"the value four is at the 4th position"
        case _ => "the value four is not at the 4th position"
    }

    println(verifyTheFourthElement1)
    println(verifyTheFourthElement2)


    val numbers: List[Int] = List(1,2,3,4)
    val emptyNumbers: List[Int] = List()
    emptyNumbers match {
        case Nil => println("empty list")
        case h :: t => println(s"$h" + " " + s"$t")
    }

    // Nil stands for empty
    def processList(numbers: List[Int]): String =  numbers match {
        case Nil => ""
        case h :: t => s"$h" + " " + processList(t)
    }

    println(processList(emptyNumbers))

    numbers match {
        case List(1,_*) :+ 4 => println("ends with 4")
        case _ => println("doesn't end with 4")
    }

    case class Person(name: String, age: Int, favoriteMovies: List[String])
    def requestMoreInfo(p: Person): String = {"Age:" + p.age + " Favorite movies: " + p.favoriteMovies}
    val bob = Person("Bob", 34, List("Inception", "The Departed"))
    bob match {
        case p @ Person(name, _, _) => println(s"$name's info: ${requestMoreInfo(p)}")
    }

}