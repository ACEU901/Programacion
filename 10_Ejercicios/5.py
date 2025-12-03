for i in range(1, 100):
    if i % 4 == 0 and i % 6 == 0:
        print("TechNova")
    elif i % 4 == 0:
        print("Tech")
    elif i % 6 == 0:
        print("Nova")
    elif i % 7 == 0:
        print("Lucky")
    else:
        print(i)