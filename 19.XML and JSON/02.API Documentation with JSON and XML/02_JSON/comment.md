Represents a comment on a posting.

| Element            | Description                                 | Type                | Required | Note                                                                            |
| ------------------ | ------------------------------------------- | ------------------- | -------- | ------------------------------------------------------------------------------- |
| Commment           | Top Level                                   | comment data object | Required |                                                                                 |
| &nbsp;&nbsp;userId | ID of user making a comment                 | string              | Required |                                                                                 |
| &nbsp;&nbsp;discID | ID of Discussion that is being commented on | string              | Required |                                                                                 |
| &nbsp;&nbsp;time   | Time that comment is posted                 | string              | Optional |                                                                                 |
| &nbsp;&nbsp;discID | ID of Discussion making a comment           | string              | Optional | YYYY-MM-DD HH:MM:SS GMT. Default is the time the comment is received by server. |
| &nbsp;&nbsp;text   | text of comment                             | string              | Required |                                                                                 |
