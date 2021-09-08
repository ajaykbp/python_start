if __name__ == '__main__':
    sentence = 'its a beautiful day'
    result = sentence.encode()
    print('Encoded value is -->{0}\nType of is -->{1}'.format(result, str(type(result))))
    resultDecoded = result.decode()
    print('Encoded value is -->{0}\nType of is -->{1}'.format(resultDecoded, str(type(resultDecoded))))