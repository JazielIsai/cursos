import html

from bs4 import BeautifulSoup


class Points(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x=', self.x, ' y=', self.y)


p1 = Points("A", "B")
p1.print_point()


soup = BeautifulSoup(html, "html.parser")
print(soup.prettify())