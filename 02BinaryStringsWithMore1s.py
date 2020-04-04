# Ward Sylvester

"""
Write a build_and_find_binaries function below which builds and checks the binary sequences of length as target_len.
If the binary sequence has more 1's than 0's, print it.
This should be a recursive function - you should not use any iteration in your solution.
If the current string does not have the target length yet, there should be two recursive function calls.
If the current string has the target length, it should check and (if there are more 1's) print the binary sequence.

For the function call:
build_and_find_binaries('', 4, 0, 0, 0)

The printed values should be (the sequence of printed values may vary):
0111
1011
1101
1110
1111
"""


def build_and_find_binaries(current_str, target_len, current_len, one_counter, zero_counter):
    if current_len < target_len:
        build_and_find_binaries(current_str+'0', target_len, current_len+1, one_counter, zero_counter+1)
        build_and_find_binaries(current_str+'1', target_len, current_len+1, one_counter+1, zero_counter)
    else:
        if one_counter > zero_counter:
            print(current_str)
        

build_and_find_binaries('', 4, 0, 0, 0)
build_and_find_binaries('', 8, 0, 0, 0)

