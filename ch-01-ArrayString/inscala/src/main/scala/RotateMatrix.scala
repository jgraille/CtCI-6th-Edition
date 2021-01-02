import Array._
import scala.util.control.Breaks._

class Matrix(val dim: Int) {
    var matrix: Array[Array[Int]] = Array.ofDim[Int](dim,dim) 
    
    def feed(): Array[Array[Int]] = {
        var h:Int = 1
        for(i <- 0 to (dim - 1)){
            for(j <- 0 to (dim - 1)){
                matrix(i)(j) = h
                h = h + 1
            }
        }
        return matrix
    }

    def rotate(): Array[Array[Int]] = {
        var rotated: Array[Array[Int]] = Array.ofDim[Int](dim,dim)
        var d: Int = dim - 1
        for (col <- 0 to d) {
            var h: Int = 0
            for (row <- 0 to d) {
                rotated(d - col)(row) = this.feed()(row)(col)
            }
        }
        return rotated
    }

}
object RotateMatix extends App {
    var myMatrix = new Matrix(4)
    var matrix4: Array[Array[Int]] = Array.ofDim[Int](4,4)
    matrix4(0)(0) = 4
    matrix4(1)(0) = 3
    matrix4(2)(0) = 2
    matrix4(3)(0) = 1
    matrix4(0)(1) = 8
    matrix4(1)(1) = 7
    matrix4(2)(1) = 6
    matrix4(3)(1) = 5
    matrix4(0)(2) = 12
    matrix4(1)(2) = 11
    matrix4(2)(2) = 10
    matrix4(3)(2) = 9
    matrix4(0)(3) = 16
    matrix4(1)(3) = 15
    matrix4(2)(3) = 14
    matrix4(3)(3) = 13

    def run(input: Int): Array[Array[Int]] = {
        return myMatrix.rotate()
    }

    def assertEq(array1: Array[Array[Int]], array2: Array[Array[Int]],dim: Int): Boolean = {
        var flag: Boolean = true         
        for (i <- 0 to (dim -1)) {
            for (j <- 0 to (dim -1)) {
                if (array1(i)(j) != array2(i)(j)) {
                    flag = false
                    break()
                }
            }
        }
        return flag
    }
    myMatrix.feed().foreach {row => row foreach print; println()}
    println("--------")
    myMatrix.rotate().foreach {row => row foreach print; println()}
    println(assertEq(myMatrix.rotate(), matrix4, 4))

}