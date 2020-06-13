import random

#手の定義
rock = 0
scissors = 1
paper = 2

#ランダムに手を選択
hand = [rock, scissors,  paper]
my_hand = random.choice(hand)
enemy_hand = random.choice(hand)

#勝敗
judge = ["引き分け", "敗北", "勝利"]

#結果
result = judge[(my_hand - enemy_hand + 3)%(3)]
hand = ["グー",  "チョキ", "パー"]
print("あなた：" + hand[my_hand])
print("相手：" + hand[enemy_hand])
print("勝敗：" + result)