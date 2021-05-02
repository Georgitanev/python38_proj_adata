import json

parties_dictionary = {
    "ПП ГЕРБ": "GERP",
    "БСП за БЪЛГАРИЯ": "BSP",
    "ВОЛЯ": "VOLQ",
    "Движение за права и свободи - ДПС": "DPS",
    "ОБЕДИНЕНИ ПАТРИОТИ - НФСБ, АТАКА и ВМРО": "OP",
}

with open('parties_dictionary.json'.format(1), 'w', encoding='utf-8') as file:
    json.dump(parties_dictionary, file, ensure_ascii=False)

