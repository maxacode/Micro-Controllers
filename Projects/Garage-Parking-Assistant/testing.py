with open("config.ini", "r") as data:
    dataDict = data.read().split()
    
    justrightcm= dataDict[0].split("=", 1)[1]
    tofarcm= dataDict[1].split("=", 1)[1]
    toclosecm= dataDict[2].split("=", 1)[1]

    print(justrightcm, tofarcm, toclosecm) 

