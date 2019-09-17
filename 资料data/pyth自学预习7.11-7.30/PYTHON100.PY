# print ('Hello Python world!\n')
# print ('*' * 10)
# for i in range(5):
#     print ('*        *')
# print ('*' * 10)
# print ('*\n' * 6)

# a = 176
# b = 219
# print (chr(b),chr(a),chr(a),chr(a),chr(b))
# print (chr(a),chr(b),chr(a),chr(b),chr(a))
# print (chr(a),chr(a),chr(b),chr(a),chr(a))
# print (chr(a),chr(b),chr(a),chr(b),chr(a))
# print (chr(b),chr(a),chr(a),chr(a),chr(b))

print('\n'.join([''.join([('Love'[(x-y)%4]if((x*0.05)**2+(y*0.1)**2-1)\
    **3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-30,30)])for y \
    in range(15,-15,-1)]))
