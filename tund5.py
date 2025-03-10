import random


sõne="Programmeerimine"
print(sõne)
sõne_list = list(sõne)
print(sõne_list)
sõne_list.reverse()
print(sõne_list)

if ("P" in sõne_list):
    print(sõne_list.index("P"))
print(len(sõne_list))
print(len(sõne))
sõne_list.remove("m")
print(sõne_list)
mCount = sõne_list.count("m")
for i in range(mCount):
    sõne_list.remove('m')
print(sõne_list)


tähed = random.randint(1, 6)
for i in range(tähed):
    while True:
        try:
            t = input("Sisesta täht: ")
            if (t.isalpha()): 
                break
            print("Ainult tähed lubatudwl")
        except:
            print("On vaja täht!")
    while True:
        try:
            index = int(input("Sisesta index: "))
            if (index > len(sõne_list)):
                print("Index on liiga suur!")
                continue
            break
        except:
            print("On vaja index!")

    sõne_list.insert(index, t)

print(sõne_list)
sõne_list.sort(reverse=True)
print(sõne_list)
