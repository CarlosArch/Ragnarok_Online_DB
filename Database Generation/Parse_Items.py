'WARNING: This will truncate the ITEMS table and insert all from item_db.txt.'
import sqlite3

with sqlite3.connect('RagnarokDatabase.db') as conn:
    cur = conn.cursor()
    cur.execute('BEGIN TRANSACTION')
    cur.execute('PRAGMA foreign_keys = ON;')
    cur.execute('DELETE FROM ITEMS;')
    with open('item_db.txt') as item_db_txt:
        next(item_db_txt)
        for item in item_db_txt:
            item = item.split(sep=',')
            item = {
                'ID'           : item[0].replace('=', '')
               ,'NAME'         : item[2]
               ,'CLASS_ID'     : item[3]
               ,'WEIGHT'       : item[6]
               ,'BUY_PRICE'    : item[4] if item[4] else int(int(item[5])*2) if item[5] else 0
               ,'SELL_PRICE'   : item[5] if item[5] else int(int(item[4])/2) if item[4] else 0
            }
            cur.execute('''
                INSERT INTO ITEMS (
                    ID
                   ,NAME
                   ,CLASS_ID
                   ,WEIGHT
                   ,BUY_PRICE
                   ,SELL_PRICE
                ) VALUES (
                    :ID
                   ,:NAME
                   ,:CLASS_ID
                   ,:WEIGHT
                   ,:BUY_PRICE
                   ,:SELL_PRICE
                );
            '''
           ,item
           )
    cur.execute('COMMIT')
