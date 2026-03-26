#num1=(int(input('Ente first num')))
#num2=(int(input('Enter second num')))
#print(num1+num2)
#print(num1-num2)
#print(num1*num2)
#print(num1%num2)
#print(num1//num2)
#print(pow(num1, num2))
#type casting or conversion
#overall concept is to converting one datatype to# another data type

#area=int(input('Enter area of square : '))
#area=area**2
#print('Area of square is : ', area)

#def is_even_or_odd(num):        
#    if (num & 1 == 0):
 #       return "even"
#    else:
#        return "odd"

# Example usage
#number = int(input("Enter a number: "))
#print(f"The number {number} is {is_even_or_odd(number)}.")


#def swap_other_approach(a, b):
#    a, b = b, a
#    return a, b

#num1 = int(input("Enter first number: "))
#num2 = int(input("Enter second number: "))
#print(f"Original: num1 = {num1}, num2 = {num2}")
#a, b = num1, num2

#a, b = swap_other_approach(a, b)
#print(f"After swap with other approach: num1 = {a}, num2 = {b}")

def cigar_party(cigars, is_weekend):
    if is_weekend:
        return cigars >= 40
    else:
        return 40 <= cigars <= 60

cigars = int(input("Enter number of cigars: "))
is_weekend = input("Is it the weekend? (yes/no): ").lower() == 'yes'
print(f"Party successful: {cigar_party(cigars, is_weekend)}")



