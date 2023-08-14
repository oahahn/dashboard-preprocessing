import os
from googleapiclient.http import MediaIoBaseDownload
from http.client import IncompleteRead
from googleapiclient.errors import HttpError
import io
from collections import defaultdict
from oauth2client import file, client, tools
from googleapiclient import discovery
from httplib2 import Http


def download_files():
    DRIVE = get_gdrive_connection()

    # airdata
    destination_path = 'old-csvs/airdata_matches.csv'
    file_id = '1hjYBPm6wNBgdgHEgFVMDS_zfrQ0CXf5z'
    do_download(destination_path, DRIVE, file_id)

    # det_match
    destination_path = 'old-csvs/det_match.csv'
    file_id = '17MX-QbCDyP8UBAQCAtJv5pv0Dg0I74lQ'
    do_download(destination_path, DRIVE, file_id)

    # kml_matches
    destination_path = 'old-csvs/kml_matches.csv'
    file_id = '1c9usVJVJFkLqyAh1IFMcwu805oizYYIV'
    do_download(destination_path, DRIVE, file_id)

    # location_dataframe
    destination_path = 'old-csvs/location_dataframe.csv'
    file_id = '1PTw7C8o-uFq-edJM0URTsSpvQ-BVW6w7'
    do_download(destination_path, DRIVE, file_id)

    # survey_match
    destination_path = 'old-csvs/survey_match.csv'
    file_id = '10ZDOIF2bnIJ-cRJFCNQ3Jzg08rP1lxYa'
    do_download(destination_path, DRIVE, file_id)

    # video_matches
    destination_path = 'old-csvs/video_matches.csv'
    file_id = '1WBjegH1Z6xP2BjQ70LTCmPUvhRJwVkQa'
    do_download(destination_path, DRIVE, file_id)


def do_download(destination_path, DRIVE, file_id, file_sha1=None, hash_store=defaultdict(str), hash_store_file='',
                test=False):
    '''
    Download the file
    '''
    folder_path = os.path.dirname(destination_path)
    os.makedirs(folder_path, exist_ok=True)
    if os.path.exists(destination_path):
        print(f'update {destination_path},{file_sha1} {hash_store[destination_path]}')
    else:
        print(f'dl {destination_path}')
    file_contents = download_file(DRIVE, file_id)
    if file_contents is not None:
        with open(destination_path, 'wb') as write:
            write.write(file_contents.getvalue())
        if hash_store_file != '':
            add_hash(destination_path, hash_store_file, file_sha1)
    else:
        print(f'skipping non-binary doc {destination_path}')
    return True

def download_file(DRIVE, file_id):
    """Downloads a file
    Args:
        file_id: ID of the file to download
    Returns : IO object with location.
    Load pre-authorized user credentials from the environment.
    TODO(developer) - See https://developers.google.com/identity
    for guides on implementing OAuth2 for the application.
    """

    try:
        request = DRIVE.files().get_media(fileId=file_id)
        file = io.BytesIO()
        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            print(F'Download {int(status.progress() * 100)}.')

    except HttpError as error:
        print(f'HTTP error occurred: {error}, with file {file_id}')
        file = None
    except IncompleteRead as error:
        print(f'IncompleteRead error occurred: {error}, with file {file_id}')
        file = None

    return file


def add_hash(destination_path, hash_store_file, file_sha1):
    with open(hash_store_file, 'a') as hash_write:
        hash_write.writelines(
            f'{file_sha1}  {destination_path}\n')


def get_gdrive_connection():
    '''actually provides the connection to the API for use elsewhere'''
    creds = generate_credentials()
    DRIVE = discovery.build('drive', 'v3', http=creds.authorize(Http()))
    return DRIVE


def generate_credentials():
    '''Handles login, and then passes on credentials for the connection to be started'''
    SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
    if not os.path.exists('storage.json') and os.path.exists('~/storage.json'):
        store = file.Storage('~/storage.json')
    else:
        store = file.Storage('storage.json')
    creds = store.get()
    # Get credentials according to either https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
    # or https://codelabs.developers.google.com/codelabs/gsuite-apis-intro/#6
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_id.json', SCOPES)
        creds = tools.run_flow(flow, store)
    return creds


if __name__ == '__main__':
    download_files()
