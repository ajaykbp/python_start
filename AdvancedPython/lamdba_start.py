
def CelsiusToFahrenheit(temp):
    return (temp * 9/5 ) + 32

def FahrenheitToCelsius(temp):
    return (temp - 32) * 5/9

def main():
    ctemp = [0, 12, 34, 100]
    ftemp = [32, 65, 100, 212]
    print(list(map(CelsiusToFahrenheit, ctemp)))
    print(list(map(FahrenheitToCelsius, ftemp)))

    #using lambda
    print(list(map(lambda l: (l * 9/5) + 32, ctemp)))
    print(list(map(lambda l: (l - 32) * 5/9, ftemp)))

if __name__ == '__main__':
    main()