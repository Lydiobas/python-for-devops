# #variables
# boys = 15
# girls = 20
# print(boys + girls)


# fruits = 50
# vegetables = 30
# print("total:" , fruits - vegetables)

# houses = 10
# apartments = 20
# print("total:", houses * apartments)


# a = 10
# b = 5
# print("total:", a / b)

def main():
    print("Hello World!")
main()

def add():
	Total = 10 + 20
	print(Total)
add()

def sub():
	Total = 10 - 20
	print(Total)
sub()

#To make the function dynamic,you can pass inputs to the function and return the output
def add(a, b):
	Total = a + b
	return Total
print(add(10, 20))

def sub(a, b):
	Total = a - b
	return Total
print(sub(10, 20))

def mul(a, b):
	Total = a * b
	return Total
print(mul(10, 20))

