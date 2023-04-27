import pathlib

import yaml

from investement import RealEstate, Stock

def load_definition_file(investement_type: str):
    definition_path = ""

    with open(definition_path, 'r') as file:
        yaml_data = file.read()

    parsed_data = yaml.load(yaml_data, Loader=yaml.FullLoader)
    return parsed_data


class InvestmentFactory:
    def get_investment(self, investment_type: str, **kwargs):
        if investment_type == "real_estate":
            return self.real_estate(**kwargs)
        elif investment_type == "stock":
            return self.stock(**kwargs)

    def real_estate(self, **kwargs):
        return RealEstate(**kwargs)

    def stock(self, **kwargs):
        return Stock(**kwargs)
