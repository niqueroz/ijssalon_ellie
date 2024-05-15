def decoreer(tekst=""):
    lengte = len(tekst) +4
    print ()
    print (lengte * "*")
    print (f"* {tekst} *")
    print(lengte * "*")
    print ()


def fooi_pp(bedrag,personen):
    bedrag_pp = bedrag/personen
    return f"Het bedrag per persoon is {bedrag_pp} euro"


def onderstreep(tekst=""):
    uit = []
    uit.append(tekst)
    uit.append(len(tekst) * "=")
    return uit 


def som (mijn_dictionary):
    mijn_som = 0
    mijn_values = mijn_dictionary.values()
    for e in mijn_values:
        mijn_som = mijn_som + e
    return mijn_som 
