player = {
    'name' : 'nico',
    'age' : 12,
    'alive' : True,
    'fav_food' : ["피자", "치킨"]
}
player['fav_food'].append("라면")
print(player.get('fav_food'))
print(player['fav_food'])