represents Weather forecast for multiple days.

| Element                 | Description                                                           | Type                             | Notes                                                                        |
| ----------------------- | --------------------------------------------------------------------- | -------------------------------- | ---------------------------------------------------------------------------- |
| longtitude              | longtitude of the location where weather forecast takes place         | Number                           |                                                                              |
| latitude                | latitude of the location where weather forecast takes forecasted      | Number                           |                                                                              |
| forecasts               | daily forecasts                                                       | array of daily forecast objectss |
| &nbsp;&nbsp;date        | date of the weather forecast                                          | date                             | Format is YYYY-MM-DD                                                         |
| &nbsp;&nbsp;description | text description of weather forecast                                  | string                           | Valid values: "sunny", "overcast", "partly cloudy", "raining", and "snowing" |
| &nbsp;&nbsp;maxTemp     | maximum temperature                                                   | number                           | in degree Celcius                                                            |
| &nbsp;&nbsp;minTemp     | minimum temperature                                                   | number                           | in degree Celcius                                                            |
| &nbsp;&nbsp;windSpeed   | wind speed                                                            | number                           | in kilometers per hour                                                       |
| &nbsp;&nbsp;danger      | true if the weather conditions are dangerous; otherwise, false. value | Boolean                          |                                                                              |
