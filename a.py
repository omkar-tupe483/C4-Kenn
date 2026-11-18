age = 20
name = "Kenn"

if age >= 18:
	print("Adult")
else:
	print("Minor")

for number in range(1, 6):
	print(number)

def greet(person):
	return f"Hello, {person}"

print(greet(name))
