# -*- coding: utf-8 -*-
import sys
import libbrjsonparser as libBrJsonParser
from libmediathek4 import lm4

class libbr(lm4):
	def __init__(self):
		self.parser = libBrJsonParser.parser()
		self.channels = {'ARD-Alpha':'ARD_alpha', 
			'BR':'BR_Fernsehen', 
			'BRde':'BRde'
			}

		self.defaultMode = 'libBrListMain'

		self.modes = {
			'libBrListMain': self.libBrListMain,
			'libBrListNew': self.libBrListNew,
			'libBrListSeries': self.libBrListSeries,
			'libBrListEpisodes': self.libBrListEpisodes,
			'libBrListBoards': self.libBrListBoards,
			'libBrListBoard': self.libBrListBoard,
			'libBrListCategories': self.libBrListCategories,
			'libBrListCategory': self.libBrListCategory,
			'libBrListGenres': self.libBrListGenres,
			'libBrListGenre': self.libBrListGenre,
			'libBrListSections': self.libBrListSections,
			'libBrListSection': self.libBrListSection,
			'libBrListChannel': self.libBrListChannel,
			'libBrListChannelDate': self.libBrListChannelDate,
			'libBrListChannelDateVideos': self.libBrListChannelDateVideos,
			'libBrSearch': self.libBrSearch,
			'libBrListSearch': self.libBrListSearch,
		}

		self.playbackModes = {
			'libBrPlay':self.libBrPlay,
			'libBrPlayOld':self.libBrPlayOld,
			}
	
	def libBrListMain(self):
		l = []
		#l.append({'metadata':{'name':self.translation(32030)}, 'params':{'mode':'libBrListNew'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32132)}, 'params':{'mode':'libBrListSeries'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32133)}, 'params':{'mode':'libBrListChannel'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32134)}, 'params':{'mode':'libBrListBoards'}, 'type':'dir'})
		l.append({'metadata':{'name':self.translation(32135)}, 'params':{'mode':'libBrListCategories'}, 'type':'dir'})
		#l.append({'metadata':{'name':self.translation(32039)}, 'params':{'mode':'libBrSearch'}, 'type':'dir'})
		return {'items':l,'name':'root'}
	
	def libBrListNew(self):
		return self.parser.parseNew()
			
	def libBrListSeries(self):
		#libMediathek.sortAZ()
		return self.parser.parseSeries()
	def libBrListEpisodes(self):
		return self.parser.parseEpisodes(self.params['id'])

	def libBrListBoards(self):
		return self.parser.parseBoards()	
	def libBrListBoard(self):
		return self.parser.parseBoard(self.params['boardId'])

	def libBrListCategories(self):
		return self.parser.parseCategories()
	def libBrListCategory(self):
		return self.parser.parseCategory(self.params['id'])

	def libBrListGenres(self):
		return self.parser.parseGenres()
	def libBrListGenre(self):
		return self.parser.parseGenre(self.params['id'])
		
	def libBrListSections(self):
		#libMediathek.sortAZ()
		return self.parser.parseSections()
	def libBrListSection(self):
		return self.parser.parseSection(self.params['id'])

	def libBrListVideos2(self):
		return self.parser.parseLinks(self.params['url'])

	def libBrListChannel(self):
		l = []
		for channelName,channel in self.channels.items():
			l.append({'metadata':{'name':channelName}, 'params':{'mode':'libBrListChannelDate','channel':channel}, 'type':'dir'})
		return {'items':l,'name':'libBrListChannel'}

	def libBrListChannelDate(self):
		return
		#return libMediathek.populateDirDate('libBrListChannelDateVideos',params['channel'],True)
		
	def libBrListChannelDateVideos(self):
		#xdatum = date.today() - timedelta(int(params['datum']))
		return self.parser.parseDate(self.params['yyyymmdd'],self.params['channel'])#params['datum'] =yyyy-mm-dd
		#return self.parser.parseDate(datum.strftime('%Y-%m-%d'),params['channel'])#params['datum'] =yyyy-mm-dd
		
	def libBrSearch(self):
		#search_string = libMediathek.getSearchString()
		return self.parser.parseSearch(search_string)
		#return libBrListSearch(search_string)

	def libBrListSearch(self,searchString=False):
		if not searchString:
			searchString = self.params['searchString']
		return search(searchString)
		
	def libBrPlay(self):
		return self.parser.parseVideo(self.params['id'])
		
	def libBrPlayOld():
		return self.parser.parseVideoOld(self.params['url'])
		
		
		