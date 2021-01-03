n = int(input())

peanut = 10
chicken = 40
protein = 250

protein_c = n // protein
chicken_c = n % protein // chicken
peanut_c = n % protein % chicken // peanut

if n % protein % chicken % peanut != 0:
    print(-1)
else:
    print(protein_c, chicken_c, peanut_c)