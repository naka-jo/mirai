import glob

files_original = glob.glob('./data_original/*')
files_original = sorted(files_original)
files_modern = glob.glob('./data_modern/*')
files_modern = sorted(files_modern)

for f_original, f_modern in zip(files_original, files_modern):
    with open(f_original, 'r') as f:
        lines_original = f.readlines()
    c_original = len(lines_original)

    with open(f_modern, 'r') as f:
        lines_modern = f.readlines()
    c_modern = len(lines_modern)

    print(f'{f_original}: {c_original}, {f_modern}: {c_modern}')