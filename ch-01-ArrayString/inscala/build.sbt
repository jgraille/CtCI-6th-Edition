ThisBuild / scalaVersion := "2.13.3"
ThisBuild / organization := "CtCI"

libraryDependencies += "org.scalactic" %% "scalactic" % "3.2.2"
libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.2" % Test

lazy val hello = (project in file("."))
  .settings(
    name := "StrCompress"
  )
logBuffered in Test := false


