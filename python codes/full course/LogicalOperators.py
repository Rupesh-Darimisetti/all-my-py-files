has_high_income=True
has_good_credit=True
if has_high_income and has_good_credit:
    print("1:Eligible for loan\n")

has_high_income=False
has_good_credit=True
if has_high_income and has_good_credit:
    print("2:Eligible for loan\n")

has_high_income=False
has_good_credit=True
if has_high_income or has_good_credit:
    print("3:Eligible for loan\n")


has_high_income=True
has_good_credit=False
if has_high_income or has_good_credit:
    print("4:Eligible for loan\n")

has_high_income=False
has_good_credit=False
if has_high_income or has_good_credit:
    print("5:Eligible for loan\n")

has_good_credit=True
has_criminal_record=False
if has_good _credit and not has_criminal_record:
    print("6:Eligible for loan\n")

has_good_credit=True
has_criminal_record=True
if has_good_credit and not has_criminal_record:
    print("7:Eligible for loan\n")
