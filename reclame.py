from algemene_functies import mijn_functie_2




def aanbieding_1(smaak,prijs,korting):
    return(f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {(1-korting)*prijs} euro.")

totaal = aanbieding_1("aardbei",4,0.1)
print(totaal)



def inkomsten_totaal(inkomsten,btw):
    return(f"Het totaal van alle inkomsten van deze week is {inkomsten} euro, waarover {inkomsten*btw} euro btw betaald dient te worden")

totaal = inkomsten_totaal(220+430+125+160+205+90+345,0.09)
print(totaal)



def laag_en_hoog(mijn_lijst):
    return max(mijn_lijst), min(mijn_lijst)

mijn_lijst = [220, 430, 125, 160, 205, 90, 345]
totaal = laag_en_hoog(mijn_lijst)
print(totaal)



def gemiddelde(mijn_lijst):
    return (f"De gemiddelde inkomsten deze week zijn {mijn_lijst} euro.")

totaal= gemiddelde((220+430+125+160+205+90+345)/7)
print(totaal)



def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst) 

invoer_lijst = [10, 5, 3, 4, 1, 2, 9]
totaal = meervoudig(invoer_lijst)
print(totaal)

invoer_lijst_2 = [10, 5, 3, 4, 1, 2, 9]
def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2 (korte_lijst[0], korte_lijst [1])
    return uitvoer
totaal = combinatie(invoer_lijst_2)
print(totaal)