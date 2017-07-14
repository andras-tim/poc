import textwrap
from pyDatalog import pyDatalog


class Person(pyDatalog.Mixin):
    def __init__(self, name, gender, father=None, mother=None):
        """
        :type name: str
        :type father: str
        :type father: Person or None
        :type mother: Person or None
        """
        super(Person, self).__init__()

        self.name = name
        self.gender = gender
        self.father = father
        self.mother = mother

    def __repr__(self):
        return '<{}>'.format(self.name)


def print_eval(code):
    """
    :type code: str
    """
    print('### {}'.format(code))
    ret = eval(code)

    print('{ret_type}\n\n{ret}\n'.format(
        ret_type=type(ret),
        ret=textwrap.indent(str(ret), '    ')
    ))

pyDatalog.create_terms('X, Y, Z, PARENT, CHILD, GENDER, ANCESTOR, people, children, ancestors')

"""
Original:

+(mother['Look Skywalker'] == 'Padmé Amidala')
+(father['Look Skywalker'] == 'Anakin Skywalker')

+(mother['Leia Organa'] == 'Padmé Amidala')
+(father['Leia Organa'] == 'Anakin Skywalker')

+(mother['Anakin Solo'] == 'Leia Organa')
+(father['Anakin Solo'] == 'Han Solo')

+(mother['Foo Smally'] == 'Ciao Mediumy')
+(father['Foo Smally'] == 'Look Skywalker')
"""

_snakin_skywalker = Person('Anakin Skywalker', 'male')
_padme_amidala = Person('Padmé Amidala', 'female')
_mara_jade = Person('Mara Jade', 'female')
_look_skywalker = Person('Look Skywalker', 'male', father=_snakin_skywalker, mother=_padme_amidala)
_ben_skywalker = Person('Ben Skywalker', 'male', father=_look_skywalker, mother=_mara_jade)
_leia_organa = Person('Leia Organa', 'female', father=_snakin_skywalker, mother=_padme_amidala)
_han_solo = Person('Han Solo', 'male')
_jaina_solo = Person('Jaina Solo', 'female', father=_han_solo, mother=_leia_organa)
_jacen_solo = Person('Jacen Solo', 'male', father=_han_solo, mother=_leia_organa)
_anakin_solo = Person('Anakin Solo', 'male', father=_han_solo, mother=_leia_organa)


print_eval('Person.name[X]')
print_eval('(Person.name[X])')
print_eval('Person.name[X] == "foo"')
print_eval('Person.gender[X] == "male"')
print_eval('Person.name[X] == "Look Skywalker"')
print_eval('(Person.name[X] == "Look Skywalker") >= X')

children(X, Y) <= (Person.mother[Y] == X)
children(X, Y) <= (Person.father[Y] == X)

print_eval('children(PARENT, CHILD) & (Person.gender[CHILD] == GENDER)')

ancestors(X, Y) <= (children(X, Y))
ancestors(X, Z) <= (children(X, Y) & ancestors(Y, Z))

"""
Original:

print(ancestors('Anakin Skywalker', X))
"""

print_eval('(Person.name[PARENT] == "Padmé Amidala") & ancestors(PARENT, ANCESTOR)')
