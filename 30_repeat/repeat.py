def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    res = "";
    if type(num) == int:
        if num == 0:
            return '';
        elif num > 0:
            for n in range(1,num+1):
                res = res + phrase;
            return res;
        else:
            return None;
    else:
        return None;
       
