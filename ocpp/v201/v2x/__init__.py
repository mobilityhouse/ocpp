import os
from ocpp.messages import SchemaValidator, OCPPVersion

schema_path = os.getcwd() + "/schemas"

v2x_validator = SchemaValidator(
    ocpp_version=OCPPVersion.v201, path_to_schemas=schema_path
)
