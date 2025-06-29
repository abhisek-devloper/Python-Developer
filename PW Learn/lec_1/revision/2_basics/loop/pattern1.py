n = 5

for r in range(1,n+1):
    if r<=n:
        for c in range(1,n+1):
            if c<=r:
                print("* ", end='')
        print("\n")
