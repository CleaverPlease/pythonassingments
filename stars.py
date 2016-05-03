#part one
def draw_star(xlist):

    for item in xlist:
        print item
        print '*'*item
draw_star([1,7,5,3])

#part two
def draw_star(xlist):

    for item in xlist:
        if (isinstance(item,int)):
            print "*"*item
        # elif (isinstance(item,str)):
        else:
            print item[0]*len(item)

draw_star([1,"dog",3,])
