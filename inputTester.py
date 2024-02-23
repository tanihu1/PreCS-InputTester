import subprocess
import os
import difflib
#Create results folder
output_path ="./test results"
if not os.path.exists(output_path):
    os.mkdir(output_path) 
#Read info from input.txt
input_file = open("input.txt","r")
user_code = input_file.readline().strip()
example_out_file = input_file.readline().strip()
args = input_file.readline().strip()
if args.capitalize()=='Y':
    args = input_file.readline().split(" ")
else:
    args = []
input_lines = input_file.readlines()
compiled_file_path = os.path.join(output_path,"your_code")
compile_command = ["gcc",user_code, "-o",compiled_file_path]
#Compile user C file
subprocess.run(compile_command, check=True)

#Store all necessary paths
user_output = os.path.join(output_path,f"{user_code}-output.txt")
example_output = os.path.join(output_path,f"{example_out_file}-output.txt")
diffrences = os.path.join(output_path,"compare_result.txt")
example_out_file = f"./{example_out_file}"

#Run user's code and store output
with open(user_output, 'w') as outfile:
    process = subprocess.Popen([compiled_file_path]+ args, stdin=subprocess.PIPE, stdout=outfile, universal_newlines=True)
    for line in input_lines:
        process.stdin.write(line)
    process.stdin.close()
    process.communicate()
#Run instructor's code and store output
with open(example_output,'w') as outfile:
    process = subprocess.Popen([example_out_file]+ args, stdin=subprocess.PIPE, stdout=outfile, universal_newlines=True)
    for line in input_lines:
        process.stdin.write(line)
    process.stdin.close()
    process.communicate()
#Compare outputs
with open(diffrences,'w') as diff_output:
    with open(example_output,'r') as correct_output, open(user_output,'r') as given_output:
        correct_lines = correct_output.readlines()
        given_lines = given_output.readlines()
        diff = difflib.context_diff(correct_lines,given_lines,fromfile=" '*' Marks correct output",tofile="'-' marks YOUR output")
        diff_output.write('\n'.join(diff))
