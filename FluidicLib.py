from controller import *
from chains import *

class FluidicLib:
	def __init__(self, loadpath):
		self.strands = loadPods(loadpath)
		self.controllers = FluidicControllers(loadpath)
		self.last_update_time = time.time()
		
		self.updateThread = repeatEveryThreaded(1.0/30, self.__update)

	def __update(self):
		t = time.time()
		
		dt = t - self.last_update_time
		self.last_update_time = t
		tween.update(dt)
		self.controllers.updateLedsColors(self.strands)
		self.controllers.updateArtnet()
	

	def stop(self):
		self.updateThread.join()


	def turnOnStrand(self, strandIndex):
		if strandIndex >= len(self.strands) or strandIndex < 0:
			print("turnOnStrand(strandIndex) index out of bounds. index == %d" % (strandIndex) )
			return

		for p in self.strands[strandIndex]:
			p.setOn()


