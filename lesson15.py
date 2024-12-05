def print_mirrored_triangle(height):
    
    for i in range(1, height + 1):
        
        for j in range(height - i):
            print(" ", end="")
        
        for k in range(i):
            print("*", end="")
        
        print()

height = int(input("Enter the height of the mirrored right-angle triangle: "))


print_mirrored_triangle(height)
