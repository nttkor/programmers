import string

def validate_password(password):

    # 문자열이 8자 이상인지 확인합니다.
    is_long = False
    if len(password) >= 8:
        is_long = True
    
    # 문자열에 숫자가 포함되어 있는지 확인합니다.
    includes_digit = False
    for digit in password:
        if digit in string.digits:
            includes_digit = True
            break
    
    # 문자열에 알파벳 대문자가 포함되어 있는지 확인합니다.
    includes_upper = password
    for char in password:
        if char in string.ascii_uppercase:
            includes_upper = True
            break
    
    # 문자열에 알파벳 소문자가 포함되어 있는지 확인합니다.
    includes_lower = False
    for char in password:
        if char in string.ascii_lowercase:
            includes_lower = True
    
    return is_long and includes_digit and includes_upper and  includes_lower


def validate_birthday(birthday):
    
    year, month, day = birthday
    
    # 연도가 조건에 맞는지 확인하고, 아니면 False를 return 합니다.
    if 1900 > year  or year > 2018:
        return False
    if not (1 <= month <= 12):
        return False
    # 달이 31일까지 있는 경우, 날짜가 유효한지 체크합니다.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        if not(1 <= day <= 31):
            return False
    
    # 달이 30일까지 있는 경우, 날짜가 유효한지 체크합니다.
    elif month in [4,6,9,11]:
        if not(1 <= day <= 30):
            return False
    
    # 2월인 경우, 날짜가 유효한지 체크합니다.
    else:
        febday = 28
        if is_leap_year(year) == True:
            febday = 29
        if not(1 <= day <= febday):
            return False
        
    return True
    


def is_leap_year(year):
    
    # 조건 1
    if year % 400 == 0:
        return True
    
    # 조건 2
    elif year % 100 == 0:
        return False
    
    # 조건 3
    elif year % 4 == 0:
        return True
    
    # 모두 아닌 경우
    else:
        return False


# 여러분의 코드를 직접 테스트해 보세요.
is_password_valid = validate_password("Q1q!!!!!")
print(is_password_valid)

is_birthday_valid = validate_birthday((1900, 2, 29))
print(is_birthday_valid)

is_2000_leap = is_leap_year(2000)
print(is_2000_leap)
