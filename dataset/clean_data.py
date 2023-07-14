import re
import glob

def remove_htmltag(file):
    with open(file, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        line = re.sub('<p>', '\n', line)
        line = re.sub('</p>', '\n', line)
        line = re.sub('<.>', '', line)
        line = re.sub('<..>', '', line)
        line = re.sub('<...>', '', line)
        line = re.sub('（.*?）', '', line)
        line = re.sub('【.*?】', '', line)
        line = re.sub('<.*?>', '', line)
        line = re.sub('\[.*?\]', '', line)
        line = re.sub('《.*?》', '', line)
        line = re.sub('〔.*?〕', '', line)
        
        judge = re.search(r'第.章', line)
        if judge == None:
            new_lines.append(line)
    
    with open(file, 'w') as f:
        for line in new_lines:
            f.write(line)
    return None

# file = './test.txt'
# module = remove_htmltag(file)

files = glob.glob('./dataset_splitP/data_original/*')
for file in files:
    module = remove_htmltag(file)

files = glob.glob('./dataset_splitP/data_modern/*')
for file in files:
    module = remove_htmltag(file)