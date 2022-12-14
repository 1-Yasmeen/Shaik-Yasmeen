def test(str):
   return str[len(str)-2] in str[len(str)-1] and str[len(str)-2]!=str[len(str)-1]
str=["a","abb","sfs","oo","de","sfde"]
print(str)
print(test(str))