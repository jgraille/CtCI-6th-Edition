from cmd import Cmd


class Child(Cmd):

    prompt = 'child> '

    #constructor
    def __init__(self):
        """
        super() accessing inherited methods from a parent class
        """
        super(Child, self).__init__()

    def do_q(self, args=True):
        raise SystemExit

    def do_display(self, args=True):
        """
        This command will display an Hellow world  (cause it's fun)
        :param args: boolean
        :return: a printed object to the text stream file
        """
        print('Hello World')


class Cake:

    def __init__(self, cakename):
        self._cakename = cakename

    @property
    def cakename(self):
        return self._cakename

    @cakename.setter
    def cakename(self, value):
        self._cakename = value

    def display(self):
        print(self._cakename)


class Ingredients(Cake):

    def __init__(self, one, two):
        """
        call the parent to get its attributes and methods (single inheritance)
        :param one: string
        :param two: string
        """
        self.one = one
        self.two = two
        Cake.__init__(self, 'blackforest')


def main():
    #child = Child().cmdloop()
    ingredients = Ingredients('chocolate', 'sugar')
    print('Affichage de la property du parent {}'.format(ingredients.cakename))
    print('Affichage de la methode du parent {}'.format(ingredients.display()))


if __name__ == '__main__':
    main()