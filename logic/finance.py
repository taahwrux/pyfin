def DailyHPR(beg, end):
    hpr = (end / beg) - 1
    return hpr * 100


if __name__ == "__main__":
    print DailyHPR(23.8, 25)

    
