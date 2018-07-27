import random
#import col


MaxCount = 1000
ChildrenNum = 100
DefaultStr='abcdefghijklmnopqrstuvwxyz '

# 指定した長さのランダムな文字列の生成
def MakeRandomStr(length, DefaultStr = 'abcdefghijklmnopqrstuvwxyz '):
    sr = random.Random()
    return ''.join([sr.choice(DefaultStr) for i in range(length)])

# 評価関数
def CalcStr(random_str, Goal_Str):
    score = 0
    for i in range(len(Goal_Str)):
        score += abs(DefaultStr.find(random_str[i]) - DefaultStr.find(Goal_Str[i]))
    return score

# 確率的に選択
def rand_select(epsilon=0.45):
    rand = random.random()
    if epsilon > rand:
        return 0
    elif epsilon < rand < epsilon+0.45:
        return 1
    else:
        return 2

# 遺伝子の交叉
def update(random_list, Goal_Str, generation):
    children = []
    childrenNo = 0
    for num0, i in enumerate(random_list):
        for num1, j in enumerate(random_list):
            if (num0 == num1):
                continue

            parent = []
            # 両親
            parent.append(i)
            parent.append(j)
            # 突然変異
            parent.append(MakeRandomStr(len(Goal_Str)))

            child = ''
            for k in range(len(Goal_Str)):
                # 親か突然変異か選ぶ
                sentence = parent[rand_select()]
                try:
                    child += sentence[k]
                except IndexError:
                    print(parent)
                    exit()

            children.append([child, CalcStr(child, Goal_Str)])
    children = sorted(children, key=lambda x: x[1])
    child_list=[]
    for i in range(ChildrenNum):
        try:
            child_list.append(children[i][0])
        except IndexError:
            print('i:{0}  length:{1}'.format(i, len(children)))
            exit()
        # 一致した場合
        if children[i][1] == 0:
            print('______________________________________')
            print('Goal_Str Found at Generation{0}'.format(generation))
            #col.blue('Goal_Str Found at Generation{0}'.format(generation))
            print(children[i][0])
            print('______________________________________')
            exit()
    return child_list

# 評価値の高い遺伝子を選択
def MakeBetterParents(bad_parents):
    betterparents = []
    for i in range(ChildrenNum):
        betterparents.append(bad_parents[rand_select()])
    return betterparents

# 実行部
def main():
    #Goal_Str = input()
    Goal_Str = 'future university'
    parent_list = []
    # 初期個体の生成
    for i in range(ChildrenNum):
        parent_list.append(MakeRandomStr(len(Goal_Str)))
    generation = 0
    while(True):
        generation += 1
        # 世代交代の回数
        if generation > MaxCount:
            print('Objective Gene not Born')
            exit()
        check = update(parent_list, Goal_Str, generation)
        print('Generation{0}:{1}'.format(generation, parent_list[0]))
        parent_list = MakeBetterParents(check)


if __name__ == '__main__':
    main()
