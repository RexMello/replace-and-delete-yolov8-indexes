
import os

NAME_OF_FOLDER = 'data'

file_paths = []
for name in os.listdir(NAME_OF_FOLDER):
    if '.txt' not in name:
        continue
    file_paths.append(f'{NAME_OF_FOLDER}/{name}')

def replace_index(line, old_index, new_index):
    parts = line.split()
    if len(parts) > 0 and parts[0] == old_index:
        parts[0] = new_index
    return ' '.join(parts)

for file_path in file_paths:
    with open(file_path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        if '21' == line.split()[0]:
            print(file_path)
            # os.remove(file_path)
            # break

    # with open(file_path, 'w') as file:
    #     for line in lines:
    #         updated_line = replace_index(line, '32', '21')
    #         file.write(updated_line)