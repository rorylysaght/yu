#stringstuff.py
import pprint
#oldstr = "the quick brown fox jumps over the lazy black dog"
oldstr = "O you possessed of sturdy intellects, observe the teaching that is hidden here beneath the veil of verses so obscure"
count = {}
newstr = oldstr.replace(' ','')
for character in newstr:
	count.setdefault(character, 0)
	count[character] = count[character] +1
pprint.pprint(count)
print(len(oldstr))
print(len(newstr))