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

