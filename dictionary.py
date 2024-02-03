meme_dict={
    "CRINGE":"coś dziwnego lub zawstydzajacego",
    "lol":"reakcja na cos zabawnego",
    "ROFL" : "odpowiedź na żart",
    "SHEESH" : "lekka dezaprobata",
    "CREEPY" : "straszny, złowieszczy"
    "AGGRO" : "stać się agresywnym/zły"
}
a=input("wpisz slowo, ktrorego nie rozumiesz:  ")
if a in meme_dict.keys():
    print(meme_dict[a])
else:
    print("nie mamy takiego wyrazu w slowaniku")
