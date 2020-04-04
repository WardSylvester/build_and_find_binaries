def build_and_find_binaries(current_str, target_len, current_len, one_counter, zero_counter):
    if current_len < target_len:
        build_and_find_binaries(current_str+'0', target_len, current_len+1, one_counter, zero_counter+1)
        build_and_find_binaries(current_str+'1', target_len, current_len+1, one_counter+1, zero_counter)
    if current_len == target_len:
        print(current_str)


build_and_find_binaries('', 4, 0, 0, 0)