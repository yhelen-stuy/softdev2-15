def min_pw(pw):
    upper = [c for c in pw if c.isupper()]
    lower = [c for c in pw if c.islower()]
    nums = [c for c in pw if c.isdigit()]
    return len(upper) > 0 and len(lower) > 0 and len(nums) > 0

print min_pw("password")
print min_pw("PaSsWoRd")
print min_pw("password123")
print min_pw("PASSWORD123")
print min_pw("PaSsWoRd123")

def rate_pw(pw):
    upper = [c for c in pw if c.isupper()]
    lower = [c for c in pw if c.islower()]
    nums = [c for c in pw if c.isdigit()]
    special = [c for c in pw if not c.isalnum()]

    rating = 1
    if len(upper) > 0 and len(lower) > 0:
        rating += 2

    rating += min(len(nums), 2)

    rating += min(len(special), 2)

    if len(upper) > 0 and len(lower) > 0 and len(nums) > 0 and len(special) > 0:
        rating += 2

    if len(pw) > 11:
        rating += 2

    return rating

print rate_pw("password") # 1
print rate_pw("Password") # 3
print rate_pw("Password1") # 4
print rate_pw("Password12") # 5
print rate_pw("Password1234") # 7
print rate_pw("Password=234") # 10
