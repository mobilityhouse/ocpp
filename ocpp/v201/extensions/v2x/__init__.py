import pathlib

from ocpp.messages import SchemaValidator

schema_path = str(pathlib.Path(__file__).parent.joinpath("schemas").resolve())
v2x_validator = SchemaValidator(path_to_schemas=schema_path)
