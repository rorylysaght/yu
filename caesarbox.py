##caesarbox.py
#
#oldstr = 'o you possessed of sturdy intellects, observe the teaching that is hidden here beneath the veil of verses so obscure'
#
oldstr = input('Enter plaintext to be encyphered: ').lower()
newstr = oldstr.replace(' ','')
newstr = newstr.replace(',','')
boxstr = ''
square = 10
#print(newstr)
def genrow(x):
    boxstr =''
    for i in range(x,len(newstr),10): # gen row
        boxstr = boxstr + newstr[i]
    print(boxstr)
    #print('\n')

for x in range(0,10):
    genrow(x)    
'''
for x in range(0, 10):
        boxstr = boxstr + newstr[i]
#cyphertext = caesar(txt, 3)
#print(cyphertext)
'''