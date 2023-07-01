import MeCab

tagger_original = MeCab.Tagger('-O wakati -d ./UniDic-wabun_1603')
tagger_modern = MeCab.Tagger('-O wakati -d ./unidic-cwj-3.1.1-full')

text = '私はペンを持っています'

new_text = tagger_modern.parse(text)

print(new_text)