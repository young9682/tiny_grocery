import random
miniMum = int(input("请输入生成数字炸弹的范围中最小的数"))

maxMum = int(input("请输入生成数字炸弹的范围中最大的数"))

bomb = random.randint(miniMum, maxMum)

print("要开始了哟~")
print("man,what can I say ,猜测数字炸弹的范围是从", miniMum, "到", maxMum, "之间")

def compare_degree(a , b):
    Gap = abs(a - b)
    if Gap >= 100:
        return "杂鱼杂鱼，你离炸弹还差太远呢"
    elif Gap >= 50 and Gap < 100:
        return "虽然你离炸弹的距离已经不远了,但你还是杂鱼呢"
    elif Gap >= 20 and Gap < 50:
        return "哼,你这杂鱼有几分本事呢，炸弹还有段距离呢"
    elif Gap >= 10 and Gap < 20:
        return "杂鱼，才没有为你要猜到而高兴呢，快接近了"
    elif Gap >= 2 and Gap < 10:
        return "我要气死了，明明快到了还能猜错，真是杂鱼呢"
    elif Gap == 1:
        return "啊啊啊啊，受不了了，离炸弹就差一步了，你这个杂鱼"
    else:
        return "恭喜你，你猜对了，你这杂鱼做事情还挺靠谱的吗"

def guess_result(guessCount):
    if guessCount == 1:
        print("这都要作弊吗，狗运这一块")
    elif guessCount >= 2 and guessCount <= 5:
        print("你这个杂鱼，居然猜对了")
    elif guessCount >= 6 and guessCount <= 20:
        print("看的出来你这个杂鱼尽力了呢")
    else:
        print("你是杂鱼程序员吗，过来测试程序的吧")


guessCount = 0

while True:
    guess = int(input("请输入你猜的数字炸弹的数字"))
    guessCount += 1

    if guess < miniMum or guess > maxMum:
        print("你输入的数字炸弹不在范围内，请重新输入")
        guessCount -= 1

    elif guess < bomb:
        print("你猜的数字炸弹小了")
        print(compare_degree(guess, bomb))

    elif guess > bomb:
        print("你猜的数字炸弹大了")
        print(compare_degree(guess, bomb))

    else:
        print("恭喜你猜对了，炸弹的数字是", bomb)
        print(compare_degree(guess, bomb))
        guess_result(guessCount)
        break