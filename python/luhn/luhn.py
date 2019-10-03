class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        if len(self.card_num) == 1:
            return False
        sum = 0
        if self.card_num.isdigit() == False:
            return False
        else:
            i = len(self.card_num) - 1
            while i >= 0:
                sum = sum + int(self.card_num[i])
                if (i - 1) >= 0:
                    num = int(self.card_num[i - 1])
                    second_digit = (2 * num) - 9 if (2 * num) > 9 else (2 * num)
                    sum = sum + second_digit
                i = i - 2         
        return sum % 10 == 0