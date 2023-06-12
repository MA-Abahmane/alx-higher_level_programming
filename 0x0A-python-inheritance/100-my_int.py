""" a class MyInt that inherits from int: """


class MyInt(int):
    """ MyInt is a rebel. MyInt has == and != operators inverted """

    def __ne__(self, value):
        """ not equal comparison inverted """
        return (self.real == value)

    def __eq__(self, value):
        """ equal comparison inverted"""
        return (self.real != value)
