def check(s):
    if len(s) < 3:
        return False
    if s[-3:] != '.py':
        return False
    for i in s:
        if (ord(i) < ord('a') or ord(i) > ord('z')) and ord(i) != ord('.') and ord(i) != ord('_'):
            return False
    return True

s = input().lower()
if check(s):
    print("yes")
else:
    print("no")
