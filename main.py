# Scenario
# The previous code needs to be improved. It's okay, but it has to be better.

# Your task is to make some amendments, which generate the following results:

# the output histogram will be sorted based on the characters' frequency (the bigger counter should be presented first)
# the histogram should be sent to a file with the same name as the input one, but with the suffix '.hist' (it should be concatenated to the original name)
# Assuming that the input file contains just one line filled with:

# cBabAa
# samplefile.txt

# the expected output should look as follows:

# a -> 3
# b -> 2
# c -> 1
# output

# Tip: Use a lambda to change the sort order.

###############################################################################################################

try:
    file = open(input("Enter the file name: "),"rt",encoding="UTF-8")
    r = file.read(1)
    dic = {}
    while r:
        if r.isalpha():
            c = r.lower()
            dic[c] = dic.get(c,0)+1
        r = file.read(1)
        
        
        
except IOError as e:
    print(e)

dic = dict(sorted(dic.items()))

for k,v in dic.items():
    print(f"{k} -> {v}")