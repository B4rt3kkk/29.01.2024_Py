rok = int(input("Podaj bierzący rok: "))
miesiac = int(input("Podaj bierzący miesiac: "))
dataUrodzenia = int(input("Podaj datę twojego urodzenia: "))
terazRok = 2024
terazMiesiac = 2

if rok + 18 < 2024:
    print("Użytkowniku nie jesteś pełnoletni wypier...")
elif terazMiesiac > miesiac:
     print("Użytkowniku jesteś pełnoletni Brawo")
else:
    print("Użytkowniku jesteś pełnoletni Brawo")
