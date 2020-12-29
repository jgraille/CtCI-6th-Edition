class StrCompressTest extends org.scalatest.funsuite.AnyFunSuite {
  test("StrCompress.run") {
    assert(StrCompress.run("aabcccccaaa") === "a2b1c5a3")
    assert(StrCompress.run("abc") === "abc")
    assert(StrCompress.run("AAAACTTTTUV") === "A4C1T4U1V1")
    assert(StrCompress.run("") === "")
  }
}