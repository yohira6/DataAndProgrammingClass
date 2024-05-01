#課題1:段階的詳細化
#日にち:4月24日
#学籍番号:70311033
#どんな処理か:小学生1年生までの引き算をする処理　1~9の数を設定→数字を出力メソッドに返す→式にして表示
#数字を出力メソッドに返す→負の数の場合「まだ習ってないよ！」を表示


#処理部分
import random

def number():
    first = random.randint(0 , 10)
    second = random.randint(0 , 10)
    third = random.randint(0 , 10)
    return first, second, third

def print_subtraction(first, second, third):
    if(0 <= first - second - third):
        print (first)
        print (second)
        print (third)
        print (str(first) + "-" +  str(second) + "-" + str(third) + "=" + str(first - second - third) )
    if(0 > first - second - third):
        print ("まだ習ってないよ!" + "(式[" + str(first) + "-" +  str(second) + "-" + str(third) + "])")
first, second, third = number()
print_subtraction(first, second, third)