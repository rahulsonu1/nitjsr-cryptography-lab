def miller_rabin_test(n, bases):
    
    d = n - 1
    r = 0
    while d % 2 == 0:
        d //= 2
        r += 1
    print(f"(a) n - 1 = 2^{r} * {d}")

   
    for a in bases:
        print(f"\nBase a = {a}")
        x = pow(a, d, n)
        print(f"a^d mod n = {x}")
        
        if x == 1 or x == n - 1:
            print("Passes this round (trivial).")
            continue
        
        for i in range(1, r):
            x = pow(x, 2, n)
            print(f"Square {i}: x = {x}")
            if x == n - 1:
                print("Passes this round.")
                break
        else:
            print("Fails for this base → Composite")
            return False  

    print("\n Passes all bases Probable prime")
    return True  



n = 1000003
bases = [2, 3, 5, 7]
result = miller_rabin_test(n, bases)

if result:
    print(f"\nConclusion: {n} is a probable prime.")
else:
    print(f"\nConclusion: {n} is composite.")