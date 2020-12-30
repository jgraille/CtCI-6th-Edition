import Array._

class Matrix(val dim: Int) {
    var largeur: Int = dim
    var longueur: Int = dim  

def init(): Array[Array[Int]] = {
    var matrix = ofDim[Int](largeur,longueur)
    return matrix 
    }
}

object Create extends App {
    val myMatrix = new Matrix(4);
    for (x <- myMatrix.init()) {
        for (y <- x) {
            print(y)
        }
    }
}