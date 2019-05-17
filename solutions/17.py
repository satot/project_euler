one_nine = '''
one
two
three
four
five
six
seven
eight
nine
'''
teens = '''
ten
eleven
twelve
thirteen
fourteen
fifteen
sixteen
seventeen
eighteen
nineteen
'''
decades = '''
twenty
thirty
forty
fifty
sixty
seventy
eighty
ninety
'''

hundred = "hundred"
thousand = "thousand"
_and = "and"

def count_below_99(prefix=""):
    total = 0
    p_len = len(prefix)
    # 1-9
    for l in one_nine.strip().split("\n"):
        total += (p_len + len(l))
    # 10-19
    for l in teens.strip().split("\n"):
        total += (p_len + len(l))
    # 20-99
    for l in decades.strip().split("\n"):
        total += (p_len + len(l))
        for m in one_nine.strip().split("\n"):
            total += (p_len + len(l) + len(m))
    return total

total = 0
total += count_below_99()
#100-999
for l in one_nine.strip().split("\n"):
    prefix = l + hundred
    total += len(prefix)
    total += count_below_99(prefix+_and)

print total + len("one" + thousand)
