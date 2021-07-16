template = '''SELECT
    MOBS.ID
   ,MOBS.NAME
   ,MOBS.LEVEL
   ,MOBS.HP
   ,MOBS.BASE_EXP
   ,MOBS.JOB_EXP
   ,MOBS.MVP_EXP
   ,IIF(MOBS.MVP_EXP > 0,1,0) AS MOB_IS_BOSS
   ,MOBS.PLANT

   ,'{droptype}' AS DROP_TYPE
   ,MOBS.{id_column}
   ,ITEMS.NAME
   ,ITEMS.WEIGHT
   ,ITEMS.SELL_PRICE
   ,MOBS.{percentage_column}
FROM
    MOBS
    LEFT JOIN ITEMS ON
        MOBS.{id_column} = ITEMS.ID

UNION ALL

'''

types_and_columns = [
    ['MVP_DROP_1' ,'MVP_DROP_ID_1' ,'MVP_DROP_PERCENTAGE_1']
   ,['MVP_DROP_2' ,'MVP_DROP_ID_2' ,'MVP_DROP_PERCENTAGE_2']
   ,['MVP_DROP_3' ,'MVP_DROP_ID_3' ,'MVP_DROP_PERCENTAGE_3']
   ,['DROP_1'     ,'DROP_ID_1'     ,'DROP_PERCENTAGE_1']
   ,['DROP_2'     ,'DROP_ID_2'     ,'DROP_PERCENTAGE_2']
   ,['DROP_3'     ,'DROP_ID_3'     ,'DROP_PERCENTAGE_3']
   ,['DROP_4'     ,'DROP_ID_4'     ,'DROP_PERCENTAGE_4']
   ,['DROP_5'     ,'DROP_ID_5'     ,'DROP_PERCENTAGE_5']
   ,['DROP_6'     ,'DROP_ID_6'     ,'DROP_PERCENTAGE_6']
   ,['DROP_7'     ,'DROP_ID_7'     ,'DROP_PERCENTAGE_7']
   ,['DROP_8'     ,'DROP_ID_8'     ,'DROP_PERCENTAGE_8']
   ,['DROP_9'     ,'DROP_ID_9'     ,'DROP_PERCENTAGE_9']
   ,['CARD_DROP'  ,'CARD_DROP_ID'  ,'CARD_DROP_PERCENTAGE']
]

with open('Other/SQLunpivot.txt', 'w') as textfile:
    for droptype, id_column, percentage_column in types_and_columns:
        textfile.write(template.format(
            droptype=droptype
           ,id_column=id_column
           ,percentage_column=percentage_column))