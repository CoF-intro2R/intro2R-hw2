# autograding hw2

import os
import pytest

def test_dir_struc():
  assert os.path.isdir("R")
  assert os.path.isdir("Results")
  assert os.path.isfile("R/hw2.R")
  assert os.path.isfile("Results/data_summaries.txt")

def test_results():
  if os.path.isfile("Results/data_summaries.txt"):
    
    with open("Results/data_summaries.txt", 'r') as res:
      content = res.read()
      
    line1 = 'The number of NA values in the data is 202\n'
    line2 = 'The mean of the cell area is 3.657 microns^2\n'
    line3 = 'The sd of the cell area is 2.783 microns^2\n'

    lines = [line1, line2, line3]
    ans = "".join(lines)
      
    assert content == ans

