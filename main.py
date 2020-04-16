# import faulthandler
# faulthandler.enable()
from twitterscraper import query_tweets
from datetime import datetime, timedelta
import urllib.parse
# import os
# os.environ['no_proxy'] = '*'
import gspread
import settings
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    settings.CREDENTIALS_KEY_FILE, scope)
gc = gspread.authorize(credentials)
SPREADSHEET_KEY = settings.SPREADSHEET_KEY
worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

since_date = datetime.strptime(settings.SINCE_DATE, '%Y-%m-%d')


def daterange(start_date, end_date):
    days = (end_date - start_date).days
    for n in range(days):
        yield start_date + timedelta(n), start_date + timedelta(n + 1)


def egosearch(request):
    request_json = request.get_json()
    if 'start_date' in request_json and 'end_date' in request_json:
        start_date = request_json['start_date']
        end_date = request_json['end_date']
    else:
        start_date = None
        end_date = None
    if start_date == None and end_date == None:
        start_date = datetime.today() - timedelta(1)
        end_date = datetime.today()

    for start, end in daterange(start_date, end_date):
        insert_row = (start_date - since_date).days + 2
        worksheet.update_cell(insert_row, 1, str(start.date()))
        insert_column = 2
        for name, query in settings.EGOSEARCH_QUERIES.items():
            tweets = query_tweets(urllib.parse.quote(query),
                                  10000, start.date(), end.date(), 1, '')
            worksheet.update_cell(insert_row, insert_column, len(tweets))
            insert_column += 1


if __name__ == "__main__":
    egosearch()
    # main(datetime.today() - timedelta(1), datetime.today())
