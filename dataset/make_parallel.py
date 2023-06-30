import glob

def make_parallel(file_path, parallel_path):
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

    with open(parallel_path, 'a') as f:
        for line in lines_2:
            f.write(line)
            
files = glob.glob('./data_original/*')
files = sorted(files)
for file in files:
    module = make_parallel(file, './parallel/parallel_original.txt')
    
files = glob.glob('./data_modern/*')
files = sorted(files)
for file in files:
    module = make_parallel(file, './parallel/parallel_modern.txt')