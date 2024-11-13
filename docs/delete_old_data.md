# Deleting Old Data

***

OpenTAKServer can periodically delete old data from the database. This feature can be enabled by an administrator on the
Scheduled Jobs page of the UI. The default settings will delete data (markers, location data, R&B Lines, alerts, CoT messages, and EUDs)
that are older than one week, or EUDs that haven't connected within the last week. This interval can be configured by adding or
changing the following settings in config.yml

- `OTS_DELETE_OLD_DATA_SECONDS` default `0`
- `OTS_DELETE_OLD_DATA_MINUTES` default `0`
- `OTS_DELETE_OLD_DATA_HOURS` default `0`
- `OTS_DELETE_OLD_DATA_DAYS` default `0`
- `OTS_DELETE_OLD_DATA_WEEKS` default `1`

OpenTAKServer will add up these values and delete any data that's older than the interval. For example, if you set
`OTS_DELETE_OLD_DATA` to `2` and `OTS_DELETE_OLD_DATA_DAYS` to `1`, it will delete data older than 2 weeks and 1 day.