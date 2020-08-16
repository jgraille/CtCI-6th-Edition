def climbingLeaderBoard(scores, alice):
    scores = list(set(scores))
    scores.sort(reverse = True)
    i = 0
    res = []
    while(i < len(alice)):
            j = 0
            while((j < len(scores)) and (scores[j] > alice[i])):
                    j += 1
            res.append(j + 1)
            i += 1
    return (res)


if __name__ == '__main__':
    scores = [100,90,90,80,75,60]
    alice = [55,65,77,90, 102]
    res = climbingLeaderBoard(scores, alice)
    print(res)


