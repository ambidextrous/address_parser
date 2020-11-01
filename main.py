from json import dumps
import click
from typing import List, Dict
import string

from postal.parser import parse_address


def strip_punctuation(s: str) -> str:
    """
    Returns a copy of a given string with punctuation removed

    strip_punctuation("Dog!5 ca.T") -> "Dog5 caT" 
    """
    exclude = set(string.punctuation)
    return "".join(ch for ch in s if ch not in exclude)


def fix_capitalization(parsed_substring: str, original_string: str) -> str:
    """
    Fixes capitalization in a lower case substring to match that in 
    an original string possibly containing capital letters

    fix_capitalization("rue emma", "Rue Emma 4") -> "Rue Emma"
    """
    depunctuated_parsed = strip_punctuation(parsed_substring)
    depunctuated_original = strip_punctuation(original_string)
    parsed_list = depunctuated_parsed.split()
    original_list = depunctuated_original.split()
    original_list_lower = [item.lower() for item in original_list]
    fixed_list = []
    for i in range(len(parsed_list)):
        for j in range(len(original_list)):
            if parsed_list[i] == original_list_lower[j]:
                fixed_list.append(original_list[j])
    return " ".join(item for item in fixed_list)


def format_address(raw_address: str) -> Dict[str, str]:
    """
    Calls pypostal NLP library to parse street and housenumber data from a
    given address string: https://github.com/openvenues/pypostal

    format_address('Calle 39 No 1540') 
    ->
    expected_address = {"street": "Calle 39", "housenumber": "No 1540"}
    """
    if not raw_address:
        raise ValueError(f"Cannot extract address data from {raw_address}")
    try:
        parsed_address = parse_address(raw_address)
        house_number = [
            item[0] for item in parsed_address if item[1] == "house_number"
        ][0]
        road = [item[0] for item in parsed_address if item[1] == "road"][0]
        formatted_address = {
            "street": fix_capitalization(road, raw_address),
            "housenumber": fix_capitalization(house_number, raw_address),
        }
    except IndexError as ex:
        message = f"Unable to parse street and house number data from input `{raw_address}` (parsed to `{parsed_address}`)"
        raise ValueError(message)
    return formatted_address


@click.command(
    name="parse",
    help="Parses street and house numbder data from an address. E.g. 'Calle 39 No 1540' -> {'street': 'calle 39', 'housenumber': 'no 1540'}",
)
@click.argument("address", nargs=-1)
def parse(address: str) -> None:
    """
    Minimal Command Line Interface tool to parse street and housenumber data from a give address string

    Useage:

    python main.py 'Calle 39 No 1540' 
    ->
    prints '{"street": "Calle 39", "housenumber": "No 1540"}' to stdout
    """
    if not address:
        raise ValueError("Missing address parameter")
    formatted_address = format_address(address[0])
    print(dumps(formatted_address))


if __name__ == "__main__":
    parse()
