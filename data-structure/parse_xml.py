from xml.dom import minidom


def parse_xml() -> list[str]:
    """
    Parses an XML file and retrieves the names of cities.

    Returns:
        list[str]: A list of city names.

    """
    file = minidom.parse('./assets/municipios.xml')

    cities_names: list[str] = list()
    cities_nodes = file.getElementsByTagName('municipio')
    for _, city in enumerate(cities_nodes):
        state = city.getElementsByTagName('sigla')[0].childNodes[0].nodeValue
        name: str = city.getElementsByTagName(
            'nome')[0].childNodes[0].nodeValue
        name = f'{name}-{state}'
        # print(f'{name}')
        cities_names.append(name)
    return cities_names


if __name__ == '__main__':
    parse_xml()
