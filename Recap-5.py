player = {
    "name" :"singiyun",
    "age" : 24,
    "alive" : True,
    "fav_food" : ("피자", "햄버거"),
    "friend" : {
        "name" : "jun",
        "fav_food" : ["사과"]
    }
}

player['fav_food'] = "사과"
player.pop("alive")
player['friend']['fav_food'].append("바나나")

print (player)