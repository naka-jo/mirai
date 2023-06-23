import glob

files = glob.glob('./data_original/*')
files = sorted(files)

for file in files:
    with open(file, 'r') as f:
        s = f.read()
        print(file)
        print(len(s))