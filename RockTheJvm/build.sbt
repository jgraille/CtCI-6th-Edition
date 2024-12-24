ThisBuild / scalaVersion := "3.3.4"
ThisBuild / organization := "CtCI"
Global / onChangedBuildSource := ReloadOnSourceChanges // Automatically reload the build when source changes are detected by setting
Compile / run / fork := true
 
scalacOptions ++= Seq("-deprecation","-explain")

lazy val starter = (project in file("."))
    .settings(
        name := "Starter"
    )