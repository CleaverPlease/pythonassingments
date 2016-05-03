import random

heads = 0;
tails = 0;


for x in range(50):
    random_num = round(random.random())
    if (random_num == 1):
        side = "heads"
        heads += 1
        print 'attempt #:', x, "Throwing a coin...it's heads, got", heads, "head(s) so far and", tails, "tail(s) so far"

    elif (random_num == 0):
        side = "tails"
        tails += 1
        print 'attempt #:', x, "Throwing a coin...it's tails, got", heads, "head(s) so far and", tails, "tail(s) so far"
