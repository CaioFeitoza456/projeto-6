
import decorator
import join_function
import count_function
from sum_function_default import sum_function


def try_switch_to_float(value):
    try:
        return float(value)
       
    except ValueError:
        return None


print("""

1. Flipping texts
2. Joining lists of values
3. generator with count function
4. Packing and Unpacking a list
5. Function with default values
6. Quit

""")

while True:
    option_function = input("Type here: ")
    
    if option_function == "1":
        
        string = input("Type something: ")
        print("Flipping the string...")
        
        invert_strings = decorator.decorator()
        print(invert_strings(string))
    
    
    elif option_function == "2":
        
        list_a = []
        list_b = []
        
        for i in range(3):
            value = input("Type something for the list_a: ")
            list_a.append(value)
        
        print()
        
        for i in range(3):
            value = input("Type something for the list_b: ")
            list_b.append(value)
            
        join_lists = join_function.join_lists(
            list_a, list_b
        )
        print()
        
        print("The new list is:")
        print(join_lists)
        print()

    
    elif option_function == "3":
        limit = input("Enter the limit number: ")
        
        limit = try_switch_to_float(limit)
        result = count_function.generator_with_count(limit)
        print(result)
    
    
    elif option_function == "4":
        
        list_of_values = list()
        for i in range(0, 3):
            value_to_pack = input("Type something: ")
            list_of_values.append(value_to_pack)
        
        print()
        print("Your list is:")
        print(*list_of_values, sep="\n")
        print()


    elif option_function == "5":
        x = input("x: ")
        x = try_switch_to_float(x)
        
        y = input("y: ")
        y = try_switch_to_float(y)
        
        if isinstance(x, float) and isinstance(y, float):
            result = sum_function(x, y)
            print(f"You result is: {result}")
        
        else:
            result = sum_function()
            print(f"You result is: {result}")
    
    
    elif option_function == "6":
        break
    
            
    else:
        print("Please, enter a valid option.")
        continue
