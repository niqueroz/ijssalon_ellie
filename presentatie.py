def presenteer(mijn_dictionary,totaal):
    for k, v in mijn_dictionary.items():
        print(f"{k} : {v} euro")
    print("=================================")
    print(f"totaal : {totaal} euro")

mijn_dict = {'vis' : 10, 'vlees' : 25, 'overig' : 15}
totaal = 50
presenteer(mijn_dict,totaal)  