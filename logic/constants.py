from collections import OrderedDict

POTENTIALLY_REQUIRED_DUNGEONS = [
    "Skyview",
    "Earth Temple",
    "Lanayru Mining Facility",
    "Ancient Cistern",
    "Sandship",
    "Fire Sanctuary",
]

ALL_DUNGEON_AREAS = [
    "Skyview",
    "Earth Temple",
    "Lanayru Mining Facility",
    "Ancient Cistern",
    "Sandship",
    "Fire Sanctuary",
    "Sky Keep",
]

DUNGEON_NAMES = OrderedDict(
    [
        ("SV", "Skyview"),
        ("ET", "Earth Temple"),
        ("LMF", "Lanayru Mining Facility"),
        ("AC", "Ancient Cistern"),
        ("SS", "Sandship"),
        ("FS", "Fire Sanctuary"),
        ("SK", "Sky Keep"),
        # for the purposes of restricting triforces to sky keep
        ("Triforce", "Sky Keep"),
        ("LanayruCaves", "Lanayru Caves"),  # "short name" doesn't allow space
    ]
)
DUNGEON_NAME_TO_SHORT_DUNGEON_NAME = OrderedDict(
    [v, k] for k, v in DUNGEON_NAMES.items()
)

ENTRANCE_CONNECTIONS = {
    "Dungeon Entrance in Deep Woods": "Skyview",
    "Dungeon Entrance in Eldin Volcano": "Earth Temple",
    "Dungeon Entrance in Lanayru Desert": "Lanayru Mining Facility",
    "Dungeon Entrance in Lake Floria": "Ancient Cistern",
    "Dungeon Entrance in Sand Sea": "Sandship",
    "Dungeon Entrance in Volcano Summit": "Fire Sanctuary",
    "Dungeon Entrance on Skyloft": "Sky Keep",
}

SILENT_REALMS = OrderedDict(
    [
        ("Skyloft Silent Realm", "Skyloft Trial Gate"),
        ("Faron Silent Realm", "Faron Trial Gate"),
        ("Lanayru Silent Realm", "Lanayru Trial Gate"),
        ("Eldin Silent Realm", "Eldin Trial Gate"),
    ]
)

SILENT_REALM_CHECKS = OrderedDict(
    [
        ("Skyloft Silent Realm - Stone of Trials", "Trial Gate on Skyloft"),
        ("Faron Silent Realm - Water Scale", "Trial Gate in Faron Woods"),
        ("Lanayru Silent Realm - Clawshots", "Trial Gate in Lanayru Desert"),
        ("Eldin Silent Realm - Fireshield Earrings", "Trial Gate in Eldin Volcano"),
    ]
)

SHOP_CHECKS = [
    "Beedle - 50 Rupee Item",
    "Beedle - First 100 Rupee Item",
    "Beedle - Second 100 Rupee Item",
    "Beedle - Third 100 Rupee Item",
    "Beedle - 300 Rupee Item",
    "Beedle - 600 Rupee Item",
    "Beedle - 800 Rupee Item",
    "Beedle - 1000 Rupee Item",
    "Beedle - 1200 Rupee Item",
    "Beedle - 1600 Rupee Item",
]

MAP_CHECKS = [
    "Skyview - Chest on Tree Branch",
    "Earth Temple - Chest in West Room",
    "Lanayru Mining Facility - Chest after Armos Fight",
    "Ancient Cistern - Chest after Whip Hooks",
    "Sandship - Chest before 4-Door Corridor",
    "Fire Sanctuary - Chest after Second Trapped Mogma",
    "Sky Keep - First Chest",
]

SMALL_KEY_CHECKS = [
    "Skyview - Chest behind Two Eyes",
    "Skyview - Chest behind Three Eyes",
    "Lanayru Mining Facility - First Chest in Hub Room",
    "Ancient Cistern - Chest in East Part",
    "Ancient Cistern - Bokoblin",
    "Sandship - Chest behind Combination Lock",
    "Sandship - Robot in Brig's Reward",
    "Fire Sanctuary - Chest in First Room",
    "Fire Sanctuary - Chest near First Trapped Mogma",
    "Fire Sanctuary - Chest after Bombable Wall",
    "Lanayru Caves - Golo's Gift",
    "Sky Keep - Chest after Dreadfuse",
]

BOSS_KEY_CHECKS = [
    "Skyview - Boss Key Chest",
    "Earth Temple - Boss Key Chest",
    "Lanayru Mining Facility - Boss Key Chest",
    "Ancient Cistern - Boss Key Chest",
    "Sandship - Boss Key Chest",
    "Fire Sanctuary - Boss Key Chest",
]

TRIFORCE_CHECKS = [
    "Sky Keep - Triforce of Courage",
    "Sky Keep - Triforce of Wisdom",
    "Sky Keep - Triforce of Power",
]

END_OF_DUNGEON_CHECKS = OrderedDict(
    [
        ("Skyview", "Skyview - Ruby Tablet"),
        ("Earth Temple", "Earth Temple - Amber Tablet"),
        ("Lanayru Mining Facility", "Lanayru Mining Facility - Goddess Harp"),
        ("Ancient Cistern", "Ancient Cistern - Farore's Flame"),
        ("Sandship", "Sandship - Nayru's Flame"),
        ("Fire Sanctuary", "Fire Sanctuary - Din's Flame"),
    ]
)

