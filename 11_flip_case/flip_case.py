def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = []
    for lts in phrase:
        if lts.lower() == to_swap.lower():
            res.append(lts.swapcase());
        else:
            res.append(lts);
    return ''.join(res);
    