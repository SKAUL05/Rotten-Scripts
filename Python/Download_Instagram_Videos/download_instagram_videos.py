import urllib.request, requests, json, re, sys

def downloadVideo(postId):
    videos = []

    # sending get request and saving the response in the variable url
    url = requests.get(f"https://instagram.com/p/{str(postId)}")

    # checking if the post exists
    if (url.status_code == 404):
        print("Specified post not found")
        exit()

    # extracting data in json format
    jsonData = json.loads(re.findall(r'window._sharedData\s=\s(\{.*\});</script>', url.text)[0])
    data = jsonData['entry_data']['PostPage'][0]['graphql']['shortcode_media']

    multiplePosts = 'edge_sidecar_to_children' in data.keys()
    # checking if the post is a video or not
    isVideo = data['is_video']
    if (not isVideo and not multiplePosts):
        print("No Videos found")
        exit()

    # adding valid videos to the list named videos
    if isVideo:
        videos.append(data['video_url'])
    if multiplePosts:
        videos.extend(
            post['node']['video_url']
            for post in data['edge_sidecar_to_children']['edges']
            if post['node']['is_video']
        )
    # shows the total number of vidoes in the post
    print(f"Found {len(videos)} videos")

    for number, video in zip(list(range(len(videos))), videos):
        print(f"Downloading video {str(number + 1)}")
        urllib.request.urlretrieve(video, f"{postId}_{str(number + 1)}.mp4")

if (len(sys.argv) == 1):
    print("Please enter the ID of the video")
else:
    downloadVideo(sys.argv[1])
