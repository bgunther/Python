#99 bottles
#Brian Gunther
#December 10 2015

#GOALCreate a program that prints out every line to the song "99 bottles of beer on the wall."

bottle = 99
b2 = bottle -1

while bottle <= 99 and bottle > 0:
    if bottle > 1:
        print (bottle,"bottles of beer on the wall,",bottle," bottles of beer, take one down pass it around there are",b2, "bottles's of beer on the wall.")
    else:
        print (bottle,"bottle of beer on the wall,",bottle," bottle of beer, take one down pass it around there are",b2, "bottles of beer on the wall.")
    bottle = bottle -1
    b2 = b2-1
