import json


INIT_FILE = 'init.txt'


def get_problem_name(polygon_shortname):
#    filename = 'polygon-contest/problems/%s/statements/russian/problem-properties.json' % polygon_shortname
#    with open(filename, encoding='utf-8') as f:
#        content = f.read()
#    parsed = json.loads(content) 
#    return parsed['name']
    return polygon_shortname

min_row = -4
max_row = 4
min_column = -5
HEADER =\
"""
from table.models import *

def make_resource(name):
    resource = Resource(name=name)
    resource.save()
    return resource

def make_country(**kwargs):
    tmp = Country(**kwargs)
    tmp.save()
    return tmp

def make_card(**kwargs):
    tmp = Card(**kwargs)
    tmp.save()
    return tmp

Resource.objects.all().delete()
Card.objects.all().delete()
Country.objects.all().delete()
VirtualContest.objects.all().delete()
NeedsCardResource.objects.all().delete()
NeedsCardResource.objects.all().delete()
c0 = VirtualContest(name='Contest 0')
c0.save()
r0 = make_resource('r0')
r1 = make_resource('r1')
r2 = make_resource('r2')
r3 = make_resource('r3')

gb = make_country(name='gb', bonus=2)
de = make_country(name='de', bonus=3)
ch = make_country(name='ch', bonus=4)
cz = make_country(name='cz', bonus=5)
ro = make_country(name='ro', bonus=6)
it = make_country(name='it', bonus=7)
fr = make_country(name='fr', bonus=8)
"""


with open('init_script.py', 'w', encoding='utf-8') as output_file:
    print(HEADER, file=output_file)
#    print('AbstractTile.objects.all().delete()', file=output_file)
    
    with open(INIT_FILE, 'r', encoding='utf-8') as init:
        for line in init:
            if not line.strip():
                continue
            line = line.strip().split()
            print(line)
            # 01 kek 1 0000 1000 0
            contest_id, country, polygon_id, polygon_shortname, level, needs, gives, score = line[:8]

            print('card = make_card(ejudge_short_name="%s", name="%s", score=%d, level=%d, country=%s)' % (
                            polygon_id, polygon_shortname, int(score), int(level), country), file=output_file)
            print('c%d.cards.add(card)'  %(int(contest_id)), file=output_file);
            for i in range(0, len(needs)):
                cnt = int(needs[i])
                if cnt > 0:
                    print ('NeedsCardResource(card=card, resource=r%d, count=%d).save()' % (i, cnt), file=output_file)
            for i in range(0, len(gives)):
                cnt = int(gives[i])
                if cnt > 0:
                    print ('GivesCardResource(card=card, resource=r%d, count=%d).save()' % (i, cnt), file=output_file)
            print ('', file=output_file)
        print ('c0.save()', file=output_file)

    
#            parameters = 'row=%d, column=%d, ejudge_short_name="%02d", name="%s", statement_file_name="%02d.pdf", automatic_open_time=%d' % \
#                (int(row), int(column), int(polygon_id), get_problem_name(polygon_shortname), int(polygon_id), int(open_time)) 
#    
#            if bonus == '':
#                parameters += ', solved_award=%d, wrong_penalty=%d' % (int(award), int(award) // 20)
#
#            print('%s(%s).save()' % (class_name, parameters), file=output_file)
