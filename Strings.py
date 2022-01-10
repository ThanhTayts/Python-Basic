#String : Chuỗi kí tự
my_string = 'Hello W ord'
print(my_string , type(my_string))
my_name = "My name's Thanh Tay"
print(my_name , type(my_name))
# Escaping Backslash \
my_text = 'I\'am "Thanh Tay"'
print(my_text , type(my_text))
#Backslash
my_chanel = "Welcome to my channel \
i hope everybody happy"
print(my_chanel)

''' 
Access characters and substrings
'''
my_string = "Hello word"
print(my_string[0])
print(my_string[2:])
print(my_string[2:5])
print(my_string[:-1])
print(my_string[-1:])
print(my_string[1:-1:2]) # start , stop, step
print(my_string[::-1]) # dao chuoi

#Concatenate String using +
greeting ="Hello xin chao cac ban"
channel = "da den voi channel cua minh"
sentence = greeting+channel
print(sentence)
# Concatenate String using .join()
my_list = ['how', 'are', 'you', 'doing']
# setence = ' '.join(my_list)
setence = '+'.join(my_list)
print(setence)

'''
Basic & Useful Function
'''
#strip() xoa cac ki tu dang truoc va dang sau chuoi
print("   I am alone    ".strip())
print("**I am student**".strip('*'))
print("I am student".strip('I'))

# Split() # tach ra tung ki tu ra thanh 1 list
print('But life is good'.split())
print('But, life is good'.split(',')) # tach theo dau

# replace() # thay the ki tu
print('Help me'.replace("me","you"))

#startswith & endswith kiem tra cau co bat dau va ket thuc boi cac ki tu
my_string = 'i need the money'
print(my_string.startswith('i'))
print(my_string.endswith('money'))

#index() # kiem tra vi tri cua tu trong chuoi
print(my_string.index('e'))
#find()
print(my_string.find('e'))

#upper() & lower # viet hoa va viet thuong
print(my_string.upper())
print(my_string.lower())
# Title() in hoa tieu de
print(my_string.title())
# capitalize() in hoa chu cai dau tien
print(my_string.capitalize())
# count() dem so luong ki tu trong cau
print(my_string.count('e'))


#String Formatting : dinh dang bang %, format(), f-string
#%s
name = " Thanh Tay "
my_string = "%s Ts" %name
pi = 3.1459
my_string = "Variable is %.2f from %s" %(pi,name)
print(my_string)

# .format()
age = 17
height = 167.243435
my_string = "I am {} year old; {:.3f} cm".format(age,height)
print(my_string)

# F-String
age = 17
height = 167.243435
print(f"pi is {pi:.2f}, I am {age} year old and height {height} cm")