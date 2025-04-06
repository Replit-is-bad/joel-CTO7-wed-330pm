import random
import time

# === Configuration === #
BASE_HP = 100
SLEEP_DURATION = 1

MONSTER_TIERS = {
    "Common": {
        "monsters": ["Goblin", "Skeleton", "Zombie", "Rat"],
        "damage_range": (1, 5),
        "xp": 10,
        "weight": 70
    },
    "Elite": {
        "monsters": ["Orc", "Wraith", "Werewolf", "Vampire"],
        "damage_range": (6, 10),
        "xp": 25,
        "weight": 25
    },
    "Boss": {
        "monsters": ["Demon", "Troll", "Dragon", "Lich"],
        "damage_range": (11, 15),
        "xp": 75,
        "weight": 5
    }
}

def choose_monster():
    tiers = list(MONSTER_TIERS.keys())
    weights = [MONSTER_TIERS[tier]["weight"] for tier in tiers]
    chosen_tier = random.choices(tiers, weights=weights, k=1)[0]

    monster = random.choice(MONSTER_TIERS[chosen_tier]["monsters"])
    dmg_min, dmg_max = MONSTER_TIERS[chosen_tier]["damage_range"]
    damage = random.randint(dmg_min, dmg_max)
    xp_gain = MONSTER_TIERS[chosen_tier]["xp"]

    return chosen_tier, monster, damage, xp_gain

def simulate_battle():
    hero_hp = BASE_HP
    hero_max_hp = BASE_HP
    hero_level = 1
    hero_xp = 0
    monsters_defeated = 0

    print(f" Hero begins their quest at Level {hero_level} with {hero_hp} HP!")
    time.sleep(0.5)

    def xp_required(level):
        return 100 * level

    while hero_hp > 0:
        tier, monster, damage, xp = choose_monster()
        hero_hp -= damage

        if hero_hp <= 0:
            print(f" A {tier} monster [{monster}] hits for {damage} damage and slays the hero!")
            break

        hero_xp += xp
        monsters_defeated += 1

        print(f" [{tier}] {monster} strikes for {damage} damage! "
              f"Hero HP: {hero_hp} | Gained {xp} XP (Total: {hero_xp})")

        # Check for level up
        while hero_xp >= xp_required(hero_level):
            hero_xp -= xp_required(hero_level)
            hero_level += 1
            hero_max_hp += 20
            hero_hp = min(hero_max_hp, hero_hp + 30)  # Heal 30 HP on level up
            print(f" LEVEL UP! Hero is now Level {hero_level}! "
                  f"Max HP: {hero_max_hp}, Current HP: {hero_hp}")

        time.sleep(SLEEP_DURATION)

    print(f"\n The hero perished at Level {hero_level} after defeating {monsters_defeated} monsters.")

# === Start Adventure === #
if __name__ == "__main__":
    simulate_battle()



# strr = 'A,B,C,D,E,F'
# list = strr.split(',')

# print(list)



# cust = input('What would u like to order? ')
# order =[]

# while cust != 'end':
#     order.append(cust)
#     cust = input('What would u like to order? ')

# print('U have ordered the following: ')
# count=1
# for i in order:
#     print(str(count) +'. ' +i)
#     count += 1
    