import itertools #pip install more-itertools
#characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
characters = "abcdefghijklmnopqrstuvwxyz"
dic=open("pass1.txt","a")
##iterate all possible lengths of the password
#for leng in range(1, len(characters)+1):
    #print "lenght of password: ", leng
    ##create an iterator over the cartesian product of all possible permuations
    #it = itertools.product(characters, repeat=leng) #pass word length
it = itertools.product(characters, repeat=6)
for i in it:
    dic.write("".join(i))
dic.close()