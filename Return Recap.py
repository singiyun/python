def make_juice(fruit):
    return f"{fruit}+쥬스"

def add_ice(juice):
    return f"{juice}+얼음"

def add_sugar(iced_juice):
    return f"{iced_juice}+설탕"

juice=make_juice("사과")
cold_juice=add_ice(juice)
perfect_juice=add_sugar(cold_juice)

print(perfect_juice)