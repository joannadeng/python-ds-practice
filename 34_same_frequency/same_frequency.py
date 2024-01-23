def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    str1 = str(num1);
    list1 = list(str1);
    list1.sort();

    str2 = str(num2);
    list2 = list(str2);
    list2.sort();

    return list1 == list2;
