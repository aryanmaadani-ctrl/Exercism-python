Azara_List = (
    ("Amethyst Octopus", "1F"),
    ("Angry Monkey Figurine", "5B"),
    ("Antique Glass Fishnet Float", "3D"),
    ("Brass Spyglass", "4B"),
    ("Carved Wooden Elephant", "8C"),
    ("Crystal Crab", "6A"),
    ("Glass Starfish", "6D"),
    ("Model Ship in Large Bottle", "8A"),
    ("Pirate Flag", "7F"),
    ("Robot Parrot", "1C"),
    ("Scrimshawed Whale Tooth", "2A"),
    ("Silver Seahorse", "4E"),
    ("Vintage Pirate Hat", "7E"),
)

Rui_List = (
    ("Seaside Cottages", ("1", "C"), "Blue"),
    ("Aqua Lagoon (Island of Mystery)", ("1", "F"), "Yellow"),
    ("Deserted Docks", ("2", "A"), "Blue"),
    ("Spiky Rocks", ("3", "D"), "Yellow"),
    ("Abandoned Lighthouse", ("4", "B"), "Blue"),
    ("Hidden Spring (Island of Mystery)", ("4", "E"), "Yellow"),
    ("Stormy Breakwater", ("5", "B"), "Purple"),
    ("Old Schooner", ("6", "A"), "Purple"),
    ("Tangled Seaweed Patch", ("6", "D"), "Orange"),
    ("Quiet Inlet (Island of Mystery)", ("7", "E"), "Orange"),
    ("Windswept Hilltop (Island of Mystery)", ("7", "F"), "Orange"),
    ("Harbor Managers Office", ("8", "A"), "Purple"),
    ("Foggy Seacave", ("8", "C"), "Purple"),
)


def get_coordinate(record):
        return record[1]
        
print(get_coordinate(('Amethyst  Octopus', '1F')))



def convert_coordinate(coordinate):
    return tuple(coordinate) 


def compare_records(treasure_record, location_record):
    location1 = treasure_record[1]
    location2 = location_record[1][0] + location_record[1][1]
    while treasure_record and location_record:
        return (location1 == location2)

def create_record(Azara_locations, Rui_locations):
    if compare_records(Azara_locations, Rui_locations):
        return(tuple(Azara_locations + Rui_locations))
    else:
        return("not a match")


#از هوش مصنوعی کمک گرفته شده مجدد بررسی میشه

def clean_up(combined_records):
    report = ""
    for record in combined_records:
        treasure, old_coord, location, new_coord, color = record
        cleaned = (treasure, location, new_coord, color)
        report += str(cleaned) + "\n"
    return report