STARTING_SWORD_COUNT = {
    "Swordless": 0,
    "Practice Sword": 1,
    "Goddess Sword": 2,
    "Goddess Longsword": 3,
    "Goddess White Sword": 4,
    "Master Sword": 5,
    "True Master Sword": 6,
}

ALL_TYPES = [
    "skyloft",
    "sky",
    "thunderhead",
    "faron",
    "eldin",
    "lanayru",
    "dungeon",
    "mini dungeon",
    "free gift",
    "freestanding",
    "miscellaneous",
    "silent realm",
    "digging",
    "bombable",
    "combat",
    "song",
    "spiral charge",
    "minigame",
    "crystal",
    "short",
    "long",
    "fetch",
    "crystal quest",
    "scrapper",
    "peatrice",
    "beedle",
    "cheap",
    "medium",
    "expensive",
    "goddess",
    "faron goddess",
    "eldin goddess",
    "lanayru goddess",
    "floria goddess",
    "summit goddess",
    "sand sea goddess",
]

POST_GOAL_LOCS = {
    "Ghirahim 1": "Skyview - Ghirahim Heart Container",
    "Scaldera": "Earth Temple - Scaldera Heart Container",
    "Moldarach": "Lanayru Mining Facility - Moldarach Heart Container",
    "Koloktos": "Ancient Cistern - Koloktos Heart Container",
    "Tentalus": "Sandship - Tentalus Heart Container",
    "Ghirahim 2": "Fire Sanctuary - Ghirahim Heart Container",
}

DUNGEON_GOALS = {
    "Skyview": "Ghirahim 1",
    "Earth Temple": "Scaldera",
    "Lanayru Mining Facility": "Moldarach",
    "Ancient Cistern": "Koloktos",
    "Sandship": "Tentalus",
    "Fire Sanctuary": "Ghirahim 2",
}

RUPEE_CHECKS = [
    "Central Skyloft - Rupee Waterfall Cave Crawlspace",
    "Sky Keep - Rupee in Alcove of FS Room",
    "Skyview - Rupee Southeast Tunnel",
    "Skyview - Rupee Southwest Tunnel",
    "Skyview - Rupee East Tunnel",
    "Skyview - Rupee on Spring Pillar",
    "Ancient Cistern - Rupee East Hand",
    "Ancient Cistern - Rupee West Hand",
    "Ancient Cistern - Rupee East Room Main Path",
    "Ancient Cistern - Rupee East Room Cubby",
    "Ancient Cistern - Rupee East Room Short Tunnel 1",
    "Ancient Cistern - Rupee East Room Short Tunnel 2",
    "Ancient Cistern - Rupee East Room Short Tunnel 3",
    "Earth Temple - Rupee in Lava Tunnel",
    "Earth Temple - Rupee above Drawbridge",
    "Faron Woods - Rupee on Great Tree Branch North",
    "Faron Woods - Rupee on Great Tree Branch West",
    "Faron Woods - Rupee on Platform Near Floria Door",
    "Faron Woods - Rupee on Hollow Tree Root",
    "Faron Woods - Rupee on Hollow Tree Branch",
    "Lake Floria - Rupee Under Big Boulder",
    "Lake Floria - Rupee Behind Northeast Boulder Right",
    "Lake Floria - Rupee Behind Northeast Boulder Left",
    "Lake Floria - Rupee Behind Southeast Boulder",
    "Lake Floria - Rupee High Ledge Outside Cistern Entrance",
    "Eldin Volcano - Rupee Ledge before First Room",
    "Eldin Volcano - Rupee behind Bombable Wall in First Room",
    "Eldin Volcano - Rupee in Crawlspace in First Room",
    "Eldin Volcano - Rupee above Mogma Turf Entrance North",
    "Eldin Volcano - Rupee above Mogma Turf Entrance Southeast",
    "Eldin Volcano - Rupee Bombable Wall First Slope Right",
    "Eldin Volcano - Rupee Bombable Wall First Slope Left",
    "Lanayru Sand Sea - Rupee Harbor First Pillar",
    "Lanayru Sand Sea - Rupee Harbor Entrance Crown Right",
    "Lanayru Sand Sea - Rupee Harbor Entrance Crown Left",
    "Lanayru Sand Sea - Pirate Stronghold - Rupee Sea Pillar East",
    "Lanayru Sand Sea - Pirate Stronghold - Rupee Sea Pillar West",
    "Lanayru Sand Sea - Pirate Stronghold - Rupee Bird Statue Pillar or Nose",
]

QUICK_BEETLE_CHECKS = [
    "Lanayru Sand Sea - Rupee Harbor Entrance Crown Right",
    "Lanayru Sand Sea - Rupee Harbor Entrance Crown Left",
    "Lanayru Sand Sea - Pirate Stronghold - Rupee Sea Pillar East",
    "Lanayru Sand Sea - Pirate Stronghold - Rupee Sea Pillar West",
]
