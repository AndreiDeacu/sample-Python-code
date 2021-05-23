import operatii1

class operatii:
    def inmultire(self, a, b):
        self.produs = a * b
        print(self.produs)
    def adunare(self, a, b):
        self.suma = a + b
        print(self.suma)
    def sumaCifrelor(self, n):
        self.s = 0
        while n != 0:
            self.s = self.s + int(n) % 10
            n = int(n) / 10
        print(self.s)
    def alegere(self):
        option = int(input('alegeti operatia: \n1: adunare \n2: scadere \n3: inmultire \n4: impartire \n5: suma cifrelor \n6: oprire\n'))
        if option == 1:
            a = int(input('dati primul nr: '))
            b = int(input('dati al doilea nr: '))
            opt.adunare(a, b)
        elif option == 2:
            a = int(input('dati primul nr: '))
            b = int(input('dati al doile3a nr: '))
            opt1.scadere(a, b)
        elif option == 3:
            a = int(input('dati primul nr: '))
            b = int(input('dati al doile3a nr: '))
            opt.inmultire(a, b)
        elif option == 4:
            a = int(input('dati primul nr: '))
            b = int(input('dati al doile3a nr: '))
            opt1.impartire(a, b)
        elif option == 5:
            n = int(input('dati nr: '))
            opt.sumaCifrelor(n)
        elif option == 6:
            exit()
        while True:
            option1 = input('doriti sa continuati?\n')
            if option1 == 'da':
                option = int(input('alegeti operatia: \n1: adunare \n2: scadere \n3: inmultire \n4: impartire \n5: suma cifrelor \n6: oprire\n'))
                if option == 1:
                    a = int(input('dati primul nr: '))
                    b = int(input('dati al doilea nr: '))
                    opt.adunare(a, b)
                elif option == 2:
                    a = int(input('dati primul nr: '))
                    b = int(input('dati al doile3a nr: '))
                    opt1.scadere(a, b)
                elif option == 3:
                    a = int(input('dati primul nr: '))
                    b = int(input('dati al doile3a nr: '))
                    opt.inmultire(a, b)
                elif option == 4:
                    a = int(input('dati primul nr: '))
                    b = int(input('dati al doile3a nr: '))
                    opt1.impartire(a, b)
                elif option == 5:
                    n = int(input('dati nr: '))
                    opt.sumaCifrelor(n)
                elif option == 6:
                    break
            elif option1 == 'nu':
                break
                


opt = operatii()
opt1 = operatii1.operatiisi()
opt.alegere()

