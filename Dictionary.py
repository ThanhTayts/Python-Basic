'''
Dictionary: key - value
'''

# Create a new dictionary
my_dict = {"name":"thanhtay","age":22,"city":"quy nhon"}
print(my_dict)
# Khởi tạo dictionary bằng ham dict():
my_dict2 = dict(name = "thanhtay", age = 17)
print(my_dict2)
# Access items
content_in_dict = my_dict["city"]
print(content_in_dict)
# check for keys
# use if...in....
if "aka" in my_dict:
    print(my_dict['ake'])
else:
    print("key not exit")    
# use try except
try:
    print(my_dict["aka"])
except KeyError:
    print("no key found") 

# Add and change item
# add key
my_dict ["email"] = 'thanhtaycu@gmail.com'
print(my_dict)
# có thể ghi đè lên các giá trị
my_dict ["email"] = 'thanhtaycu@gmail.ak47'
print(my_dict)

# delete key-value
# del my_dict["city"]
# print(my_dict)

# pop # xoá key
# my_dict.pop("city")
# print(my_dict)

# popitem() xoá item cuối cùng
my_dict.popitem()
print(my_dict)


# loop dictionary
# using for loop
for key in my_dict: # in ra các key
    print(key)

for key in my_dict.keys():
    print(key)

for value in my_dict.values():
    print(value)  

for key,value in my_dict.items():
    print(f"{key} : {value}")


# Unique: Các phần tử là duy nhất
import unittest

def unique(str):
    char_set = {}
    for char in str:
        if char in char_set:
            return False
        char_set[char]  = True 
    return True    
        
class Test(unittest.TestCase):
    dataT = [('abcd'), ('432d'),('')]
    dataF = [('abcd'), ('4432d'),('ssd')]

    def test_unique(self):
        #check true
        for test_case in self.dataT:
            actualResult = unique(test_case)
            self.assertTrue(actualResult)
          #check false
        for test_case in self.dataF:
            actualResult = unique(test_case)
            self.assertFalse(actualResult)    

if __name__ == "__main__":
    unittest.main()