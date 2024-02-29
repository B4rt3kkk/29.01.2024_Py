liczba1=int(input("Podaj dodatnią liczbe1 dodatnią: "))
liczba2=int(input("Podaj dodatnią liczbe2 dodatnią: "))

if liczba1 > liczba2:
    print(f"Liczba {liczba2} jest mniejsza od {liczba1} i mieści się w niej", liczba1//liczba2, "razy")
else:
    if liczba1 < liczba2:
     print(f"Liczba {liczba1} jest mniejsza od {liczba2} i mieści się w niej", liczba2//liczba1, "razy")
