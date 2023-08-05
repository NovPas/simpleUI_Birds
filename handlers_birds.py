import json
import random


def customcards_on_open(hashMap, _files=None, _data=None):

    j = { "customcards":         {
        "options" :{
            "search_enabled" :True,
            "save_position" :True
        },
        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        # {
                        #     "type": "CheckBox",
                        #     "Value": "@cb1",
                        #     "NoRefresh": False,
                        #     "document_type": "",
                        #     "mask": "",
                        #     "Variable": "cb1",
                        #     "BackgroundColor": "#DB7093",
                        #     "width": "match_parent",
                        #     "height": "wrap_content",
                        #     "weight": 2
                        # },
                        {
                            "type": "Picture",
                            "show_by_condition": "",
                            "Value": "@pic1",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        },
                        {
                            "type": "TextView",
                            "show_by_condition": "",
                            "Value": "@val",
                            "NoRefresh": False,
                            "document_type": "",
                            "mask": "",
                            "Variable": "",
                            "TextSize": "16",
                            "TextColor": "#DB7093",
                            "TextBold": True,
                            "TextItalic": False,
                            "BackgroundColor": "",
                            "width": "match_parent",
                            "height": "wrap_content",
                            "weight": 2
                        },
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string1",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@string2",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": ""
                                },
                                # {
                                #     "type": "TextView",
                                #     "show_by_condition": "",
                                #     "Value": "@string3",
                                #     "NoRefresh": False,
                                #     "document_type": "",
                                #     "mask": "",
                                #     "Variable": ""
                                # },
                                # {
                                #     "type": "Button",
                                #     "show_by_condition": "",
                                #     "Value": "#f290",
                                #     "TextColor": "#DB7093",
                                #     "Variable": "btn_tst1",
                                #     "NoRefresh": False,
                                #     "document_type": "",
                                #     "mask": ""
                                #
                                # },
                                # {
                                #     "type": "Button",
                                #     "show_by_condition": "",
                                #     "Value": "#f469",
                                #     "TextColor": "#DB7093",
                                #     "Variable": "btn_tst2",
                                #     "NoRefresh": False,
                                #     "document_type": "",
                                #     "mask": ""
                                #
                                # }
                            ]
                        }
                        # {
                        #     "type": "PopupMenuButton",
                        #     "show_by_condition": "",
                        #     "Value": "Удалить;Проверить",
                        #     "NoRefresh": False,
                        #     "document_type": "",
                        #     "mask": "",
                        #     "Variable": "menu_delete"
                        #
                        # }
                    ]
                }
                # {
                #     "type": "TextView",
                #     "show_by_condition": "",
                #     "Value": "@descr",
                #     "NoRefresh": False,
                #     "document_type": "",
                #     "mask": "",
                #     "Variable": "",
                #     "TextSize": "-1",
                #     "TextColor": "#6F9393",
                #     "TextBold": False,
                #     "TextItalic": True,
                #     "BackgroundColor": "",
                #     "width": "wrap_content",
                #     "height": "wrap_content",
                #     "weight": 0
                # }
            ]
        }

    }
    }

    j["customcards"]["cardsdata" ] =[]
    for i in range(0 ,5):
        # if i== 0:
        #     c = {
        #
        #         "group": "Комплектующие"
        #
        #     }
        #
        #     j["customcards"]["cardsdata"].append(c)
        #
        # if i == 4:
        #     c = {
        #
        #         "group": "Уценка"
        #
        #     }
        #
        #     j["customcards"]["cardsdata"].append(c)

        c = {
            "key": str(i),
            # "descr": "Pos. " + str(i),
            "val": str(random.randint(10, 10000)) + " руб.",
            "string1": "Материнская плата ASUS ROG MAXIMUS Z690 APEX",
            "string2": "Гнездо процессора LGA 1700",
            # "string3": "Частотная спецификация памяти 4800 МГц"
            "pic1": "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"
        }

        j["customcards"]["cardsdata"].append(c)

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(j, ensure_ascii=False).encode('utf8').decode())

    return hashMap