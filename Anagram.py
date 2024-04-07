def anagram(string1,string2):
    s1=sorted(string1)
    s2=sorted(string2)
    if(s1==s2):
        print("anagram")
    else:
        print("not")
anagram("wdas","d2aw")
