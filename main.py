def table_multiply(min, max, n):
    if min <= max:
        for i in range(min, max+1):
            print(f"{i} X {n} = {i*n}")
    else:
        print("ERREUR : Le min est supérieur au Max, réessayez")
        return table_multiply(int(input("min : ")), int(input("max : ")), int(input("table : ")))

table_multiply(int(input("min : ")), int(input("max : ")), int(input("table : ")))
