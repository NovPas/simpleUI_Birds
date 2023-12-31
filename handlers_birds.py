import json
from ru.travelfood.simple_ui import NoSQL as noClass
from ru.travelfood.simple_ui import SimpleSQLProvider as sqlClass
from java import jclass
from io import BytesIO
from PIL import Image
import base64
from datetime import datetime


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

    hashMap.put("cards", json.dumps(customcards, ensure_ascii=False).encode('utf8').decode())

    return hashMap


def card_on_open(hashMap, _files=None, _data=None):

    ncl = noClass("base_nosql")
    k = str(hashMap.get("selected_card_key"))
    c = json.loads(ncl.get(k))

    hashMap.put("НазваниеПтицы", c["string1"])
    hashMap.put("ЦветПерьев", c["string2"])
    hashMap.put("ФотоПтицы", c["pic1"])

    return hashMap


def menu_input(hashMap,_files=None,_data=None):
    if hashMap.get("listener") == "menu":
        if hashMap.get("menu") == "Список всех птиц":
            hashMap.put("ShowScreen", "Список птиц")
        elif hashMap.get("menu") == "Птицы которых я видел":
            hashMap.put("ShowScreen", "Виденные птицы")
    elif hashMap.get("listener") == "ON_BACK_PRESSED":
        hashMap.put("FinishProcess", "")

    return hashMap


def actions_on_input(hashMap, _files=None, _data=None):

    if hashMap.get("listener") == "btn_add":
        hashMap.put("ShowScreen", "Добавить птицу")
    elif hashMap.get("listener") == "btn_saw":
        hashMap.put("saw_bird", str(hashMap.get("НазваниеПтицы")))
    elif hashMap.get("listener") == "add_saw_bird":
        insert_data(hashMap, str(hashMap.get("saw_bird")))
    elif hashMap.get("listener") == "save":
        save_bird(hashMap)
        hashMap.put("ShowScreen", "Список птиц")
    elif hashMap.get("listener") == "btn_destroy":
        ncl = noClass("base_nosql")
        ncl.destroy()
    elif hashMap.get("listener") == "CardsClick":
        hashMap.put("ShowScreen", "Карточка птицы")
    elif hashMap.get("listener") == "ON_BACK_PRESSED":
        current_screen_name = hashMap.get("current_screen_name")
        if current_screen_name == "Список птиц" or current_screen_name == "Виденные птицы":
            hashMap.put("ShowScreen", "Начальное меню")
        elif current_screen_name == "Карточка птицы" or current_screen_name == "Добавить птицу":
            hashMap.put("ShowScreen", "Список птиц")

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

    hashMap.put("НазваниеПтицыНовое", "")
    hashMap.put("ЦветПерьевНовый", "")
    hashMap.put("photoGallery", "")


def init_on_start(hashMap,_files=None,_data=None):
    hashMap.put("SQLConnectDatabase", "test1.DB")
    hashMap.put("SQLExec", json.dumps({"query": "CREATE TABLE IF NOT EXISTS seeing_birds (id integer primary key autoincrement, datetime DATETIME NOT NULL, name TEXT, photo BLOB, amount INTEGER)", "params": ""}))
    return hashMap

def insert_data(hashMap, name):

    if str(name) == 'None':
        hashMap.put("toast", "Выберите птицу")
        return

    previous_amount = 0

    sql = sqlClass()

    # Получаем количество
    # res = sql.SQLQuery("SELECT MAX(amount) amount FROM seeing_birds", "")
    res = sql.SQLQuery("SELECT MAX(amount) amount FROM seeing_birds WHERE name = \"" + name + "\"", "")
    records = json.loads(res)
    for record in records:
        if isinstance(record['amount'], int):
            previous_amount = record['amount']
        else:
            previous_amount = 0
    new_amount = previous_amount + 1

    # Получаем фото
    ncl = noClass("base_nosql")
    c = json.loads(ncl.get(name))
    photo_data = c['pic1']

    # Получаем Дату
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Записываем
    success = sql.SQLExec('''
        INSERT INTO seeing_birds (datetime, name, photo, amount)
        VALUES (?, ?, ?, ?)
        ''', (str(current_datetime)+","+str(name)+","+str(photo_data)+","+str(new_amount)))

    if success:
        hashMap.put("toast", "Птица успешно добавлена!!!")


def resize_base64_image(base64_string):
    try:
        decoded_data = base64.b64decode(base64_string)
        image = Image.open(BytesIO(decoded_data))
        size = (160, 160)
        image = image.resize(size, Image.ANTIALIAS)
        buffer = BytesIO()
        image.save(buffer, format="PNG")
        resized_image_data = buffer.getvalue()
        resized_base64_string = base64.b64encode(resized_image_data).decode("utf-8")
        return resized_base64_string
    except Exception as e:
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
