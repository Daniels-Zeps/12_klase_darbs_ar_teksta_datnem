# 1. Izveidot map "teksta_apstrade" un visus uzdevumus veikt tajā

# 2. Izveidot failu, kas satur Lore Ipsum pirmos 20 paragrāfus "data.txt"
# 3. Nokopēt failu "shows.txt"

# 4. Darbs ar failu "data.txt"
# ---- Noteikt cik simbolu ir tekstā:
#      ---- with open("data.txt", "r", encoding="utf-8") as file
#      ---- file.read() - nolasa saturu no faila
#      ---- len() - saraksta/teksta garums
# ---- Izvadīt visas teksta rindas, kas ir failā
#      ---- file.readline() - nolasa vienu rindu failā
#      ---- while True: - cikls nolasīsāna
#      ---- if line: breal - pārtrauc lasīšanu, ja "line" ir None vērtība
#      vai
#      ---- split("\n") - sadala tekstu par rindstarpām
#      ---- for line in text.split("\n"):
# ---- Saskaitīt, cik Vārdu ir failā
#      ---- split(" ")
# ---- Saskaitīt, cik lielo burtu ir tekstā
#      ---- isupper() - nosaka vai simbols ir lielais burts
# ---- Saskaitīt, cik vārdi beidzas ar patskani (vowl - "aeiou")
#      ---- letter in "aeiou" - nosaka vai burt ir patskanis

# 5. Darbs ar failu "shows.txt"
# ---- Noteikt, cik reizes teksts "the"/"The" parādās tekstā
#      ---- lower() - pārveido visu tekstu uz mazajiem burtiem
#      ---- upper() - pārveido visu tekstu uz lielajiem burtiem
# ---- Ciparu saskaitīšana (for cikls)
#      ---- Var izmantot try: except: un float
#      vai
#      ---- isdigit() - nosaka vai teksts ir skaitlis
# ---- Skaskaitīt ciparus, kas ir lielāki par 5
# ---- Saskaitīt cik ieraksti ir "Movie" datu tipa
#      ---- text[index] - atļauj piekļūt kādam elementam no split(" ") saraksta
# ---- Saskaitīt cik ieraksti ir pirms 2000 gada
#      ---- string[start:end] - atļauj izgriezt fragmentu no teksta
# ---- Aizstāt " ar '
#      ---- replace("\"", "\'") - atļauj aizvietot simbolu tekstā
# ++++ Skaskaitīt skaitļus tekstā
#      ---- replace("-", " ")
#      ---- split(" ")
#      ---- split(" ")

