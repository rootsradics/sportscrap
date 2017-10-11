class Link():
	streamer_table={
		"acestream":	"acestream://",
		"sopcast":		"sop://broker.sopcast.com:3912/",
		"youtube":		"https://www.youtube.com/watch?v=",
	}
	# lang_table={
		# "englisch":		"anglais",
		# "spanisch":		"espagnol",
		# "ukrainisch":	"ukrainien",
		# "polnisch":		"polonais",
	# }
	
	def __init__(self, streamer, video_id, lang="??", health="?", bitrate="", url="", match=None):
		self.streamer=streamer
		self.video_id=video_id
		self.lang=lang
		self.health=health
		self.bitrate=bitrate
		self.url=url
		self.match=match
		
		self.makeUrl()
		
		
	def makeUrl(self):
		if self.streamer in Link.streamer_table:
			self.url=Link.streamer_table[self.streamer]+self.video_id
		return(self.url)
		
	def makeTitle(self):
		if self.bitrate:
			sBitrate=" [{}]".format(self.bitrate)
		else:
			sBitrate=""
			
		self.title="[{}] {}, {} ({}%){}".format(self.streamer, self.match.name, self.lang, self.health, sBitrate)
		return(self.title)
	
	def getDictForJson(self):
		d=self.__dict__
		d.pop("match", None)
		return(d)