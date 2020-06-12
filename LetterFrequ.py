import sys


def char_counts(string1):
    dict = {'a': 0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,
             'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for letter in string1:
        letter = letter.lower()
        if letter in dict:
            dict[letter] += 1/(len(string1))
    return dict

title1 = sys.argv[1]

text1 = open(title1, "r", encoding="utf8").read()

cfreqs = char_counts(text1)

import operator
cfreqs = sorted(cfreqs.items(), key=operator.itemgetter(1))

for i in cfreqs:
    len = int(i[1]*1000)
    print(i[0]," : " ,'{:.3f}%'.format(i[1]*100), len*"|")
