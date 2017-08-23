import textwrap
from pyDatalog import pyDatalog


def print_eval(code):
    """
    :type code: str
    """
    print('### {}'.format(code))
    ret = eval(code)

    print('type: {ret_type}\n\n{ret}\n'.format(
        ret_type=type(ret),
        ret=textwrap.indent(str(ret), '    ')
    ))


pyDatalog.create_terms('X, Y, Z, PERSON, PARENT, CHILD, ANCESTOR, people, mothers, fathers, children, ancestors')

+(fathers['Look Skywalker'] == 'Anakin Skywalker')
+(mothers['Look Skywalker'] == 'Padmé Amidala')

+(fathers['Ben Skywalker'] == 'Look Skywalker')
+(mothers['Ben Skywalker'] == 'Mara Jade')

+(fathers['Leia Organa'] == 'Anakin Skywalker')
+(mothers['Leia Organa'] == 'Padmé Amidala')

+(fathers['Jaina Solo'] == 'Han Solo')
+(mothers['Jaina Solo'] == 'Leia Organa')

+(fathers['Jacen Solo'] == 'Han Solo')
+(mothers['Jacen Solo'] == 'Leia Organa')

+(fathers['Anakin Solo'] == 'Han Solo')
+(mothers['Anakin Solo'] == 'Leia Organa')

print_eval('fathers[CHILD] == "Anakin Skywalker"')

people(X) <= (mothers[X] == Y)
people(Y) <= (mothers[X] == Y)
people(X) <= (fathers[X] == Y)
people(Y) <= (fathers[X] == Y)

print_eval('people(PERSON)')

children(X, Y) <= (mothers[Y] == X)
children(X, Y) <= (fathers[Y] == X)

print_eval('children(PARENT, CHILD)')

ancestors(X, Y) <= (children(X, Y))
ancestors(X, Z) <= (children(X, Y) & ancestors(Y, Z))

print_eval('ancestors("Padmé Amidala", ANCESTOR)')
