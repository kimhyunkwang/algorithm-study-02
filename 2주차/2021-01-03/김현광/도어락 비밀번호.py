cheshire, elice = input().split()

new_cheshire = cheshire[3] + cheshire[2] + cheshire[1] + cheshire[0]
new_elice = elice[3] + elice[2] + elice[1] + elice[0]

password = int(new_cheshire) + int(new_elice)
print(password)