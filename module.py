# two_sum takes two integer arguments and returns the sum of the integers
def two_sum(a: int, b: int) -> int:
    tsum = a + b
    return tsum

    

# remove_vowels takes a string argument and return a string with all vowels removed
def remove_vowels(s: str) -> str:
    letters = ["a", "e", "i", "o", "u"]
    output = ""
    for char in s:
        if char.lower() not in letters:
            output += char
    return output

    


    


    


    

# factorial takes an integer argument and returns the factorial result of that integer
# factorial must use iteration and not the built-in factorial function
def factorial(num: int) -> int:
    output = 1
    for i in range(1,num + 1):
        output *= i
    return output


    
   
# listify takes a string argument and returns a list of characters in the string
def listify(s: str) -> list:
    output = []
    for char in s: 
        output.append(char)
       
    return output

   