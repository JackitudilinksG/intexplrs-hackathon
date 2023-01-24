play = True

road_dict = {"I_ln":1, "II_ln":2, "IV_ln":4, "rb_rd":0.5}
eis = []

while play == True:
    choice = str(input("choose a road? (Y/N): "))
    if choice == "N":
        play = False
    elif choice == "Y":
        road = str(input("road type: "))
        cps = road_dict.get(road)
        ei = 1/cps
        eis.append(ei)
    else:
        print("invalid option")

print(eis)
