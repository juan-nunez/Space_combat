from utility import ImageHelper
import pygame


class MapView:
	def __init__(self, window = None):
		if window == None:
			self.window = pygame.display.get_surface()
		else:
			self.window = window

		self.gameMap = None
		self.players = []
		self.projectiles = []



	def render(self):
		for player in self.players:
			img = self.getPlayerRepresentation(player)
			x = player["location"]["x"]
			y = player["location"]["y"]

			#eventually need x,y to be bounds in a rectangle
			self.window.blit(img,(x,y))

		for projectile in self.projectiles:
			x = projectile["location"]["x"]
			y = projectile["location"]["y"]

			pygame.draw.circle(self.window,(255,255,255),(x,y),10)

		pygame.display.flip()



	def getPlayerRepresentation(self,player):
		direction = player['direction']
		playerId = player['id']
		imgstr = ImageHelper.getShip(playerId,direction)
		return pygame.image.load(imgstr)



	def getMap(self):
		return self.gameMap

	def setMap(self,gameMap):
		self.gameMap = gameMap
		self.players = self.gameMap['players']
		self.projectiles = self.gameMap['projectiles']