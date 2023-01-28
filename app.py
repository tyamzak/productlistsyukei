productList = []

#エラー処理
try:
    # ファイル読込
    with open('productList.csv', 'r') as f:
        # 繰り返し
        while True:
            # 1行ずつ読む
            s = f.readline()
            if s == "":
                break
            else:
                #空白ではない場合、,で分割してLISTに追加する
                productList.append(s.split(',')[1].replace('\n',''))


except:
    # エラーが出た場合の表示
    print('ファイルが読み込めませんでした。')

purchase = []

# エラー処理
try:
    # ファイルの読み込み
    with open('purchase.csv', 'r') as f:
        while True:
            # 1行ずつ読む
            s = f.readline()
            if s == "":
                break
            else:
                #空白ではなかった場合に追加
                purchase.append(s)

except:
    # エラー時の処理
    print('ファイルが読み込めませんでした。')

#日付順になる様に並べ替える
purchase.sort()
#dictを準備
purchase_dict = {}
#0で初期化するための変数
zeros = [0] * len(productList)
# dictを製品リストと0で初期化
purchase_dict = dict(zip(productList,zeros))
yearmonth = ""

#購入データごとに処理
for i in purchase:
    #購入データを日付文字と購入内容に分割
    dateint, item = i.replace('\n','').split(',')

    # 今回処理の日付が前回の日付と一致しなかった場合
    if yearmonth != "" and yearmonth != dateint[0:6]:
        # 出力してリセット
        print(f'<{yearmonth[0:4]} 年 {yearmonth[4:6]} 月>')
        print('{: <16}'.format('製品') + '{: >13}'.format('個数'))
        print('-' * 32)
        # アイテム毎に出力
        for key, value in purchase_dict.items():
            print('{: <16}'.format(key) + '{: >16}'.format(value))
        # dictを製品リストと0で初期化
        purchase_dict = dict(zip(productList,zeros))
        print()
    #前回処理年月の記録
    yearmonth = dateint[0:6]
    # dictに購入数を記録
    if item in productList:
        purchase_dict[item] += 1
    

# forが終了した時にもう一度出力
print(f'<{yearmonth[0:4]} 年 {yearmonth[4:6]} 月>')
print('{: <16}'.format('製品') + '{: >13}'.format('個数'))
print('-' * 32)
for key, value in purchase_dict.items():
    print('{: <16}'.format(key) + '{: >16}'.format(value))
purchase_dict = dict(zip(productList,zeros))
    