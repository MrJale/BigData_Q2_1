#!/usr/bin/python
import sys

summ = {}
for line in sys.stdin:
    line = line.strip()
    shooter, defender, made, missed = line.split('@')
    shooter = shooter.strip()
    defender = defender.strip()
    made = int(made.strip())
    missed = int(missed.strip())
    if (shooter,defender) not in summ.keys():
        summ[(shooter,defender)] = [made,missed]
    else:
        summ[(shooter,defender)] = [summ[(shooter,defender)][i]+[made,missed][i] for i in range(2)]
        
for k,v in summ.items():
    summ[k] = v[0]/(v[0]+v[1])
    
player = {}
for k,v in summ.items():
    if k[0] not in player.keys():
        player[k[0]]=[(k[1],v)]
    else:
        player[k[0]].append((k[1],v))
        
for k,v in player.items():
    v.sort(key=lambda x: x[1])
    
for k,v in player.items():
    print(f'{k:20}{v[0][0]:20}')