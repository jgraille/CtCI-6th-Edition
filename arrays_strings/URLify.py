
def URLify(sentence,n):
    i = n - 1
    sentence = list(sentence)
    while i>=0 and sentence[i] == ' ':
        i -= 1
    l = []
    while i >= 0:
        a = sentence[i]
        if sentence[i] == ' ' and sentence[i - 1] == ' ':
            l.append(i)
        if sentence[i] == ' ' and sentence[i-1] != ' ':
            sentence[i] = '%20'
        i -= 1
    res = [x for i,x in enumerate(sentence) if i not in l]
    return (''.join(res))


def main():
    sentences = ["link   "," link ","huge   space    ","huge space",""]
    for i in sentences:
        print(URLify(i,len(i)))
if __name__ == '__main__':
    main()