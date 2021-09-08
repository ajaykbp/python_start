def test(arg1):
    """
    this is docsstring of test
    args1: accepts args1 int type
    :return: nothing
    """
    print(arg1)

if __name__ == '__main__':
    #test(1)
    print(test.__doc__)