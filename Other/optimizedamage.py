from math import floor, sqrt
from scipy.optimize import differential_evolution, LinearConstraint
from gekko import GEKKO

from stattable import stat_table

def stat_assign(STR_pts, INT_pts, DEX_pts, LUK_pts, is_ranged):
    STR_pts = floor(STR_pts)
    INT_pts = floor(INT_pts)
    DEX_pts = floor(DEX_pts)
    LUK_pts = floor(LUK_pts)

    STR = stat_table[STR_pts]
    INT = stat_table[INT_pts]
    DEX = stat_table[DEX_pts]
    LUK = stat_table[LUK_pts]

    ATK, MATK, VCTM = advanced_stats(STR + 3
                                    ,INT + 12
                                    ,DEX + 8
                                    ,LUK + 2
                                    ,is_ranged)

    return STR, INT, DEX, LUK, ATK, MATK, VCTM

def advanced_stats (STR, INT, DEX, LUK, is_ranged):
    if not is_ranged:
        ATK = 2 * (floor((175 / 4) + STR + (DEX / 5) + (LUK / 3)))
    else:
        ATK = 2 * (floor((175 / 4) + (STR / 5) + DEX + (LUK / 3)))

    MATK = floor(floor(175 / 4) + INT + floor(INT / 2) + floor(DEX / 5) + floor(LUK / 3))

    VCTM = 1-sqrt(((DEX * 2) + INT) / 530)

    return ATK, MATK, VCTM

def ability(ATK, bonus_ATK, MATK, bonus_MATK, INT, VCTM):
    
    damage = (ATK + bonus_ATK) * (300 + ((5 * 50) * (INT / 40))) / 100
    cooldown = 3 * VCTM + .5

    # damage = (MATK + bonus_MATK) * ((350 + (INT*3)) * 175) / 100
    # cooldown = .6 + 12 * VCTM

    return damage, cooldown

def problem(arguments):
    STR_pts, INT_pts, DEX_pts, LUK_pts = arguments
    is_ranged = True
    STR, INT, DEX, LUK, ATK, MATK, VCTM = stat_assign(STR_pts, INT_pts, DEX_pts, LUK_pts, is_ranged)

    bonus_ATK = 100+185
    bonus_MATK= 0

    DAM, CD = ability(ATK, bonus_ATK, MATK, bonus_MATK, INT, VCTM)
    dps = DAM / CD
    return -dps

if __name__ == '__main__':
    bounds = [
        (0, 1415)
       ,(0, 1415)
       ,(0, 1415)
       ,(0, 1415)
    ]
    constraint = LinearConstraint([[1,1,1,1]],[0],[2730])

    result = differential_evolution(problem
                                   ,bounds
                                   ,maxiter=5000
                                   ,popsize=100
                                   ,constraints=(constraint))

    STR_pts, INT_pts, DEX_pts, LUK_pts = result.x
    STR, INT, DEX, LUK, ATK, MATK, VCTM = stat_assign(STR_pts, INT_pts, DEX_pts, LUK_pts, is_ranged=True)

    print(f'STR = {STR} ({STR_pts:.0f} points)\n'
         ,f'INT = {INT} ({INT_pts:.0f} points)\n'
         ,f'DEX = {DEX} ({DEX_pts:.0f} points)\n'
         ,f'LUK = {LUK} ({LUK_pts:.0f} points)\n'
         ,f'{-result.fun:.2f} approx. DPS')