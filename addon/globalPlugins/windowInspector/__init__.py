import globalPluginHandler
import ui
import api
import addonHandler
from .updateChecker import UpdateChecker, show_update_dialog, CURRENT_VERSION

addonHandler.initTranslation()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	
	scriptCategory = _("Window Inspector")

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
		
		winName = fgObj.name if fgObj and fgObj.name else _("[No Window]")
		
		try:
			wClass = focusObj.windowClassName
		except (AttributeError, NotImplementedError):
			wClass = _("[No Class]")
			
		if not wClass:
			wClass = _("[No Class]")

		msg = _("Window: {winName}, class: {wClass}").format(winName=winName, wClass=wClass)
		ui.message(msg)

	script_announceWindowInfo.__doc__ = _("Announces the name of the foreground window and the window class name of the focused object.")

	__gestures = {
		"kb:NVDA+control+shift+d": "announceWindowInfo",
	}
