import json
from ru.travelfood.simple_ui import NoSQL as noClass
from java import jclass
from io import BytesIO
from PIL import Image
import base64


def customcards_on_open(hashMap, _files=None, _data=None):

    ncl = noClass("base_nosql")
    keys = ncl.getallkeys()

    customcards = get_customcards_settings()

    customcards["customcards"]["cardsdata"] =[]
    jkeys = json.loads(keys)
    for k in jkeys:
        c = json.loads(ncl.get(k))
        c['key'] = k
        customcards["customcards"]["cardsdata"].append(c)

    if not hashMap.containsKey("cards"):
        hashMap.put("cards", json.dumps(customcards, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def card_on_open(hashMap, _files=None, _data=None):

    hashMap.put("toast", str(hashMap.get("selected_card_key")))

    ncl = noClass("base_nosql")
    k = str(hashMap.get("selected_card_key"))
    c = json.loads(ncl.get(k))

    hashMap.put("НазваниеПтицы", c["string1"])
    hashMap.put("ЦветПерьев", c["string2"])
    hashMap.put("ФотоПтицы", c["pic1"])

    return hashMap


def actions_on_input(hashMap, _files=None, _data=None):

    hashMap.put("toast", "hashMap.get(listener): " + hashMap.get("listener"))

    if hashMap.get("listener") == "btn_add":
        hashMap.put("ShowScreen", "Добавить птицу")
    elif hashMap.get("listener") == "save":
        save_bird(hashMap)
        hashMap.put("ShowScreen", "Список птиц")
    elif hashMap.get("listener") == "btn_destroy":
        ncl = noClass("base_nosql")
        ncl.destroy()
    elif hashMap.get("listener") == "CardsClick":
        hashMap.put("ShowScreen", "Карточка птицы")

    return hashMap


def save_bird(hashMap):

    pic1 = ""
    if hashMap.get("photoGallery"):
        jphotoarr = json.loads(hashMap.get("photoGallery"))
        pic1_row = jphotoarr[0]["base64"]
        pic1 = resize_base64_image(pic1_row)

    ncl = noClass("base_nosql")
    key = hashMap.get("НазваниеПтицыНовое")
    json_string = {"string1": hashMap.get("НазваниеПтицыНовое"),
                   "string2": hashMap.get("ЦветПерьевНовый"),
                   "pic1": pic1
                   }
    ncl.put(key, json.dumps(json_string, ensure_ascii=False), True)


def resize_base64_image(base64_string):
    try:
        # Decode base64 string into binary data
        decoded_data = base64.b64decode(base64_string)

        # Open the image using PIL
        image = Image.open(BytesIO(decoded_data))

        # Resize the image to 100x100 pixels
        size = (160, 160)
        image = image.resize(size, Image.ANTIALIAS)

        # Convert the resized image back to binary data
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        resized_image_data = buffer.getvalue()

        # Encode the resized image data back to base64
        resized_base64_string = base64.b64encode(resized_image_data).decode("utf-8")

        return resized_base64_string
    except Exception as e:
        print("Error occurred:", str(e))
        return ""


def get_customcards_settings():
    return \
        {"customcards": {
            "options": {
                "search_enabled": True,
                "save_position": True
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
                                "weight": 1
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
                                "weight": 1
                            },
                            {
                                "type": "LinearLayout",
                                "orientation": "vertical",
                                "height": "wrap_content",
                                "width": "match_parent",
                                "weight": "2",
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
                                ]
                            }
                        ]
                    }
                ]
            }

        }
        }
