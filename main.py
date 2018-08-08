class Board:
    width = 40
    height = 40
    array = []
    cells = []

    def __init__(self):
        for _j in range(self.height):
            row = []
            row2 = []
            for _i in range(self.width):
                row.append('.')
                row2.append('.')
            self.array.append(row)
            self.cells.append(row2)

    def show(self):
        for _i in range(self.height):
            row = ""
            row2 = ""
            row = row.join(self.array[_i])
            row2 = row2.join(self.cells[_i])
            print(row+"    "+row2)

    def set_letter(self, row: int, col: int, let: str):
        self.array[row][col] = let

    def set_cell(self, row: int, col: int, ori: str):
        if self.cells[row][col] == '-' and ori == '|' or self.cells[row][col] == '|' and ori == '-':
            self.cells[row][col] = '+'
            return
        self.cells[row][col] = ori

    def get_letter(self, row: int, col: int):
        return self.array[row][col]

    def set_word(self, row: int, col: int, word: str, orientation='-'):
        if orientation == "|":
            for letter in word:
                self.set_letter(row, col, letter)
                self.set_cell(row, col, orientation)
                row += 1
            return
        else:
            for letter in word:
                self.set_letter(row, col, letter)
                self.set_cell(row, col, orientation)
                col += 1
            return

    def find_possible_spots(self):
        to_ret = []
        r = int(self.height / 2)
        c = int(self.width / 2)
        step = 1
        while True:
            for i in range(step):
                c += 1
                if r >= self.height or r < 0 or c >= self.width or c < 0:
                   return to_ret
                if self.cells[r][c] == '-' or self.cells[r][c] == '|':
                    if self.cells[r][c] == '-':
                        anty_ori = '|'
                    else:
                        anty_ori = "-"
                    to_ret.append([r,c, anty_ori])
            for i in range(step):
                r += 1
                if r > self.height or r < 0 or c > self.width or c < 0:
                   return to_ret
                if self.cells[r][c] == '-' or self.cells[r][c] == '|':
                    if self.cells[r][c] == '-':
                        anty_ori = '|'
                    else:
                        anty_ori = "-"
                    to_ret.append([r,c, anty_ori])
            step += 1
            for i in range(step):
                c -= 1
                if r > self.height or r < 0 or c > self.width or c < 0:
                   return to_ret
                if self.cells[r][c] == '-' or self.cells[r][c] == '|':
                    if self.cells[r][c] == '-':
                        anty_ori = '|'
                    else:
                        anty_ori = "-"
                    to_ret.append([r,c, anty_ori])
            for i in range(step):
                r -= 1
                if r > self.height or r < 0 or c > self.width or c < 0:
                   return to_ret
                if self.cells[r][c] == '-' or self.cells[r][c] == '|':
                    if self.cells[r][c] == '-':
                        anty_ori = '|'
                    else:
                        anty_ori = "-"
                    to_ret.append([r, c, anty_ori])
            step += 1

    def try_fit_word(self, row: int, col: int, word: str, ori: str):
        if ori == '-':
            if self.cells[row][col - 1] != '.':
                return False
            for letter in word:
                if self.get_letter(row, col) != letter and self.get_letter(row, col) != '.':
                    return False
                if self.cells[row-1][col] == '-':
                    return False
                if self.cells[row+1][col] == '-':
                    return False
                if self.cells[row-1][col] == '|' and self.cells[row][col] != '|':
                    return False
                if self.cells[row+1][col] == '|' and self.cells[row][col] != '|':
                    return False
                col += 1
            if self.cells[row][col] != '.':
                return False
            return True
        else:
            if self.cells[row - 1][col] != '.':
                return False
            for letter in word:
                if self.get_letter(row, col) != letter and self.get_letter(row, col) != '.':
                    return False
                if self.cells[row][col-1] == '|':
                    return False
                if self.cells[row][col+1] == '|':
                    return False
                if self.cells[row][col-1] == '-' and self.cells[row][col] != '-':
                    return False
                if self.cells[row][col+1] == '-' and self.cells[row][col] != '-':
                    return False
                row += 1
            if self.cells[row][col] != '.':
                return False
            return True



    def put_word(self, word: str):
        spots = self.find_possible_spots()
        for spot in spots:
            letter = self.get_letter(spot[0], spot[1])
            position = word.find(letter)
            if position == -1:
                continue
            if spot[2] == '-':
                if self.try_fit_word(spot[0], spot[1] - position, word, spot[2]):
                    self.set_word(spot[0], spot[1] - position, word, spot[2])
                    return
                else:
                    continue
            else:
                if self.try_fit_word(spot[0] - position, spot[1], word, spot[2]):
                    self.set_word(spot[0] - position, spot[1], word, spot[2])
                    return
                else:
                    continue
            print("Failed to fit :(")






def intersection(first: str, second: str):
    for l in first:
        for i in second:
            if(i == l):
                return first.index(l), second.index(i)
    return -1, -1

wordString = "Nie rzucim ziemi, skąd nasz ród, Nie damy pogrześć mowy! Polski my naród, polski lud, Królewski szczep piastowy, Nie damy by nas zniemczył wróg... Tak nam dopomóż Bóg! Do krwi ostatniej kropli z żył Bronić będziemy Ducha, Aż się rozpadnie w proch i w pył Krzyżacka zawierucha. Twierdzą nam będzie każdy próg... ak nam dopomóż Bóg! Nie będzie Niemiec pluł nam w twarz, Ni dzieci nam germanił. Orężny wstanie hufiec nas, Duch będzie nam hetmanił, "
wordString = wordString.upper().replace(',','').replace('.','').replace("!", "")
wordSet = wordString.split(" ")

to_be_removed = []
for word in wordSet:
    if len(word) < 6:
        to_be_removed.append(word)

for word in to_be_removed:
    wordSet.remove(word)

wordSet.sort(key=len, reverse=True)
print(wordSet)

theboard = Board()
theboard.set_word(20,15, wordSet[0], '-')
for wordnum in range(1, len(wordSet)):
    theboard.put_word(wordSet[wordnum])
    theboard.show()
    input("continue...")
theboard.show()