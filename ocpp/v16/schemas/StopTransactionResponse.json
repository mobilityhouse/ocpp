{
    "$schema": "http://json-schema.org/draft-04/schema#",
    "title": "StopTransactionResponse",
    "type": "object",
    "properties": {
        "idTagInfo": {
            "type": "object",
            "properties": {
                "expiryDate": {
                    "type": "string",
                    "format": "date-time"
                },
                "parentIdTag": {
                    "type": "string",
                    "maxLength": 20
                },
                "status": {
                    "type": "string",
                    "enum": [
                        "Accepted",
                        "Blocked",
                        "Expired",
                        "Invalid",
                        "ConcurrentTx"
                    ]
                }
            },
            "required": [
                "status"
            ]
        }
    },
    "additionalProperties": false
}
