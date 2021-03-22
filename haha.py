# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""
viceradkovy
komentar
"""

def sliceNdice(string = 'toto je testovaci retez'):
    strList = string.split(' ')
    return [x.upper() for x in strList if x[0] != 't']


def returnFirstChar(string):
    return string[0], ord(string[0])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sliceNdice())
    print(sliceNdice('This is test string 2'))
    character, asciiCode = returnFirstChar('Abeceda')
    print('{}\t{}'.format(character, asciiCode))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/