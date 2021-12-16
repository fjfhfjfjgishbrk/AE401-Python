import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import datetime

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():

    #date
    daysToSearch = 1
    timeAfter = datetime.datetime.utcnow() - datetime.timedelta(days=daysToSearch)






    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret_601321538159-9k284aupk3cdfcehi4r6rq5s1v4eda30.apps.googleusercontent.com.json"
    DEVELOPER_KEY = "AIzaSyCXJc0iUaG6XheQqe8yzao4Uray8ElJ9ZU"
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    # credentials = flow.run_console()
    """youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)"""

    youtube = googleapiclient.discovery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    channelList = ["UCl_gCybOJRIgOXw6Qb4qJzQ", "UCt30jJgChL8qeT9VPadidSw"]

    request = youtube.channelSections().list(
        part="snippet,contentDetails",
        channelId="UCl_gCybOJRIgOXw6Qb4qJzQ"
    )
    response = request.execute()

    channelList.extend(response["items"][7]["contentDetails"]["channels"])

    request = youtube.channelSections().list(
        part="snippet,contentDetails",
        channelId="UCyl1z3jo3XHR1riLFKG5UAg"
    )
    response = request.execute()

    channelList.extend(response["items"][3]["contentDetails"]["channels"])

    for i in channelList:
        haveVid = 0

        request = youtube.channels().list(
            part="snippet,contentDetails,statistics",
            id=i
        )

        response = request.execute()
        recentVid = response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        requestVid = youtube.playlistItems().list(
            part="snippet",
            maxResults=20,
            playlistId=recentVid
        )

        try:
            responseVid = requestVid.execute()
        except googleapiclient.errors.HttpError:
            continue

        for j in responseVid["items"]:
            try:
                if datetime.datetime.fromisoformat(j["snippet"]["publishedAt"][:-1]) > timeAfter:
                    if haveVid == 0:
                        print(response["items"][0]["snippet"]["title"])
                        print()
                        haveVid = 1
                    print(j["snippet"]["title"] + "  https://www.youtube.com/watch?v=" + j["snippet"]["resourceId"]["videoId"])
            except KeyError:
                pass
        if haveVid:
            print()


if __name__ == "__main__":
    main()