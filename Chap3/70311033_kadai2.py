#課題2：データを扱うプログラム
#日にち：2024/05/01
#学籍番号：70311033
#名前：髙橋 天
#処理の説明：CSVファイルをリストで読み込み

#処理部分
import pandas as pd
filename = "data1.csv"
df = pd.read_csv(filename)

#int型に変換
df['pay'] = df['pay'].str.replace(',', '').astype(int)

#CSVを出力
column_pay = df['pay']
print(column_pay)

#範囲を指定して足し算
column_pay_range_sum = df.loc[ 5:10,'pay'].sum()
print("範囲の合計:", column_pay_range_sum)