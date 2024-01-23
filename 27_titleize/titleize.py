def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower();
    lst = phrase.split(" ");
    lst2 = [];
    for word in lst:
        lst2.append(word.capitalize());
    return ' '.join(lst2);


