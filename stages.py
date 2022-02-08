class Hangman:
    def __init__(self, stage):
        self.stage = stage

        if self.stage == 1:
            self.mode_1()
        elif self.stage == 2:
            self.mode_2()
        elif self.stage == 3:
            self.mode_3()
        elif self.stage == 4:
            self.mode_4()
        elif self.stage == 5:
            self.mode_5()
        elif self.stage == 6:
            self.mode_6()
        elif self.stage == 7:
            self.mode_7()
        elif self.stage == 8:
            self.mode_8()
        elif self.stage == 9:
            self.mode_9()
        elif self.stage == 10:
            self.mode_10()
        elif self.stage == 11:
            self.mode_11()
        elif self.stage == 12:
            self.mode_12()
        elif self.stage == 13:
            self.mode_13() 

    def mode_1(self):
        print('\t')
        print('\t')
        print('\t')
        print('\t')
        print('\t/')
        
    def mode_2(self):
        print('\t')
        print('\t')
        print('\t')
        print('\t')
        print('\t/ \\')

    def mode_3(self):
        print('\t')
        print('\t')
        print('\t')
        print('\t |')
        print('\t/ \\')

    def mode_4(self):
        print('\t')
        print('\t')
        print('\t |')
        print('\t |')
        print('\t/ \\')
    
    def mode_5(self):
        print('\t')
        print('\t |')
        print('\t |')
        print('\t |')
        print('\t/ \\')

    def mode_6(self):
        print('\t /')
        print('\t |')
        print('\t |')
        print('\t |')
        print('\t/ \\')

    def mode_7(self):
        print('\t /--')
        print('\t |')
        print('\t |')
        print('\t |')
        print('\t/ \\')

    def mode_8(self):
        print('\t /----')
        print('\t |')
        print('\t |')
        print('\t |')
        print('\t/ \\')

    def mode_9(self):
        print('\t /----')
        print('\t |   o')
        print('\t |')
        print('\t |')
        print('\t/ \\')
    
    def mode_10(self):
        print('\t /----')
        print('\t |   o')
        print('\t |   |')
        print('\t |')
        print('\t/ \\')

    def mode_11(self):
        print('\t /----')
        print('\t |   o')
        print('\t |  /|')
        print('\t |')
        print('\t/ \\')
    
    def mode_11(self):
        print('\t /----')
        print('\t |   o')
        print('\t |  /|\\')
        print('\t |')
        print('\t/ \\')

    def mode_12(self):
        print('\t /----')
        print('\t |   o')
        print('\t |  /|\\')
        print('\t |  /')
        print('\t/ \\')

    def mode_13(self):
        print('\t /----')
        print('\t |   o')
        print('\t |  /|\\')
        print('\t |  / \\')
        print('\t/ \\')