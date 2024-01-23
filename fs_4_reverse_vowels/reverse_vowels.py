def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vol_lst = [];
    new_s = ""
    for ltr in s:
        if ltr in "aeiouAEIOU":
            vol_lst.append(ltr);
            new_s += ltr.replace(ltr,"=");
        else:
            new_s += ltr;
    vol_lst.reverse();
    
    res = ""
    idx = 0;
    for ltr in new_s:
        if ltr == "=":
            res += ltr.replace(ltr,vol_lst[idx]);
            idx += 1;
        else:
            res += ltr;
    return res;

    
    
