class Henyo:
    def __init__(self):
        self.char_count = 0

        # Loops
        self.loop_count_smemory = 0
        self.loop_activated = False
        self.get_loop_content = False
        self.content_count = 0

        self.printer = ""

        # Init Cells
        self.cells = []
        self.initCells()
        self.pointer = 149
        self.searchCells()

    def initCells(self):
        for i in range(301):
            self.cells.append(0)

    def searchCells(self):
        with open(input("Filename: ")) as file:
            for line in file:
                for char in line:
                    self.check(char)
                    self.char_count += 1
            print(self.printer)
    
    def check(self, char):
        if not self.loop_activated:
            if char == "+":
                self.cells[self.pointer] += 1
            elif char == ">":
                self.pointer += 1
            elif char == ".":
                self.printer += chr(self.cells[self.pointer])
            elif char == "[":
                if not self.loop_activated:
                    self.loop_activated = True
        else:
            self.check_loop(char)
        

    def check_loop(self, char):
        if not self.get_loop_content:
            if char == "+":
                
                self.loop_count_smemory += 1
            elif char == "x":
                self.loop_count_smemory += 10
            elif char == "y":
                self.loop_count_smemory += 100
            elif char == "{":
                self.get_loop_content = True
            elif char == "]":
                self.loop_count_smemory = 0
                self.loop_activated = False
        else:
            if char == "+":
                for i in range(self.loop_count_smemory):
                    self.content_count += 1
            elif char == "-":
                for i in range(self.loop_count_smemory):
                    self.content_count -= 1
            elif char == ">":
                for i in range(self.content_count):
                    self.pointer += 1
            elif char == "<":
                for i in range(self.content_count):
                    self.pointer -= 1
            elif char == "}":
                self.get_loop_content = False
                self.cells[self.pointer] += self.content_count
                self.content_count = 0

if __name__ == '__main__':
    # Initialize Henyo
    Henyo()