import MeCab

tagger_original = MeCab.Tagger('-O wakati -d ./UniDic-wabun_1603')
tagger_modern = MeCab.Tagger('-O wakati -d ./unidic-cwj-3.1.1-full')

with open('./train_data/train.original', 'r') as f:
    lines = f.readlines()

with open('./train_data/train.original', 'w') as f:
    for line in lines:
        f.writelines(tagger_modern.parse(line))

with open('./train_data/train.modern', 'r') as f:
    lines = f.readlines()

with open('./train_data/train.modern', 'w') as f:
    for line in lines:
        f.writelines(tagger_original.parse(line))


with open('./test_data/test.original', 'r') as f:
    lines = f.readlines()

with open('./test_data/test.original', 'w') as f:
    for line in lines:
        f.writelines(tagger_modern.parse(line))

with open('./test_data/test.modern', 'r') as f:
    lines = f.readlines()

with open('./test_data/test.modern', 'w') as f:
    for line in lines:
        f.writelines(tagger_original.parse(line))