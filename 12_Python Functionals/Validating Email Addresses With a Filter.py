def fun(email):
    count = 0
    try:
        username,websitename_extension=email.split("@")
        websitename,extention=websitename_extension.split(".")
    except ValueError:
        return False
    if username.replace("-","").replace("_","").isalnum() or username.isalnum():
        count = count+1
    if websitename.isalnum():
        count = count+1
    if len(extention) <= 3:
        count = count+1
    if count == 3:
        return True
    else:
        return False
def filter_mail(emails):
    return list(filter(fun, emails))
if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)