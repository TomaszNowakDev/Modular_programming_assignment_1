# Modular Programming Assignment 1

A teacher runs a rewards system in her classroom. Students sit at four different tables, each with a different name. Each table earns points for good behavior and good work. If all the tables have a minimum number of points, the children can watch a movie on Friday.
Create a main () function.
Add code to print out your name to the screen.
Call this main () function.
Add the following to the main () function (you can copy and paste from here):
tables = ["Glas", "Dubh", "Gorm", "Dearg"]
Write each of the following functions and call them from main (), using print () in main () where necessary to print the returned / edited data.
### Q1
Write a function to ask for and return the teacher's name and the minimum points each table must earn to watch a movie.
The minimum points should be validated as a positive, integer number.
### Q2
Write a function that receives the tables' names and returns a list of the number of points each table has earned.
Each number of points should be validated as a positive, integer number.
The name of the table should appear in the prompt.
### Q3
The children were very noisy when the teacher stepped outside to talk with a colleague.
Write a function that receives a list of the number of points each table has earned.
The function should reduce each table's points by 1 as a consequence of their behavior.
### Q4
Write a function that receives the names of the tables, the number of points each table has earned, and the teacher's name.
The function should print the teacher's name and a neat table of each table's name and points earned, and place a star (*) after the points for each table that has fewer than 10 points
### Q5
The children will get to watch a movie on Friday if each table has earned a minimum number of points, specified by the teacher in Q1. Write a function that receives the number of points for each table and the minimum number of points per table for a movie, and prints a message to let them know if they can or cannot watch a movie on Friday.
