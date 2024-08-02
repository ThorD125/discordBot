def randomPass(amount):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=amount))