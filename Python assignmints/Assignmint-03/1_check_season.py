def check_season(m):
    if m in("september","october","november"):
        print("The season: Autumn")
    elif m in("december","january","february"):
        print("The season: Winter")
    elif m in("march","april","may"):
        print("The season: Spring")
    else:
        print("The season: Summer")
    

month=input("Eneter a month: ")
check_season(month.lower())
