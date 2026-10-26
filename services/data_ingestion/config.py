
import yaml

# function that turns that YAML file into a list the rest of the code can use.


def load_instruments(path):
    with open(path) as f:
        data = yaml.safe_load(f)
    return data["instruments"]