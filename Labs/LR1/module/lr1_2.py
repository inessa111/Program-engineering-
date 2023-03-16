import re
# Написать регулярное выражение, определяющее является ли данная строка 
#строкой "abcdefghijklmnopqrstuv18340" или нет.
def stringing(a):
    if not a :
        return False
    str='abcdefghijklmnopqrstuv18340'
    result = re.findall(a, str)    
    if result==str.split():
        return True
    else:
        return False
  