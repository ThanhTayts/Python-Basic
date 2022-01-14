# Required Parameter & Default Parameter
# def print_name(name): # parameter : tham số
#     print(name)

# def print_names(name,greeting): #Tham số bắt buộc
#     print(f"{name} : {greeting}")

# def print_namess(name,greeting="Welcom"): #Tham số mặc định
#     print(f"{name} : {greeting}")    

# def main():
#     # print_name("ThanhTayts") # argument : đối số
#     # print_names("thanhtay","ts")
#     print_namess("Thanhtay")

# if __name__ == "__main__":
#     main()

#Argument    
# def codexplore(a,b,c):
#     print(a,b,c)

# def main():
#     #Positional Argument : đối số thêo vị trí
#     codexplore(1,2,3)
#     #Keyword Argument : đối số theo từ khoá
#     codexplore(a=1,c="Hello",b=2)

# if __name__ == "__main__":
#     main()

# Variable-lenght Parameter : tham số với độ dài thay đổi
# *args và **kwargs
# *args : truyền vào 1 list
def VariablelenghtArgExample(a,b, *args):
    print(a,b)
    for arg in args:
        print(arg)
#**kwargs : truyền vào dictionary
def VariablelenghtArgExamples(a,b, *args,**kwargs):
    print(a,b)
    for arg in args:
        print(arg)   
    for key,value in kwargs.items():
        print(f"{key} : {value}")         

def main():
    VariablelenghtArgExamples("a","b","Hello",1,2,3, size ="S", age=17)
# khi gọi hàm *args hay **kwargs có hay không cũng được    

if __name__ == "__main__":
    main()