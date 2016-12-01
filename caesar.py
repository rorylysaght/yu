# decode ascii encoded CAESAR CYPHER - written for Python 3
# to run in Python 2.7, replace 'input' with 'raw_input'
print('Enter the cypher you want to decode, and guess the key.')
strASCII = '' # this will hold all 256 ASCII chars

cyphertext = input('Cyphertext: ') # the encrypted string we want to decode
key = int(input('Key: ')) # hint: less than 10

for i in range(256):
    strASCII = strASCII + chr(i)  # create string with all 256 ASCII characters

for x in range(len(cyphertext)):
    m = strASCII.find(cyphertext[x])    # m = position of this char within strASCII
    print(cyphertext[x] + ' = ' + str(m) + ' = ' + chr(m-key))