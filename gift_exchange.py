import random
families={'Keith':{
              'Brian':['Pascale','Kepler','Fermi'],
              'Susan':['Kira','Laurel'],
            },
          'Denny':{
              'Holly':['Isaac', 'Jordan', 'Jalon']
              ,},
          'Dean':{
              'Mary':['Myka','Koehn'],
              'Mandie':['Aryanna','Hazen'],
            },
          }
assignments={}
unassigned = set(sum([sum(s.values(),[]) for s in families.values()],[]))
for aunt_or_uncle, grandkids in families.items():
    other_gen_1 = families.copy()
    del other_gen_1[aunt_or_uncle]
    other_kids = set(sum([sum(s.values(),[]) for s in other_gen_1.values()],[]))
    for grandkid, great_grandkids in grandkids.items():
        for kid in great_grandkids:
            in_other_families = (unassigned & other_kids)
            getting_gift_for = random.sample(in_other_families,1)[0]
            assignments[kid] = getting_gift_for
            unassigned.remove( getting_gift_for )
            
