

print("Program generujacy kartke urodzinowa")
imie = input("Podaj imie odbiorcy: ")
rok_urodzenia = int(input("Podaj rok urodzennia odbiorcy: "))
wiek = (2025 - rok_urodzenia)
spersonalizowaną_wiadomość = input("Zloz swoje zyczenia z okazi Urodzin {}: ".format(imie))
imie_nadawcy = input("Podaj swoje imie: ")
SZABLON = f"""
{imie} wszystkiego najlepszego z okazji {wiek} urodzin!
{spersonalizowaną_wiadomość}
{imie_nadawcy}
"""
print(SZABLON)