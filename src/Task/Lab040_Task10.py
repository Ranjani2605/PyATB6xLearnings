

def check_status_code(status_code):
    if status_code == 200:
        return 'PASS'
    elif status_code == 400 or status_code == 500:
        return 'FAIL'
    else:
        return 'UNKNOWN'


print(check_status_code(200))
print(check_status_code(400))
print(check_status_code(0))


