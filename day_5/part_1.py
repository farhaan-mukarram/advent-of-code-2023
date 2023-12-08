import re
from helper import parseFile

FILENAME = "input.txt"


maps = {
    "seed_to_soil": [],
    "soil_to_fertilizer": [],
    "fertilizer_to_water": [],
    "water_to_light": [],
    "light_to_temperature": [],
    "temperature_to_humidity": [],
    "humidity_to_location": [],
}


map_names = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]


def convert_map_name_to_key(map_name: str) -> str:
    return map_name.replace("map:", "").strip().replace("-", "_").strip()


def populate_map(name: str, mapping_details: list[str]) -> None:
    idx = mapping_details.index(name) + 1
    temp_map = []

    while idx < len(mapping_details) and mapping_details[idx] != "":
        destination_range_start, source_range_start, range_length = re.findall(
            r"\d+", mapping_details[idx]
        )

        destination_range_end = int(destination_range_start) + int(range_length) - 1
        source_range_end = int(source_range_start) + int(range_length) - 1

        temp_map.append(
            {
                "dest": (destination_range_start, destination_range_end),
                "source": (source_range_start, source_range_end),
                "range": range_length,
            }
        )

        idx += 1

    key = convert_map_name_to_key(map_name=name)
    maps[key] = temp_map


def find_item_destination(source: int, map_list):
    destination = source

    for item in map_list:
        dest_ranges, source_ranges = item["dest"], item["source"]
        dest_range_start, dest_range_end = dest_ranges
        source_range_start, source_range_end = source_ranges

        if source >= int(source_range_start) and source <= int(source_range_end):
            delta = source - int(source_range_start)
            destination = int(dest_range_start) + delta
            break

    return destination


def find_location_for_seed(seed_number: int):
    soil_number = find_item_destination(seed_number, maps["seed_to_soil"])
    fertilizer_number = find_item_destination(soil_number, maps["soil_to_fertilizer"])
    water_number = find_item_destination(fertilizer_number, maps["fertilizer_to_water"])
    light_number = find_item_destination(water_number, maps["water_to_light"])
    temperature_number = find_item_destination(
        light_number, maps["light_to_temperature"]
    )
    humidity_number = find_item_destination(
        temperature_number, maps["temperature_to_humidity"]
    )
    location_number = find_item_destination(
        humidity_number, maps["humidity_to_location"]
    )

    return location_number


if __name__ == "__main__":
    lines = parseFile(FILENAME)
    locations = []

    initial_seeds = lines[:1][0].split(":")[-1].strip().split(" ")

    mapping_details = lines[1:]

    for name in map_names:
        populate_map(name=name, mapping_details=mapping_details)

    for seed in initial_seeds:
        location = find_location_for_seed(seed_number=int(seed))
        locations.append(location)

    print("The lowest location number is:", min(locations))
