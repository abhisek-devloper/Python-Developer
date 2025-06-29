a = [1,2,3]

try:
    print(f"Second element {a[1]}")
    print(f"fourth element {a[3]}")   # when error this line go to except section
except:
    print("Error in found fourth element")
    
