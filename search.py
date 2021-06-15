### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりした".format(word))
    else:
        print("{}が見つかりません".format(word))
        source.append(word)

if __name__ == "__main__":
    search()




import csv

with open('sample.csv','r')as f:
    reader = csv.reader(f)
    print(line)
