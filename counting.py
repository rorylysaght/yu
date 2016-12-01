# Prog to ask user for name and number, then count by 2's
print ('####### Counting by 2s #######')
       
myName = raw_input('Your name? ').capitalize()

print("Hello " + myName)

endNum = raw_input('Enter a number: ')
endNum = int(endNum)  # convert string to integer

raw_input('Counting to ' + str(endNum) + ' - press Enter to start: ')

for x in range(1, endNum+1, 1):
	print (x)

print('Done!')