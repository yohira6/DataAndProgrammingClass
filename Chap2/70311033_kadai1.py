#課題1:段階的詳細化
#日にち:4月24日
#学籍番号:70311033
#どんな処理か:引き算をする処理　数を設定→数字を出力メソッドに返す→式にして表示


#処理部分
def number():
    first = 10
    second = 2
    third = 4
    return first, second, third

def print_subtraction(first, second, third):
    print (first)
    print (second)
    print (third)
    print (str(first) + "-" +  str(second) + "-" + str(third) + "=" + str(first - second - third) )

first, second, third = number()
print_subtraction(first, second, third)