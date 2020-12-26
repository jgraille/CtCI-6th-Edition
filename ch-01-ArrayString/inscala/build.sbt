ThisBuild / scalaVersion := "2.12.7"
ThisBuild / organization := "CtCI"

lazy val hello = (project in file("."))
  .settings(
    name := "arraystring"
  )

