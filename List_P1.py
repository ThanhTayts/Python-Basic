# list chua duoc nhieu kieu du lieu
#1 Creating a list

# list_1 = ["banana", "apple", "orangr", "cherry"]
# list_2 = [1,2,'a',False,None,'5']
# list_3 = list # tao 1 empty list
# print(list_2)

# # Access element
my_list = [1,2,2,2,'3',True]
# print(len(my_list)) # ham len tra ve do dai cua chuoi
# print(my_list[2])
# print(my_list.index('3')) # tra ve vi tri cua '3'
# print(my_list.count(2)) # tra ve so luong phan tu so 2 trong list
# for lop access each element
# for item in my_list:
#     print(item)

# enumerate function sẽ trả về item và index của mỗi item trong list
# for indexs,item in enumerate(my_list, start=1): # bắt đầu tại vị trí 1
#     print(f"{indexs} : {item}")


#Slicing [start : stop : step]    
# print(my_list[0:1]) # chỉ lấy giá trị đầu tiên
# print(my_list[1:]) 
# print(my_list[::2]) 
# print(my_list[::-1]) # đảo ngược list


# Operations & Useful Methods
### Add to List 
# new_list = my_list*2
# add_list = my_list + [100,'abc']
# print(add_list)

# Hàm Append dùng thêm 1 giá trị mới vào list
# print(my_list.append("6"))
# print(my_list)

# Hàm Extend dùng để thêm nhiều giá trị vào list
# print(my_list.extend([6,7,8,9,"ad"]))
# print(my_list)

# Hàm Insert dùng add 1 giá trị theo index
# print(my_list.insert(3,4)) #thêm giá trị 4 tại index = 3
# print(my_list)

### Remove from list
# Hàm pop dùng xoá phần tử cuối cùng
# print(my_list.pop()) #xoá phần tử cuối cùng
# print(my_list.pop(1)) #xoá phần tử có index =1 
# print(my_list)
# # Hàm remove dùng để xoá phần tử mong muôn
# my_list.remove(2) # xoá giá trị đầu tiên mà nó gặp
# print(my_list)
# # Hàm del dùng để xoá giá trị theo index
# del my_list[1]
# print(my_list)

### sorted list
num_list = [1,2,4,7,8,3,5,6]
#hàm sort sắp xếp các phần tử từ bé đến lớn
# num_list.sort()
# print(num_list)
# # nếu muôn sắp xếp từ lớn đến bé thì 
# num_list.sort(reverse=True) 
# print(num_list)

# # hàm reverse dùng đảo vị trí các phần tử trong list
# num_list.reverse()
# print(num_list)

# hàm reversed và sorted sẽ thực tạo trên 1 list mới


# UsedFul operations
# Hàm Max trả về giá trị max của lis
print(max(num_list)) # max
print(min(num_list)) # min
print(sum(num_list)) # sum