import glob

# def make_parallel(file_path):
#     with open(file_path, 'r') as f:
#         lines = f.readlines()

#     lines_1 = []
#     lines_2 = []

#     for line in lines:
#         line = line.replace('\u3000', '')
#         lines_1.append(line)

#     for line in lines_1:
#         if line != '\n':
#             lines_2.append(line)

#     with open(file_path, 'w') as f:
#         for line in lines_2:
#             f.write(line)

files = glob.glob('../finished/data_original/*')
files = sorted(files)
del files[0]
train = files[:46]
val = files[46:]
for file in train:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open('../parallel_corpus/train_data/train_original.txt', 'a') as f:
        for line in lines:
            f.write(line)

for file in val:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open('../parallel_corpus/val_data/val_original.txt', 'a') as f:
        for line in lines:
            f.write(line)

files = glob.glob('../finished/data_modern/*')
files = sorted(files)
del files[0]
train = files[:46]
val = files[46:]
for file in train:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open('../parallel_corpus/train_data/train_modern.txt', 'a') as f:
        for line in lines:
            f.write(line)

for file in val:
    with open(file, 'r') as f:
        lines = f.readlines()
    with open('../parallel_corpus/val_data/val_modern.txt', 'a') as f:
        for line in lines:
            f.write(line)