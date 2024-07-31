from pytube import YouTube

# رابط الفيديو على YouTube
video_link = "https://www.youtube.com/watch?v=YWv2lDLSczk"

try:
    # إنشاء كائن YouTube للفيديو
    youtube_video = YouTube(url=video_link)

    # طباعة معلومات عن الفيديو (اختياري)
    print(f"Title: {youtube_video.title}")
    print(f"Publish Date: {youtube_video.publish_date}")
    print(f"Author: {youtube_video.author}")
    print(f"Thumbnail: {youtube_video.thumbnail_url}")
    print(f"Views: {youtube_video.views} Views")

except Exception as e:
    print(f"An error occurred: {e}")
