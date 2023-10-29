a = float(input("Sisesta A: "))
b = float(input("Sisesta B: "))
c = float(input("Sisesta C: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Sellist kolmanurka pole olemas!")
elif a == b and b==c:
    print("Võrdkülgne kolmnurk")
elif a == b and b != c or a == c and a != b or b == c and b != a:
    print("Võrdhaarne")
else:
    print("Erikülgne kolmnurk")