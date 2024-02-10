def is_win(card: dict) -> bool:
    """Check card is win."""

    for val in card.values():
        if sum(val) == 0:
            return True


    for i in range(len(card)):
        row = 0
        for val in card.values():
            row += val[i]
        if row == 0:
            return True

    main_diagonal = 0
    # i = 0
    # while i < len(card):
    #     for val in card.values():
    #         main_diagonal += val[i]
    #         i += 1
    #     if main_diagonal == 0:
    #         return True

    i = 0
    for val in card.values():
        main_diagonal += val[i]
        i+=1
    if main_diagonal == 0:
        return True


    diagonal = 0
    i = len(card) - 1
    while i >= 0:
        for val in card.values():
            diagonal += val[i]
        if diagonal == 0:
            return True
        i -= 1

