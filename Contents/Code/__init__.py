TITLE = 'Streamer'
ART    = 'art-default.jpg'
ICON   = 'icon-default.png'

PREFIX = '/video/streamer'

################################################
def Start():

	ObjectContainer.title1 = TITLE
	ObjectContainer.art = R(ART)
	DirectoryObject.art = R(ART)
	DirectoryObject.thumb = R(ICON)

#################################################
@handler(PREFIX, TITLE)
def MainMenu():
	oc = ObjectContainer()

	oc.add(CreateItemObject(
		url = 'http://192.168.0.106/cgi-bin/nph-zms?mode=jpeg&monitor=1&scale=100&maxfps=5&buffer=1000&user=Viewer&pass=rAMjwbeSiiyuLnApBz8X',
		title = L('Play stream')
	))

	return oc

################################################
def CreateItemObject(url, title, include_container=False):
	item = VideoClipObject(
		key = Callback(CreateItemObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(Play, url=url))
				],
			            video_resolution = '480',
			            video_codec = VideoCodec.H264,
			            audio_codec = AudioCodec.AAC,
			            audio_channels = 2,
			            optimized_for_streaming = True,
			)
		]
	)


	if include_container:
		return ObjectContainer(objects=[item])
	else:
		return item

################################################
def Play(url):
	return Redirect(url)
