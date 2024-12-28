# print("hello world")
# userVAr=input("enter string:");y=50
# print(userVAr)
# print(f"y={y}")
# floatX=float(input("enter float value:"))
# print(f"float value is {floatX}")


# x=float(input("enter float value"))
# print(int(x))

# a,b,c=12,23,43
# print(a,b,c)

# print("addition",(a+b))
# print("subtraction",(a-b))
# print("multiplication",(a*b))
# print("div",(a/b))

# list_var.append(7)
# print(list_var)
# list_var.extend([99,88,76,53,20])
# print(list_var)
# list_var.insert(2,75)
# print(list_var)
# list_var.remove(75)
# print(list_var)
# list_var.pop(2)
# print(list_var)
# list_var.sort()
# print(list_var)
# list_var.reverse()
# print(list_var)

# print(f"list::{list_var}")
# print(f"Index first element of list::{list_var[1]}")
# print(f"last index of list::{list_var[-1:-4:-1]}")
# print(f"last index of list::{list_var[1:3]}")

# list_var[1]=55
# list_var[2:6]=[55,44,95,66,77]
# print(list_var)


# print(f"set::{tuple_var}")
# print(f"Index first element of set::{tuple_var[1]}")
# print(f"last index of list::{tuple_var[-1]}")
# print(f"last index of list::{tuple_var[1:4]}")

# tuple_new=tuple_var+(12,34)
# print(tuple_new)


# list_var=[12,23,34,45,55]
# tuple_var=(12,3,24,42,3)
# set_var={12,23,34,42,2,23}
# dict_var={'a':12,'b':22,'c':32}


# print(f"Dictionary={dict_var}")
# dict_var["d"]=42
# print(f"Added new key value in dictionary={dict_var}")
# dict_var.pop('c')
# print(dict_var)
# keys=dict_var.keys()
# print(f"\nkeys are::{keys}\n")

# values=dict_var.values()
# print(f"values are::{values}\n")
# items=dict_var.items()
# print(f"items are::{items}\n")

# print(f"type of set ::{type(set_var)}")
# set_var.add(5)
# print(set_var)
# set_var.discard(42)
# print(set_var)
# union_set=set_var.union({12,79,3})
# print(union_set
# set_diff=set_var.difference(union_set)
# print(set_diff)

# a=10
# b=20

# print("\nArithmetic operation")
# print(f"{a}+{b}={a+b}")
# print(f"{a}-{b}={a-b}")
# print(f"{a}X{b}={a*b}")
# print(f"{a}/{b}={a/b}")
# print(f"{a}%{b}={a%b}")

# print("\ncomparison ")
# print(f"{a} == {b} : {a==b}")
# print(f"{a} != {b} : {a!=b}")
# print(f"{a} > {b} : {a>b}")
# print(f"{a} < {b} : {a<b}")
# print(f"{a} >= {b} : {a>=b}")
# print(f"{a} <= {b} : {a<=b}")

# print("\nLogical") 
# a, b = True, False
# print(f"{a} and {b} : {a and b}")
# print(f"{a} or {b} : {a or b}")
# print(f"not {a} : {not b}")

# a=5
# b=a<<2
# print(b)

# user_input="192.168.1.1"
# a=user_input.split(".")
# ipv4=".".join(f"{int(number):08b}" for number in a)
# print(ipv4)






# def split_string(input_string,s):
#     result = []
#     current_substring = ''
    
#     for char in input_string:
#         if char == s:
#             if current_substring:
#                 result.append(current_substring)
#                 current_substring = ''
#         else:
#             current_substring += char
    
#     if current_substring:
#         result.append(current_substring)
    
#     return result

# input_string ="192.168.1.1"
# s = "."
# result = split_string(input_string,s)
# print(result)

# for char in input_string :


# import calendar as cal

# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))

# print(f"\nCalendar for {cal.month_name[month]} {year}:")
# print(cal.month(year, month))

# print(f"\nEntire Calendar for year {year}:")
# print(cal.calendar(year))

# num=0
# if num>0:
#     print("number {num} is positive\n")
# elif num<0:
#     print("number{num} is negative\n")
# else:
#     print("number {num} is zero or not valid input\n")

# for  i in range(1,5):
#     print(i)


# count=1
# while count<=5:
#     print(count)
#     count+=count

# count=5
# while count>=0:
#     print(count)
#     count=count-1


# for i in range(1,10):
#     if i==5:
#         print("Break applying at",i)
#         break
#     print(f"loop iterate: {i}")


# def add(x,y):
#     return (x+y)
# print("result is ::",add(4,4))



