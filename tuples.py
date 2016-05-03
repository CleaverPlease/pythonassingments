# seahawks = (12, 'beast', 24, 31, 'lob', 'legion of boom')
# # print seahawks[1]
# #
# # for item in seahawks:
# #     print item
# seahawks = seahawks[:2] + ("legion of Boom",12) +seahawks[5:]
# print seahawks
# a = 'seahawks'
# b = 'lob'
# c = 12
#
# (a,b,c) = (c,b,a)
#
# print (a,b,c)
# sea_hawks = (, 'kam', 'blitz', 12)
# hawks = (1,2,3,4,10)
# print max(sea_hawks)
# print max(hawks)
# num = [9,8,7,6]
# for index,item in enumerate(num):
#     print (str(index))+"="+(str(item))
# num = (9, 1, 8, 2, 7, 3)
# print sorted(num)

def get_circle_area(r):
    #Return (circumference, area) of a circle of radius r
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)
