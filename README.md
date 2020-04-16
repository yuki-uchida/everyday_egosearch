# init

make

- settings.py and add config
- make google spreadsheet and copy spreadsheet key
  - https://docs.google.com/spreadsheets/d/<<SPREAD SHEET KEY IS HERE>>/edit#gid=0
- make GCP project and service account KEY
  - need activate GOOGLE Spread Sheet API
  - need activate GOOGLE Drive API

```
CREDENTIALS_KEY_FILE = 'XXXXX'
SPREADSHEET_KEY = 'XXX'
EGOSEARCH_QUERIES = {'XXXXX': 'XXXXX lang:ja',
'XXXXX': 'XXXX lang:ja'}
SINCE_DATE = '2020-01-01'
```

# DEPOLY

- `gcloud functions deploy <DEPLOY NAME1> --entry-point <EXECUTE FUNCTION NAME> --runtime python37 --trigger-http --allow-unauthenticated`
- and copy Cloud functions url
- beta scheduler jobs create http <DEPOLY NAME2> --schedule="0 2 \* \* \*" --uri="<CLOUD FUNCTIONS ENTRY POINT URI>" --headers Content-Type=application/json --time-zone=Asia/Tokyo --message-body='{}'
