from string import Template


def main():
    sentence = Template("Hi There, I am ${name}. Wanted to brief you about today's City weather. Expecting "
                        "$weatherCondition today. \nTemperature will be $temperature Celsius. humidity will"
                        "be around $humidity")
    print(sentence.substitute(name='Ajay', weatherCondition='Hot', temperature=45, humidity=4))
    data = {'name': 'Kalpana', 'weatherCondition': 'Breezy', 'temperature': 30, 'humidity': 4}
    print('\n'+sentence.substitute(data))


if __name__ == '__main__':
    main()
