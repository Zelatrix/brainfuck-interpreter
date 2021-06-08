import sys
import re 

args = []  # A list to store the flags passed into the code when run

def interpret(program):
    
    if len(sys.argv) == 1:
        p_len = len(program)
    else:
        regex = re.compile(".*\.bf")
        for arg in range(len(sys.argv)):
            if regex.match(sys.argv[arg]):
                inp_file = open(sys.argv[arg]).read()
                p_len = len(inp_file)

    bf_tape = [0] * 30000   # max 30k cells
    
    tape_idx = 0
    prog_index = 0
    indentation = 1 # The nesting level for loops

    # While loop interpreter
    while prog_index < p_len:
        # Increment the value in the current cell
        if program[prog_index] == "+":
            bf_tape[tape_idx] += 1
            prog_index += 1
        # Decrement the current cell value
        elif program[prog_index] == "-":
            bf_tape[tape_idx] -= 1
            prog_index += 1
        # Move one cell forward on the tape
        elif program[prog_index] == ">":
            tape_idx += 1
            prog_index += 1
        # Move one cell backwards on the tape
        elif program[prog_index] == "<":
            tape_idx -= 1
            prog_index += 1
        
        # Looping
        elif program[prog_index] == "[":
            if bf_tape[tape_idx] == 0:
                while program[prog_index] != "]":
                    prog_index += 1
                prog_index += 1
            else:
                prog_index += 1
        elif program[prog_index] == "]":
            if bf_tape[tape_idx] != 0:
                while program[prog_index] != "[":
                    prog_index -= 1
                prog_index += 1
            else:
                prog_index += 1
        
        # Output the byte at the current index
        elif program[prog_index] == ".":
            char = bf_tape[tape_idx]
            bf_tape[tape_idx] = chr(char)
            prog_index += 1
        # Take in a single byte as input
        elif program[prog_index] == ",":
            single_byte = input()[0]
            bf_tape[tape_idx] = single_byte
            prog_index += 1
        else: 
            prog_index += 1
    return bf_tape
        
def main():
    if len(sys.argv) == 1:
        program = input("brainfuck> ")
    else:
        regex = re.compile(".*\.bf")
        for arg in range(len(sys.argv)):
            if regex.match(sys.argv[arg]):
                program = open(sys.argv[arg]).read()

    # Checking program arguments
    if "--tape" in sys.argv:
        args.append("--tape")

    if "--tape" in args:    
        print(interpret(program))
    else:
        # Only print out the cells with nonzero values
        # print("Output: ", end="")
        for cell in interpret(program):
            if cell != 0:
                print(cell, end="")

if __name__ == "__main__":
    main()