import glob

def count(files):
    c = 0
    for o in files:
        with open(o, 'r') as f:
            lines_o = f.readlines()
        c += len(lines_o)
    print(c)
        
        


files_o = glob.glob('../finished/data_original/*')
files_o = sorted(files_o)
del files_o[0]
count(files_o)