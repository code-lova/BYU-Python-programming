#COMBINING ALL EXAMPLES ON WEEK 5 CONDITIONAL STATEMENT
country = input("What coutry are you from: ")
tax = 0
if country.lower() == "canada":
    province = input("What province are you from: ")
    if province.lower() in("alberta", "yukon", "nunavut"):
        tax = .05
    elif province.lower() == "ontario":
        tax = 0.13
    else:
        tax = 0.15
    print(tax)
else:
    print("You are to pay " + str(tax) + " taxes")