Represents a request to record a television program.

| Element                | Attribute | Description                                    | Type            | Required | Notes                                                        |
| ---------------------- | --------- | ---------------------------------------------- | --------------- | -------- | ------------------------------------------------------------ |
| recordTV               |           | Top level                                      | TV program data | Required |                                                              |
| &nbsp; &nbsp; when     |           | Date and time when the program starts          |                 | Required |                                                              |
|                        | date      | Date                                           | string          | Optional | Format is YYYY-MM-DD. Default value is today's date.         |
|                        | time      | Time the program begins                        | string          | Required | Format is HH:MM, with am or pm afterwards for 12 hour format |
|                        | format    | Format for the time: either 12 hour or 24 hour | string          | Required | Valid values: `24` or `12`                                   |
| &nbsp; &nbsp; duration | hours     | Length of the program                          | number          | Required | In hours                                                     |
| &nbsp; &nbsp; station  | channel   | Channel to record                              | number          | Required |                                                              |
