a = 3
if a - 1 < 0: # False, tiếp tục
     print('a nhỏ hơn 1')
elif a - 2 < 0: # False, tiếp tục
     print('a nhỏ hơn 2')
elif a - 3 < 0: # False, tiếp tục
     print('a nhỏ hơn 3')
elif a - 4 < 0: # True, kết thúc
     print('a nhỏ hơn 4')
elif a - 5 < 0: 
    # Khối BIG đã kết thúc, dù đây là True nhưng không ý nghĩa
     print('a nhỏ hơn 5')
#OUTPUT: a nhỏ hơn 4