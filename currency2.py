"""

Money Exchange program
Takes in a currency and a value and changes it to a different currency 
"""

currency = raw_input("What is currency? (dollars/pesos) ") 
money = input("Enter your amount: ")

if currency == 'dollars':
    pesos = money *9
    print "your", money, "dollars are", euros, "pesos"
elif currency == 'pesos':
    dollars = money /9
    print "Your", money, "pesos are", dollars, "dollars"
else:
    print 'your currency is not supported'
