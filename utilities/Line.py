import re
from abc import ABC, abstractmethod
from colors import strip_color

class Line(ABC):

    center_h = False

    def __init__(self):
        super().__init__()

    def center(self, columns, text):
        return text.rjust(int((columns - len(text)) / 2) + len(text))

    @abstractmethod
    def draw(self, columns):
        pass
    

class OneColumnLine(Line):

    def __init__(self, text = "", center_h = False):
        self.text = text
        self.center_h = center_h

    def draw(self, columns):
        col_width = len(strip_color(self.text))

        colored_offset = len(self.text) - int(col_width)

        return (self.text if not self.center_h else self.center(columns + colored_offset, self.text)) + "\n"

class TwoColumnsLine(Line):

    def __init__(self, col1_text = "", col2_text = "", center_h = False):
        self.col1_text = col1_text
        self.col2_text = col2_text
        self.center_h = center_h

    def draw(self, columns):
        
        col1_width = len(strip_color(self.col1_text))
        col2_width = len(strip_color(self.col2_text))

        colored_offset_1 = len(self.col1_text) - int(col1_width)
        colored_offset_2 = len(self.col2_text) - int(col2_width)

        if not self.center_h:
            return self.col1_text.ljust(int(columns / 2 + colored_offset_1)) + self.col2_text.ljust(int(columns / 2 + colored_offset_2)) + "\n"
        else:
            return self.center(columns / 2 + colored_offset_1, self.col1_text).ljust(int(columns / 2 + colored_offset_1)) + self.center(columns / 2 + colored_offset_2, self.col2_text).ljust(int(columns / 2 + colored_offset_2)) + "\n"

class LineHelper:

    @staticmethod
    def draw_lines(columns, lines):

        text = ""
        for line in lines:
            text = text + line.draw(columns)
        
        return text