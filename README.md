# Whats in this repository?
1. The source code - inputTester.py (If you want to take a look or make changes, though it isn't necessary to run the program).
2. The executable - inputTester (Download this to run the program!)
# Four important things:
1. The program is meant to work **in a linux enviorment!** Make sure your'e running it in WSL or a linux machine.
2. You might need to have python installed to run the program, if your'e having problems, make sure python3 is installed on your linux machine.
   To install python on linux:
   ```shell
   sudo apt install python3
   ```
3. I've tried, but the program can't run on mobax. There's libraries that can't be installed there (dont try, I've got reported for trying).
4. You'll need to give the ```inputTester``` executable permissions to run on your linux machine. To do that, run this command in the same directory:
   ```shell
   chmod +x inputTester
   ```
   You will also need to do the same for the instructor's .out file:
   ```shell
   chmod +x <Instructors file name>
   ```
# How does it work?
1. Place the executable ("InputTester") in the same directory as your .c code.
2. Place the instructor provided .out file in the same directory.
3. Create a text file named: "input.txt" (The name must match!).
4. Write the following lines into "input.txt":

**line 1**: -The name of your program-

**line 2**: -The name of the instructor's .out file-

**line 3**: "y" if your program requires command line args, "n" if it doesnt

**line 4**: If you've written "y" in line 3, insert arguments here, seperated by a space. If you've written "n" start writing the desired input for the program.

**line 5+**: From here onward start writing the desired input, each line will be given to the program at run-time.

5. Run the program by typing:
   ```
   ./inputTester
   ```
   In the linux Terminal.
6. That's it. A folder named "test results" has been created and you can see the results there.

### Example of input.txt with command line args: 
```
ex_4.c
example.out
y
2 2 yotam#itay pen ipad 0 1 2 3
0
0
0
1
1
0
1
1
```
This example shows how you can use the program to test your code for ex_4. Notice tgat command line arguments were given, so input lines start at line 5.
### Example of input.txt without line args:
```
myProgram.c
example.out
n
0
1
2
1
0
0
2
hello
test
```
In this example no arguments were given, and the input lines start at line 4.

# How to read the comparison file:

The comparison file will only include the text **around the aread where differences were found**. For example if the output is 100 lines, but differences were found only around lines 22-35 and 66-89, only those lines will be included.
## The syntax:

'!' before a line means the line has a difference. Thats basically all you need to know.

## Example comparison file for ex 4:


```
***  '*' Marks correct output
--- '-' marks YOUR output

***************
(Here, the file specifies differences were found between line 21 to 39)
*** 21,39 ****

  5. cheese

  6. rotor

  7. oil

! 8. tracto ('!' Means the difference is here)

  

  Let the game begin!

  

  Current board state:

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 21,39 ----

  5. cheese

  6. rotor

  7. oil
	
! 8. tractor

  

  Let the game begin!

  

  Current board state:

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 43,55 ****

  yotam: 1, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |       X       |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 43,55 ----

  yotam: 1, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | X | X | X |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

! | X | X | X | pen |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 59,71 ****

  yotam: 2, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |      ipad     |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 59,71 ----

  yotam: 2, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | X | X |

  -----------------------------------------------------------------

! | X | ipad | X | X |

  -----------------------------------------------------------------

! | X | X | X | pen |

  -----------------------------------------------------------------

! | X | X | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 75,87 ****

  yotam: 3, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |     apple     |       X       |

  -----------------------------------------------------------------

! |       X       |      ipad     |       X       |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |     apple     |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 75,87 ----

  yotam: 3, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | apple | X |

  -----------------------------------------------------------------

! | X | ipad | X | X |

  -----------------------------------------------------------------

! | X | X | X | pen |

  -----------------------------------------------------------------

! | X | apple | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 91,103 ****

  yotam: 4, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |     apple     |      ring     |

  -----------------------------------------------------------------

! |       X       |      ipad     |      ring     |       X       |

  -----------------------------------------------------------------

! |       X       |       X       |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |     apple     |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 91,103 ----

  yotam: 4, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | apple | ring |

  -----------------------------------------------------------------

! | X | ipad | ring | X |

  -----------------------------------------------------------------

! | X | X | X | pen |

  -----------------------------------------------------------------

! | X | apple | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 107,119 ****

  yotam: 5, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |     apple     |      ring     |

  -----------------------------------------------------------------

! |     cheese    |      ipad     |      ring     |       X       |

  -----------------------------------------------------------------

! |     cheese    |       X       |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |     apple     |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 107,119 ----

  yotam: 5, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | apple | ring |

  -----------------------------------------------------------------

! | cheese | ipad | ring | X |

  -----------------------------------------------------------------

! | cheese | X | X | pen |

  -----------------------------------------------------------------

! | X | apple | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 123,135 ****

  yotam: 6, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |     apple     |      ring     |

  -----------------------------------------------------------------

! |     cheese    |      ipad     |      ring     |     rotor     |

  -----------------------------------------------------------------

! |     cheese    |     rotor     |       X       |      pen      |

  -----------------------------------------------------------------

! |       X       |     apple     |       X       |       X       |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 123,135 ----

  yotam: 6, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | apple | ring |

  -----------------------------------------------------------------

! | cheese | ipad | ring | rotor |

  -----------------------------------------------------------------

! | cheese | rotor | X | pen |

  -----------------------------------------------------------------

! | X | apple | X | X |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 139,151 ****

  yotam: 7, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! |      pen      |      ipad     |     apple     |      ring     |

  -----------------------------------------------------------------

! |     cheese    |      ipad     |      ring     |     rotor     |

  -----------------------------------------------------------------

! |     cheese    |     rotor     |      oil      |      pen      |

  -----------------------------------------------------------------

! |       X       |     apple     |       X       |      oil      |

  -----------------------------------------------------------------

  

  It is yotam's turn.

--- 139,151 ----

  yotam: 7, liav: 0, itay: 0

  Current board state:

  -----------------------------------------------------------------

! | pen | ipad | apple | ring |

  -----------------------------------------------------------------

! | cheese | ipad | ring | rotor |

  -----------------------------------------------------------------

! | cheese | rotor | oil | pen |

  -----------------------------------------------------------------

! | X | apple | X | oil |

  -----------------------------------------------------------------

  

  It is yotam's turn.

***************

*** 153,156 ****

  

  The scores are:

  yotam: 8, liav: 0, itay: 0

! Congratulations yotam! You won!

--- 153,156 ----

  

  The scores are:

  yotam: 8, liav: 0, itay: 0

! Congratulations yotam! You won!
```


