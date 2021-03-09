Represents a request for a meeting in a calendar.

| Element                   | Description                                                            | Type                | Required | Notes                                                                   |
| ------------------------- | ---------------------------------------------------------------------- | ------------------- | -------- | ----------------------------------------------------------------------- |
| meeting                   | Top level                                                              | meeting data object | Required |                                                                         |
| &nbsp; &nbsp; time        | When meeting starts.                                                   | string              | Required | Format is YYYY-MM-DD HH:MM:SS. Timezone is GMT.                         |
| &nbsp; &nbsp; duration    | How long meeting lasts                                                 | number              | Required | In minutes                                                              |
| &nbsp; &nbsp; description | Description of the meeting                                             | string              | Required |                                                                         |
| &nbsp; &nbsp; location    | Location of the meeting                                                | number              | Optional | Default is an empty string                                              |
| &nbsp; &nbsp; reminder    | How many minutes before the meeting a reminder event should take place | number              | Optional | Default is 10 minutes                                                   |
| &nbsp; &nbsp; invitees    | List of email address of people to invite to the meeting               | array of string     | Optional | The strings should be valid email addresses. Default is an empty array. |
