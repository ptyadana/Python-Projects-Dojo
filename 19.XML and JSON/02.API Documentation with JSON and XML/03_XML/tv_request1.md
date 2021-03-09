Represents a request to record a television program.

| Element                | Description             | Type            | Required | Notes                                                                                                                                  |
| ---------------------- | ----------------------- | --------------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| recordTV               | Top level               | TV program data | Required |                                                                                                                                        |
| &nbsp; &nbsp; date     | Date of the program     | string          | Optional | Format is YYYY-MM-DD HH:MM:SS. Default value is today's date.                                                                          |
| &nbsp; &nbsp; time     | Time the program begins | number          | Required | Attributes: **format** has values `24` or `12` for 24 or 12 hour formats. Format is HH:MM, with am or pm afterwards for 12 hour format |
| &nbsp; &nbsp; duration | Length of the program   | number          | Required | In hours                                                                                                                               |
| &nbsp; &nbsp; channel  | Channel to record       | number          | Required |                                                                                                                                        |
