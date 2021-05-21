def downloadLink(url):
    try:
        from pytube import YouTube
    except Exception as e:
        print("some modules are missing {}".format(e))

    ytd = YouTube(url)

    # print(ytd.streams)
    print(ytd.streams.filter(only_audio=True, file_extension='mp4').first().download(output_path='C:/Users/Abdim/Desktop/downloadedFroYT'))

downloadLink("https://www.youtube.com/watch?v=KGD2N5hJ2e0")