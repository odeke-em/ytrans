import unittest

def main():
    testLoader = unittest.TestLoader()
    tests = testLoader.discover('tests')
    tRunner = unittest.runner.TextTestRunner()

    tRunner.run(tests)

if __name__ == '__main__':
    main()
