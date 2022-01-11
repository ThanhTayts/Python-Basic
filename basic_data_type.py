import math
#Basic data Types:
''' 
Cac kieu du lieu co ban trong python : bool, None, int, float, complex, str
'''

# Topic 0 bool & None
# bool True(1) False(0)
# var_bool = True
# # print(type(var_bool))
# a = 4+True
# print(a)
# b = False
# if b == 0:
#     print("B is zero")
# else:
#     print("B not is zero")    
# # None phan tu 0, gia tr rong
# var_none = None
# print(type(var_none))
# # None dung trong if else se bang False
# email = None
# if email:
#     print(f"Email address {email}")
# else:
#     print(f"email is empty or {email}")    
   

# Topic 1 Int & Float & Complex
# print(type(1)) # int
# print(type(-10.67))# float
# print(type(complex(2,5)))# complex
# print(4E2) #4*10^2
# c = complex(2,5)
# print(f"Real is {c.real}; Imag is {c.imag}")

# Topic 2 Arithmetic: cac phep toan : +, -, *, **, /, //, %.
# print(5+2) 
# print(5-2)
# print(5*2)
# print(5/2) # chia 
# print(5//2) # chia lấy nguyên
# print(5%2) # chia lấy dư
# print(5**5) # luỹ thừa

#Topic 3 Toán tử gán : =, +=, *=, /=, //=, %=, **=

#Topic 4 Basic function (Hàm cơ bản đã được xây dựng sẵn)
print(pow(5,5)) # ham mu
print(abs(-5)) # tri tuyet doi
print(round(5.5)) # ham lam tron len 
print(round(5.468, 2)) # lam tron 2 chu so thap phan
print(bin(512)) # so nhi phan
print(hex(512)) # so hex
print(oct(512)) # so oct

# Topic 5 Toan tu so sanh
# ==, >=, <=, >, <, !=, is, isnot

# Topic 6 Toan tu Logic
# and, or, not, in, not