import binascii

def interpret(program):

    p_len = len(program)
    bf_tape = [0] * 30000   # max 30k cells
    tape_idx = 0
    prog_index = 0

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
        else: 
            prog_index += 1
    return bf_tape

def main():
    # Example programs:
    # 5 + 2 = 7          ++>+++++<+>-
    # Hello world        ++++++++[>++++[>++>+++>+++
    #                    >+<<<<-]>+>+>->>+[<]<-]>>.>
    #                    ---.+++++++..+++.>>.<-.<.+++.
    #                    ------.--------.>>+.>++.
    # 
    # 

    program = input("Please enter some source code: ")
    # Only print out the cells with nonzero values
    for cell in interpret(program):
        if cell != 0:
            print(cell, end =" ")

main()
