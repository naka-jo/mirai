before_file = './save/result.txt'

after_file = './save/cleanup.txt'

with open(before_file, 'r') as f:
    lines = f.readlines()

with open(after_file, 'w') as f:
    for line in lines:
        f.writelines(line.replace(' ', ''))