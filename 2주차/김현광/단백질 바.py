n = int(input())
peanut = 10
chicken = 40
protein = 250

protein_count = n // protein
chicken_count = n % protein // chicken
peanut_count = n % protein % chicken // peanut

if n % protein % chicken % peanut != 0:
    print(-1)
else:
    print(protein_count, chicken_count, peanut_count)