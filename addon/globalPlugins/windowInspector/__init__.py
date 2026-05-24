import globalPluginHandler
import ui
import api
from .updateChecker import UpdateChecker, show_update_dialog, CURRENT_VERSION

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	scriptCategory = "Window Inspector"

	def __init__(self):
		super(GlobalPlugin, self).__init__()
		self.update_checker = UpdateChecker(
			on_update_available_callback=self._on_update_available
		)
		self.update_checker.start()

	def _on_update_available(self, version, download_url, release_info):
		"""Callback called when an update is available."""
		show_update_dialog(CURRENT_VERSION, version, download_url, release_info)

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
