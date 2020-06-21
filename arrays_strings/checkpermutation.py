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
        return True


def main():
    string1 = "issou"
    string2 = "uossi"
    print(checkpermutation_1(string1,string2))
    

if __name__ == "__main__":
    main()