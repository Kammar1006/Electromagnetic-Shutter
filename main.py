from only_longest import longest
from all_same import same

if __name__ == "__main__":
    flag = int(input("Lambda/10 tylko dla najdłuższego wymiaru liniowego (1), lambda/10 dla każdej odlełości (2)"))
    if(flag == 1):
        longest()
    elif(flag == 2):
        same()