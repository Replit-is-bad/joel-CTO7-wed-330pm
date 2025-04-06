import random
import time
from datetime import datetime

# === Configuration === #
SLEEP_DURATION = 1
POST_BATTLE_DELAY = 2.5
STATS_FILE = "hero_stats.txt"

HERO_CLASSES = {
    "Warrior":   {"hp": 120, "xp_mod": 1.0, "hp_gain": 25},
    "Rogue":     {"hp": 90,  "xp_mod": 1.2, "hp_gain": 15},
    "Mage":      {"hp": 80,  "xp_mod": 1.5, "hp_gain": 10},
    "Paladin":   {"hp": 100, "xp_mod": 1.1, "hp_gain": 20}
}

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

def log_hero_stats(name, hclass, level, xp, monsters_defeated, killer, tier):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(STATS_FILE, "a") as f:
        f.write(f"[{timestamp}] Hero: {name} the {hclass} | Level: {level} | XP: {xp} | "
                f"Defeated: {monsters_defeated} monsters | "
                f"Killed by: [{tier}] {killer}\n")

def choose_class():
    print("🎭 Choose your class:")
    for i, cls in enumerate(HERO_CLASSES.keys(), 1):
        print(f"  {i}. {cls} (HP: {HERO_CLASSES[cls]['hp']}, XP Mod: {HERO_CLASSES[cls]['xp_mod']})")
    while True:
        try:
            choice = int(input("Select class number: "))
            cls = list(HERO_CLASSES.keys())[choice - 1]
            return cls
        except (ValueError, IndexError):
            print("❌ Invalid choice. Try again.")

def simulate_battle():
    hero_name = input("🧙‍♂️ Enter your hero’s name: ").strip() or "Nameless One"
    hero_class = choose_class()

    stats = HERO_CLASSES[hero_class]
    hero_hp = stats["hp"]
    hero_max_hp = stats["hp"]
    xp_mod = stats["xp_mod"]
    hp_gain_per_level = stats["hp_gain"]

    hero_level = 1
    hero_xp = 0
    monsters_defeated = 0

    print(f"🚀 {hero_name} the {hero_class} begins their quest at Level {hero_level} with {hero_hp} HP!")
    time.sleep(0.5)

    def xp_required(level):
        return 100 * level

    while hero_hp > 0:
        tier, monster, damage, base_xp = choose_monster()
        hero_hp -= damage

        if hero_hp <= 0:
            print(f"☠️ A {tier} monster [{monster}] hits for {damage} damage and slays {hero_name}!")
            log_hero_stats(hero_name, hero_class, hero_level, hero_xp, monsters_defeated, monster, tier)
            break

        gained_xp = int(base_xp * xp_mod)
        hero_xp += gained_xp
        monsters_defeated += 1

        print(f"👾 [{tier}] {monster} hits for {damage} damage! "
              f"{hero_name}'s HP: {hero_hp} | +{gained_xp} XP (Total: {hero_xp})")

        # Level up check
        while hero_xp >= xp_required(hero_level):
            hero_xp -= xp_required(hero_level)
            hero_level += 1
            hero_max_hp += hp_gain_per_level
            hero_hp = min(hero_max_hp, hero_hp + 30)
            print(f"🌟 LEVEL UP! {hero_name} is now Level {hero_level}! "
                  f"Max HP: {hero_max_hp}, Current HP: {hero_hp}")
            time.sleep(SLEEP_DURATION)

        time.sleep(POST_BATTLE_DELAY)

    print(f"\n💀 {hero_name} the {hero_class} perished at Level {hero_level} after defeating {monsters_defeated} monsters.")
    print(f"📝 Stats saved to {STATS_FILE}")

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
    