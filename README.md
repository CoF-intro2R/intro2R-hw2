# Homework 2

In this homework, you will use some of the commands you learned in week two to report some summaries of a dataset. These data are stored for you in this repo already.

For this week, I will not give you specific commit messages or instruct you in when to commit changes. You can develop your own workflow from now on, but I recommend committing changes regularly and at logical breaks in the development of your project so it's easy to go back to specific versions of the project if necessary. Make your commit messages concise but specific so you could return the project to a specific state/version if necessary.

## Setting up your project

1) Clone your assignment repo to your local machine and add a directory called `/R` and one called `/Results`. Add an R script to the `/R` directory and name it `hw2.R`.

2) Open your R script using RStudio and add code to complete the following tasks. Your code should be commented well and will, upon completion, add a file called `data_summaries.txt` to the `/Results` folder with your solutions to the tasks below.

## Tasks to complete

The fictitious data you will be using to practice newly developed R skills assumes we have discovered microscopic alien lifeforms on some new planets that an intrepid space explorer, *Spaceman Spiff*, has discovered. In a daring mission, Spaceman Spiff visited all planets to take soil samples. Amoeba-like lifeforms were discovered on four of the planets in the `Zargot-2` system. The data are collections of morphological measurements painstakingly taken under a microscope for many thousands of these lifeforms.

1) Load the `aliens.csv` data using either relative file paths or the `here()` function from package `here`.

2) Determine how many `NA` values exist in the data. Store the result as an object with a name you can remember.

3) Determine the mean and standard deviation of the *2D area* of these single cell lifeforms (averaged across all measurements). Assume that the area can be approximated by an ellipse, and recall that the area of an ellipse can be calculated as

$$
A = \pi ab
$$

  where $a$ is half the length of the major axis (the "radius in the long direction") and $b$ is half the length of the minor axis (the "radius in the short direction"). Store the mean and standard deviation of the area as objects and give them names you can remember.

4) Add the following lines to the script, **being sure to replace `<results-file.txt` with the name and filepath to the results file you will turn in. You can use relative file paths or the `here` package. The file should be called `/Results/data_summaries.txt`:

```r
if(!exists(<results-file.txt>)){
  file.create(<results-file.txt>)
}
```

5) Using the `paste()` function and the named objects you created, write code that ouputs

> `The number of NA values in the data is <count>`.

6) Do the same for the other summaries, **being sure to round the result to 2 places past the decimal using the `round()` function**. The units should be written as "mm^2".

> `The mean of the cell area is <mean units>`.

> `The sd of the cell area is <sd units>`.

7) Once you have these working, wrap each of these `paste()` calls in or pipe them to the `writeLines()` function so that these summaries are each written to a new line of the `/Results/data_summaries.txt` file.

8) Check your results and push them up to the remote when you are satisfied.

## Grading rubric

- 1 pt for complete and correct repo.

- 0.5 pt for full attempt.

- 0 pt for less than a full attempt.



