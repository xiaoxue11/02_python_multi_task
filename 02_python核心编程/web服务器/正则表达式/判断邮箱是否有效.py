import re


def main():
    email_address = input('please input email address: ')
    ret = re.match(r'[a-zA-Z0-9_]{4,20}@163\.com$', email_address)
    if ret:
        print('{} is valid---'.format(email_address))
    else:
        print('{} is nonvalid---'.format(email_address))


if __name__ == '__main__':
    main()
