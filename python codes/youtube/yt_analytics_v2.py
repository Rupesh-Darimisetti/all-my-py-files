"""
Targeted query reports
Retrieve daily channel statistics

This example calls the YouTube Analytics API to retrieve daily views and other metrics for the authorizing user's channel for the 2017 calendar year. The sample uses the Google APIs Python client library.

The code requests the user's permission to access the https://www.googleapis.com/auth/yt-analytics.readonly scope.

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

Your application might also need to request access to other scopes. For example, an application that calls the YouTube Analytics API and the YouTube Data API might need users to also grant access to their YouTube accounts. The authorization overview identifies scopes typically used in applications that call the YouTube Analytics API.
Set up authorization credentials

Before running this sample locally for the first time, you need to set up authorization credentials for your project:

    Create or select a project in the Google API Console.
    Enable the YouTube Analytics API for your project.
    At the top of the Credentials page, select the OAuth consent screen tab. Select an Email address, enter a Product name if not already set, and click the Save button.
    On the Credentials page, click the Create credentials button and select Oauth client ID.
    Select the application type Other, enter the name "YouTube Analytics API Quickstart", and click the Create button.
    Click OK to dismiss the resulting dialog.
    Click the file_download (Download JSON) button to the right of the client ID.
    Move the downloaded file to your working directory.

Install required libraries

You also need to install the Google APIs Client Library for Python and some additional libraries:

pip install --upgrade google-api-python-client
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

Run the code

Now, you are ready to actually test the sample:

    Copy the code sample below to your working directory.
    In the sample, update the value of the CLIENT_SECRETS_FILE variable to match the location of the file that you downloaded after setting up your authorization credentials.
    Run the sample code in a terminal window:

    python yt_analytics_v2.py

    Go through the authorization flow. The auth flow might automatically load in your browser, or you might need to copy the auth URL into a browser window. At the end of the authorization flow, if necessary, paste the authorization code displayed in the browser into your terminal window and click [return].
    The API query executes and the JSON response is output to the terminal window.

Sample code
"""
# -*- coding: utf-8 -*-

import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/yt-analytics.readonly']

API_SERVICE_NAME = 'youtubeAnalytics'
API_VERSION = 'v2'
CLIENT_SECRETS_FILE = 'YOUR_CLIENT_SECRET_FILE.json'
def get_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def execute_api_request(client_library_function, **kwargs):
  response = client_library_function(
    **kwargs
  ).execute()

  print(response)

if __name__ == '__main__':
  # Disable OAuthlib's HTTPs verification when running locally.
  # *DO NOT* leave this option enabled when running in production.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

  youtubeAnalytics = get_service()
  execute_api_request(
      youtubeAnalytics.reports().query,
      ids='channel==MINE',
      startDate='2017-01-01',
      endDate='2017-12-31',
      metrics='estimatedMinutesWatched,views,likes,subscribersGained',
      dimensions ='day',
      sort='day'
  )
