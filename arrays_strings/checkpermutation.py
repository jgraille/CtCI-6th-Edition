def checkpermutation_1(string1,string2):
    if len(string1) != len(string2):
        return False
    else:
        i = 0
        j = len(string2) - 1
        while string1[i] == string2[j]:
            i += 1
            j -= 1
            if j < 0:
                break
        if i == len(string1):
            return True
        else:
            return False


def main():
    print(checkpermutation_1("issou","uossi"))
    print(checkpermutation_1("issou","uossa"))
    

if __name__ == "__main__":
    main()