from random import choice

subjects = ['NUMBER', 'PERSON', 'LOOK', 'CHURCH', 'CASTLE', 'FRAME',
            'APPLE', 'VILLAGE', 'BUILDING', 'FARMER', 'WAY', 'GUEST', 'WEEK',
            'HOUSE', 'TABLE', 'LABOURER']
predicates = ['CLOSED', 'SILENT', 'STRONG', 'GOOD', 'NARROW', 'NEAR',
              'NEW', 'NOISE', 'CLOSE', 'DEEP', 'EARLY', 'DARK', 'FREE',
              'LARGE', 'OLD', 'ANGRY']
conjunctions = [' AND ', ' OR ', ' THEREFORE ', ' BUT ALSO ', 'WHETHER ', ' NOR ', ' BUT ', ' IF ']
operators = ['A', 'EVERY', 'NO', 'NOT EVERY']

def phrase( subjects ):
    text = choice (operators) + '' + choice (subjects)
    if text == 'A APPLE':
        text = 'AN APPLE'
    return text + 'IS'

print('')
print( phrase (subjects) + choice (predicates) + choice (conjunctions) +
       phrase (operators) + choice (predicates) + '.')
print('')
