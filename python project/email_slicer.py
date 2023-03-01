email = input("Please enter your email: ").strip()
username = email[:email.index('@')]
domain = email[email.index('@') + 1:]
if("@gmail.com" in email):
    print("Hey " + username +", I see your email is registered with Google. That's cool.")
else:
    print("Hey " + username +", looks like you've got your own custom setup at " + domain + ". Impressive!")