import json
# da vpi6a novite partii
# parties_dictionary = {
#     "ПП ГЕРБ": "GERP",
#     "БСП за БЪЛГАРИЯ": "BSP",
#     "ВОЛЯ": "VOLQ",
#     "Движение за права и свободи - ДПС": "DPS",
#     "ОБЕДИНЕНИ ПАТРИОТИ - НФСБ, АТАКА и ВМРО": "OP",
# }
# with open('parties_dictionary.json'.format(1), 'w', encoding='utf-8') as file:
#     json.dump(parties_dictionary, file, ensure_ascii=False)

#//TODO !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
parties_dictionary_new = {
    "ГЕРБ-СДС": "GERP",
    "ПП ИМА ТАКЪВ НАРОД": "ITN",
    "БСП за БЪЛГАРИЯ": "BSP",
    "Движение за права и свободи - ДПС": "DPS",
    "ДЕМОКРАТИЧНА БЪЛГАРИЯ": "DB",
    "ИЗПРАВИ СЕ! МУТРИ ВЪН!": "IMV",
}

with open('parties_dictionary_new.json'.format(1), 'w', encoding='utf-8') as file:
    json.dump(parties_dictionary_new, file, ensure_ascii=False)
