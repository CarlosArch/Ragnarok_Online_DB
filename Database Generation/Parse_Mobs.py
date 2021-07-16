'WARNING: This will truncate the MOBS table and insert all from mob_db.txt.'
import sqlite3
from binascii import unhexlify

with sqlite3.connect('RagnarokDatabase.db') as conn:
    cur = conn.cursor()
    cur.execute('BEGIN TRANSACTION')
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('DELETE FROM MOBS;')
    with open('mob_db.txt') as mob_db_txt:
        next(mob_db_txt)
        for item in mob_db_txt:
            item = item.split(sep=',')
            mob_mode = bin(int(item[25][2:], 16))[2:] if item[25][2:] else '0'
            mob_mode = mob_mode.zfill(14)
            item = {
                'ID'                    : item[0].replace('=', '')
               ,'NAME'                  : item[2]
               ,'LEVEL'                 : item[4]
               ,'HP'                    : item[5]
               ,'BASE_EXP'              : item[7]
               ,'JOB_EXP'               : item[8]
               ,'CAN_MOVE'              : mob_mode[13]
               ,'LOOTER'                : mob_mode[12]
               ,'AGRESSIVE'             : mob_mode[11]
               ,'ASSIST'                : mob_mode[10]
               ,'CAST_SENSOR_IDLE'      : mob_mode[9]
               ,'BOSS'                  : mob_mode[8]
               ,'PLANT'                 : mob_mode[7]
               ,'CAN_ATTACK'            : mob_mode[6]
               ,'CHANGE_CHASE'          : mob_mode[5]
               ,'ANGRY'                 : mob_mode[4]
               ,'CHANGE_TARGET_MELEE'   : mob_mode[3]
               ,'CHANGE_TARGET_CHASE'   : mob_mode[2]
               ,'TARGET_WEAK'           : mob_mode[1]
               ,'NO_KNOCKBACK'          : mob_mode[0]
               ,'MOVE_SPEED'            : item[26]
               ,'ATTACK_DELAY'          : item[27]
               ,'MVP_EXP'               : item[30]
               ,'MVP_DROP_ID_1'         : item[31]
               ,'MVP_DROP_PERCENTAGE_1' : item[32]
               ,'MVP_DROP_ID_2'         : item[33]
               ,'MVP_DROP_PERCENTAGE_2' : item[34]
               ,'MVP_DROP_ID_3'         : item[35]
               ,'MVP_DROP_PERCENTAGE_3' : item[36]
               ,'DROP_ID_1'             : item[37]
               ,'DROP_PERCENTAGE_1'     : item[38]
               ,'DROP_ID_2'             : item[39]
               ,'DROP_PERCENTAGE_2'     : item[40]
               ,'DROP_ID_3'             : item[41]
               ,'DROP_PERCENTAGE_3'     : item[42]
               ,'DROP_ID_4'             : item[43]
               ,'DROP_PERCENTAGE_4'     : item[44]
               ,'DROP_ID_5'             : item[45]
               ,'DROP_PERCENTAGE_5'     : item[46]
               ,'DROP_ID_6'             : item[47]
               ,'DROP_PERCENTAGE_6'     : item[48]
               ,'DROP_ID_7'             : item[49]
               ,'DROP_PERCENTAGE_7'     : item[50]
               ,'DROP_ID_8'             : item[51]
               ,'DROP_PERCENTAGE_8'     : item[52]
               ,'DROP_ID_9'             : item[53]
               ,'DROP_PERCENTAGE_9'     : item[54]
               ,'CARD_DROP_ID'          : item[55]
               ,'CARD_DROP_PERCENTAGE'  : item[56]
            }
            cur.execute('''
                INSERT INTO MOBS (
                    ID
                   ,NAME
                   ,LEVEL
                   ,HP
                   ,BASE_EXP
                   ,JOB_EXP
                   ,CAN_MOVE
                   ,LOOTER
                   ,AGRESSIVE
                   ,ASSIST
                   ,CAST_SENSOR_IDLE
                   ,BOSS
                   ,PLANT
                   ,CAN_ATTACK
                   ,CHANGE_CHASE
                   ,ANGRY
                   ,CHANGE_TARGET_MELEE
                   ,CHANGE_TARGET_CHASE
                   ,TARGET_WEAK
                   ,NO_KNOCKBACK
                   ,MOVE_SPEED
                   ,ATTACK_DELAY
                   ,MVP_EXP
                   ,MVP_DROP_ID_1
                   ,MVP_DROP_PERCENTAGE_1
                   ,MVP_DROP_ID_2
                   ,MVP_DROP_PERCENTAGE_2
                   ,MVP_DROP_ID_3
                   ,MVP_DROP_PERCENTAGE_3
                   ,DROP_ID_1
                   ,DROP_PERCENTAGE_1
                   ,DROP_ID_2
                   ,DROP_PERCENTAGE_2
                   ,DROP_ID_3
                   ,DROP_PERCENTAGE_3
                   ,DROP_ID_4
                   ,DROP_PERCENTAGE_4
                   ,DROP_ID_5
                   ,DROP_PERCENTAGE_5
                   ,DROP_ID_6
                   ,DROP_PERCENTAGE_6
                   ,DROP_ID_7
                   ,DROP_PERCENTAGE_7
                   ,DROP_ID_8
                   ,DROP_PERCENTAGE_8
                   ,DROP_ID_9
                   ,DROP_PERCENTAGE_9
                   ,CARD_DROP_ID
                   ,CARD_DROP_PERCENTAGE
                ) VALUES (
                    :ID
                   ,:NAME
                   ,:LEVEL
                   ,:HP
                   ,:BASE_EXP
                   ,:JOB_EXP
                   ,:CAN_MOVE
                   ,:LOOTER
                   ,:AGRESSIVE
                   ,:ASSIST
                   ,:CAST_SENSOR_IDLE
                   ,:BOSS
                   ,:PLANT
                   ,:CAN_ATTACK
                   ,:CHANGE_CHASE
                   ,:ANGRY
                   ,:CHANGE_TARGET_MELEE
                   ,:CHANGE_TARGET_CHASE
                   ,:TARGET_WEAK
                   ,:NO_KNOCKBACK
                   ,:MOVE_SPEED
                   ,:ATTACK_DELAY
                   ,:MVP_EXP
                   ,:MVP_DROP_ID_1
                   ,:MVP_DROP_PERCENTAGE_1
                   ,:MVP_DROP_ID_2
                   ,:MVP_DROP_PERCENTAGE_2
                   ,:MVP_DROP_ID_3
                   ,:MVP_DROP_PERCENTAGE_3
                   ,:DROP_ID_1
                   ,:DROP_PERCENTAGE_1
                   ,:DROP_ID_2
                   ,:DROP_PERCENTAGE_2
                   ,:DROP_ID_3
                   ,:DROP_PERCENTAGE_3
                   ,:DROP_ID_4
                   ,:DROP_PERCENTAGE_4
                   ,:DROP_ID_5
                   ,:DROP_PERCENTAGE_5
                   ,:DROP_ID_6
                   ,:DROP_PERCENTAGE_6
                   ,:DROP_ID_7
                   ,:DROP_PERCENTAGE_7
                   ,:DROP_ID_8
                   ,:DROP_PERCENTAGE_8
                   ,:DROP_ID_9
                   ,:DROP_PERCENTAGE_9
                   ,:CARD_DROP_ID
                   ,:CARD_DROP_PERCENTAGE
                );
            '''
           ,item)
    cur.execute('COMMIT')
