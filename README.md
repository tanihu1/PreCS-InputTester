# Whats in this repository?
1. The source code - inputTester.py (If you want to take a look or make changes, though it isn't necessary to run the program).
2. The executable - inputTester (Download this to run the program!)
# Three important things:
1. The program is meant to work **in a linux enviorment!** Make sure your'e running it in WSL or a linux machine.
2. You might need to have python installed to run the program, if your'e having problems, make sure python3 is installed on your linux machine.
   To install python on linux:
   ```shell
   sudo apt install python3
   ```
3. I've tried, but the program can't run on mobax. There's libraries that can't be installed there (dont try, I've got reported for trying).

# How does it work?
1. Place the executable ("InputTester") in the same directory as your .c code.
2. Place the instructor provided .out file in the same directory.
3. Create a text file named: "input.txt" (The name must match!).
4. Write the following lines into "input.txt":
   line 1: -The name of your program-
   line 2: -The name of the instructor's .out file-
   line 3: "y" if your program requires command line args, "n" if it doesnt
   line 4: If you've written "y" in line 3, insert arguments here, seperated by a space. If you've written "n" start writing the desired input for the program.
   line 5+: From here onward start writing the desired input, each line will be given to the program at run-time.
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
