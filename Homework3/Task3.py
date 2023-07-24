# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


LIMIT = 20
tourist_kit: dict[str, float] = {'кружка': 0.2,
                                 'ложка': 0.1,
                                 'вилка': 0.1,
                                 'нож': 0.1,
                                 'одежда': 3.0,
                                 'аптечка': 1.0,
                                 'фонарь': 1.0,
                                 'спички': 0.02,
                                 'палатка': 15.0,
                                 'котелок': 2.0,
                                 'еда': 5.0,
                                 'бухло': 5.0}


def sort_dict(d: dict):
    temp = dict(sorted(d.items(), key=lambda x: x[1]))
    return temp


def pack_a_backpack(d: dict, limit=LIMIT):
    weight = 0
    bagpack = set()
    for d_key, d_values in d.items():
        if (weight + d_values) <= limit:
            bagpack.add(d_key)
            weight += d_values
    return weight, bagpack


temp = sort_dict(tourist_kit)
bagpack = pack_a_backpack(temp)
print(bagpack)
