import random

"""
This module randomly makes gift assignments among a group of
 second cousins, ensuring no one is assigned a sibling or
 first cousin.

The more unbalanced the family branches are, the higher the
 likelihood the script will fail with
       ValueError: sample larger than population
 in which case running the script a second time usually
 finds a valid pattern.  Sufficiently unbalanced patterns, 
 though, are intractable.
"""

# families is a dict of first generation descendants to
#  dicts of second generation descendants to their children
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
    # Find the set of kids who are not related to this aunt or uncle
    other_gen_1 = families.copy()
    del other_gen_1[aunt_or_uncle]
    other_kids = set(sum([sum(s.values(),[]) for s in other_gen_1.values()],[]))
    # Iterate over the descendants of this aunt or uncle, assigning
    #  them second cousins
    for grandkid, great_grandkids in grandkids.items():
        for kid in great_grandkids:
            in_other_families = (unassigned & other_kids)
            getting_gift_for = random.sample(in_other_families,1)[0]
            assignments[kid] = getting_gift_for
            unassigned.remove( getting_gift_for )
            
for kid in sorted(assignments.keys()):
    print("{kid} will give a gift to {other_kid}".format(
          kid=kid, other_kid=assignments[kid]))
