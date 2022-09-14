class Problem:
    def __init__(self, x):
        self.tab = x;

    def __isFirst(self, x):
        for i in range(2, int(x / 2)):
            if x % i == 0:
                return False;
        return True;

    def Check(self):
        for i in range(len(self.tab)):
            if not self.__isFirst(self.tab[i]):
                return self.tab[i];

    def Check2(self):
        left = 0
        right = int(len(self.tab));
        while left < right:
            index = (left + right) // 2
            if self.__isFirst(self.tab[index]):
                if not self.__isFirst(self.tab[index + 1]):
                    return self.tab[index + 1]
                else:
                    left = index
            else:
                right = index


b = Problem([7, 2137, 5, 17, 3, 7, 7, 6, 26, 18, 24]);
print(b.Check2());
