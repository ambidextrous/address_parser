from pytest import raises

from main import format_address


def test_parse_address_number_in_street_name():

    # Arrange
    input_address = "Calle 39 No 1540"
    expected_address = {"street": "Calle 39", "housenumber": "No 1540"}

    # Act
    output = format_address(input_address)

    # Assert
    assert output == expected_address


def test_parse_address_simple_case():

    # Arrange
    input_address = "Winterallee 3"
    expected_address = {"street": "Winterallee", "housenumber": "3"}

    # Act
    output = format_address(input_address)

    # Assert
    assert output == expected_address


def test_parse_address_letter_in_housenumber():

    # Arrange
    input_address = "Blaufeldweg 123B"
    expected_address = {"street": "Blaufeldweg", "housenumber": "123B"}

    # Act
    output = format_address(input_address)

    # Assert
    assert output == expected_address


def test_parse_address_multi_word_street_name():

    # Arrange
    input_address = "Auf der Vogelwiese 23 b"
    expected_address = {"street": "Auf der Vogelwiese", "housenumber": "23 b"}

    # Act
    output = format_address(input_address)

    # Assert
    assert output == expected_address


def test_parse_address_house_number_first_with_comma():

    # Arrange
    input_address = "4, rue de la revolution"
    expected_address = {"street": "rue de la revolution", "housenumber": "4"}

    # Act
    output = format_address(input_address)

    # Assert
    assert output == expected_address


def test_parse_not_an_address():

    # Arrange
    input_address = "ceci n'est pas une address"

    # Act & Assert
    with raises(ValueError):
        format_address(input_address)


def test_parse_empty_string():

    # Arrange
    input_address = ""

    # Act & Assert
    with raises(ValueError):
        format_address(input_address)


def test_parse_none():

    # Arrange
    input_address = None

    # Act & Assert
    with raises(ValueError):
        format_address(input_address)
