import Array._

class Matrix(val dim: Int) {
    var largeur: Int = dim
    var longueur: Int = dim
    var matrix: Array[Array[Int]] = Array.ofDim[Int](largeur,longueur)  
    
    def feed(): Array[Array[Int]] = {
        for(i <- 1 to largeur){
            for(j <- 1 to longueur){
                matrix(i)(j) = 1
            }
        }
        return matrix
    }
}
object Diplay extends App {
    val myMatrix = new Matrix(4)
    myMatrix.feed.foreach {row => row foreach print; println}
}