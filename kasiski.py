import re

def gcd(*args):
    if len(args) == 1:
        return args[0]
    elif len(args) == 2:
        x, y = args
        if x<y:
            return gcd(y,x)
        elif y==0:
            return x
        else:
            return gcd(y,x%y)
    else:
        return gcd(gcd(args[0],args[1]),*args[2:])

def kasiski(**kwargs):
    for key, value in kwargs.items():
        diff = [value[i]-value[i-1] for i in range(1,len(value))]
        kwargs[key] = gcd(*diff)
    return kwargs

def main():
    with open('Chiper Text.txt', 'r') as f:
        chiper = f.read()

    # Here I use 4-grams
    pattern = re.compile(r'(?=(\w{4}))')

    matches = pattern.finditer(chiper)

    trigrams = {match.group(1) for match in matches}

    index = {trigram : [match.span()[0] for match in re.finditer(r'(?=({}))'.format(trigram), chiper)] for trigram in trigrams}

    index = dict(filter(lambda x: len(x[1])>1, index.items()))

    print(f'dict of delta is {kasiski(**index)}\n')
    print(f'the keyword length is {gcd(*kasiski(**index).values())}')

if __name__ == '__main__':
    main()