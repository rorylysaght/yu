#factorials
total = 0
s = 0
#s = raw_input('enter a number or "done": ')

while s != 'done':
    num = int(s)
    total = total + num
    s = raw_input('enter a number or "done": ')

print ('the sum is ' + str(total))