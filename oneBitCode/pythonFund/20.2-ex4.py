number = int(input("Tabuade de: "))
begin = int(input("De: "))
end = int(input("Até: "))

x = begin

while x <= end:
    print(f"Tabuada de {number} x {x} = {number * x}")
    x += 1