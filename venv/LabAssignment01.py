f = open("txtfile.txt","r")
txt = f.read()
import re
keywords = []
identifiers = []
math_operators = []
logical_Operators = []
numerical_Values = []
others = []

a_list = re.split("\s",txt)
for x in a_list:
    if x.startswith("int") or x.startswith("float") or x.startswith("if") or x.startswith("else"):
        keywords.append(x)

    elif x.isdigit()or x.isdecimal() or x.endswith(".0"):
        numerical_Values.append(x)
    elif x.__contains__("+") or x.__contains__("-") or x.__contains__("-") or x.__contains__("=") or x.__contains__("*") or x.__contains__("/"):
        math_operators.append(x)
    elif x.__contains__(">") or x.__contains__("<") or x.__contains__("||") or x.__contains__("&&") :
        logical_Operators.append(x)
    elif x.__contains__("(") or x.__contains__(")") or x.__contains__("{") or x.__contains__("}") or x.__contains__(";") or x.__contains__(","):
        others.append(x)
    else:
        identifiers.append(x)

print("Keywords: ",set(keywords))
print("Identifiers: ",set(identifiers))
print("Math Operators: ",set(math_operators))
print("Logical Operators: ",set(logical_Operators))
print("Numberical Values: ",numerical_Values)
print("Others: ",sorted(list(set(others))))