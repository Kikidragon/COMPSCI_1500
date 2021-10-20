def seconds_to_jiffies(user_seconds):
    jif = user_seconds * 100
    return jif

if __name__ == '__main__':
    sec = int(input())
    print('{:.2f}'.format(seconds_to_jiffies(sec)))