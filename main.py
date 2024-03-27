import random
import assets

DEBUG: bool = False

class Game:

    def __init__(self) -> None:
        self.word: str = self.getRandomWord()
        self.chars: list[str] = list(set(self.word))
        self.setDefault()
        self.firstTime: bool = True
        self.printStart()
        self.run()

    def run(self) -> None:
        while True:
            print(assets.hangman[self.guesses])
            self.printWord()
            if DEBUG:
                print(self.word)
            print("Guesses left: {}".format(self.guesses))
            self.printGuessed()
            ans: str = self.getInput()
            if (ans in self.word):
                self.correct.append(ans)
                self.checkWinner()
            else:
                self.guesses -= 1
                if (self.guesses == 0):
                    print(assets.hangman[self.guesses])
                    print("Word: {}".format(self.word))
                    self.gameOver()
                else:
                    self.wrong.append(ans)
            ans = ""

    def checkWinner(self) -> None:
        x: list[str] = [c for c in self.chars if c not in self.correct]
        if DEBUG:
            print(x)
        if x == []:
            self.printWord()
            self.won = True
            self.gameOver()

    def printWord(self) -> None:
        wordLen: int = len(self.word)
        showWord: list[str] = []
        for _ in range(wordLen):
            showWord += "_"
        for i in self.correct:
            for j, y in enumerate(self.word):
                if y == i:
                    showWord[j] = i
        print("Word:", "".join(showWord))

    def gameOver(self) -> None:
        if self.won:
            print("You won!")
        else:
            print("Game over! (the dude died)")
        self.setDefault()
        self.word = self.getRandomWord()
        self.chars: list[str] = list(set(self.word))
        self.printStart()

    def printGuessed(self) -> None:
        print("Right: ", end="")
        for i in self.correct:
            print(i, end=", ")
        print("| Wrong: ", end="")
        for i in self.wrong:
            print(i, end=", ")
        print(end="\n")

    def getInput(self) -> str:
        while True:
            ans: str = input("Enter character: ")
            if (ans != ""):
                ans = ans.lower()[0]
                break
        return ans

    def setDefault(self) -> None:
        self.guesses: int = 11
        self.correct: list[str] = []
        self.wrong: list[str] = []
        self.won: bool = False

    def printStart(self) -> None:
        if (self.firstTime):
            print(assets.hangman[0])
            print("Welcome to hangman!")
            self.firstTime = False
        while True:
            ans: str = input("Would you like to play?(y/n): ").lower()
            if (ans == "y"):
                break
            elif (ans == "n"):
                print("Bye!")
                quit()
            else:
                print("Not valid input try again.")

    def getRandomWord(self) -> str:
        return random.choice(assets.words)


if __name__ == "__main__":
    Game()
