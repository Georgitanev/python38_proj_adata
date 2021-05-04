import json

parties_dict_new = {
    "ГЕРБ-СДС": "GERP",
    "ПП ИМА ТАКЪВ НАРОД": "ITN",
    "БСП за БЪЛГАРИЯ": "BSP",
    "Движение за права и свободи - ДПС": "DPS",
    "ДЕМОКРАТИЧНА БЪЛГАРИЯ": "DB",
    "ИЗПРАВИ СЕ! МУТРИ ВЪН!": "IMV",
}

# saving json file with parties dictionary
with open("parties_dictionary_new.json".format(1), "w", encoding="utf-8") as file:
    json.dump(parties_dict_new, file, ensure_ascii=False, indent=4, sort_keys=True)

# schema save to json file
schema_json = {
    "$schema": "http://json-schema.org/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "date_born": {"type": "string"},
        "place_born": {"anyOf": [{"type": "null"}, {"type": "string"}]},
        "profession": {"anyOf": [{"type": "null"}, {"type": "string"}]},
        "lang": {"anyOf": [{"type": "null"}, {"type": "string"}]},
        "party": {"type": "string"},
        "email": {
            "title": "Email address",
            "type": "string",
            "pattern": "^\\S+@\\S+\\.\\S+$",
            "format": "email",
            "minLength": 6,
            "maxLength": 127,
        },
        "url": {"type": "string"},
        "education": {"anyOf": [{"type": "null"}, {"type": "string"}]},
        "pp": {"type": "string"},
        "dob": {"type": "string"},
    },
    "required": [
        "date_born",
        "dob",
        "education",
        "email",
        "lang",
        "name",
        "party",
        "place_born",
        "pp",
        "profession",
        "url",
    ],
    "title": "Welcome",
}

with open("json_schema_with_email.json".format(1), "w", encoding="utf-8") as file:
    json.dump(schema_json, file, ensure_ascii=False, indent=4, sort_keys=True)
