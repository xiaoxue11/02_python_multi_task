import re


def main():
    names = ['ages','_ages','2age','age1', 'a#123', 'age!']
    for name in names:
        ret = re.match(r"^[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret:
            print('{} is valid'.format(name))
        else:
            print('{} is nonvalid'.format(name))


if __name__ == '__main__':
    main()