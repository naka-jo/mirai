import glob

def make_parallel(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    lines_1 = []
    lines_2 = []

    for line in lines:
        line = line.replace('\u3000', '')
        lines_1.append(line)

    for line in lines_1:
        if line != '\n':
            lines_2.append(line)

    with open(file_path, 'w') as f:
        for line in lines_2:
            f.write(line)

files = glob.glob('./data_original/*')
# files = sorted(files)
# make_parallel(files[0], './parallel/test_data/test_original.txt')
# del files[0]
for file in files:
    make_parallel(file)

files = glob.glob('./data_modern/*')
# files = sorted(files)
# make_parallel(files[0], './parallel/test_data/train_modern.txt')
# del files[0]
for file in files:
    make_parallel(file)