import globalPluginHandler
import ui
import api

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	scriptCategory = "Window Inspector"

	def script_announceWindowInfo(self, gesture):
		fgObj = api.getForegroundObject()
		focusObj = api.getFocusObject()
		
		winName = fgObj.name if fgObj and fgObj.name else "[Sem Janela]"
		
		try:
			wClass = focusObj.windowClassName
		except (AttributeError, NotImplementedError):
			wClass = "[Sem Classe]"
			
		if not wClass:
			wClass = "[Sem Classe]"

		msg = "Janela: {}, classe: {}".format(winName, wClass)
		ui.message(msg)

	__gestures = {
		"kb:NVDA+control+shift+d": "announceWindowInfo",
	}
