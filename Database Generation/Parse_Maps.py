'WARNING: This will truncate the MOBS_ON_MAP table and insert all from Onmap.txt.'
import sqlite3
from binascii import unhexlify

with sqlite3.connect('RagnarokDatabase.db') as conn:
    cur = conn.cursor()
    cur.execute('BEGIN TRANSACTION')
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('DELETE FROM MOBS_ON_MAP;')
    with open('Database Generation/Original Data/Onmap.txt') as mobs_on_map_txt:
        mob_id = ''
        for line in mobs_on_map_txt:
            if not mob_id:
                mob_id = line.replace('#', '').strip()
            elif '#' in line:
                mob_id = ''
            else:
                line = line.split(' ')
                map_name = line[0].strip()
                amount = line[1].strip('()\n')
                cur.execute('''
                    INSERT INTO MOBS_ON_MAP (
                        MOB_ID
                       ,MAP_NAME
                       ,AMOUNT
                    ) VALUES (
                        :MOB_ID
                       ,:MAP_NAME
                       ,:AMOUNT
                    );
                '''
                ,{
                    'MOB_ID' : mob_id
                   ,'MAP_NAME' : map_name
                   ,'AMOUNT' : amount
                })
    cur.execute('COMMIT')
