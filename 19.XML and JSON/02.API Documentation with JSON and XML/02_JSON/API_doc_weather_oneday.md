represents Weather forecast for one day.

| Element     | Description                                                           | Type    | Notes                                                                        |
| ----------- | --------------------------------------------------------------------- | ------- | ---------------------------------------------------------------------------- |
| date        | date of the weather forecast                                          | date    | Format is YYYY-MM-DD                                                         |
| description | text description of weather forecast                                  | string  | Valid values: "sunny", "overcast", "partly cloudy", "raining", and "snowing" |
| maxTemp     | maximum temperature                                                   | number  | in degree Celcius                                                            |
| minTemp     | minimum temperature                                                   | number  | in degree Celcius                                                            |
| windSpeed   | wind speed                                                            | number  | in kilometers per hour                                                       |
| danger      | true if the weather conditions are dangerous; otherwise, false. value | Boolean |                                                                              |
