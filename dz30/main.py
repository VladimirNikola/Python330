from parsersdz30 import Parser


def main():
    pars = Parser("https://www.avion-market.ru/", "dz30.txt")
    pars.run()


if __name__ == '__main__':
    main()
