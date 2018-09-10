# Copyright (c) 2018 fieldOfView
# The VersionInTitlebarPlugin is released under the terms of the AGPLv3 or higher.

from UM.Extension import Extension
from UM.Application import Application

class VersionInTitlebarPlugin(Extension):
    def __init__(self):
        super().__init__()

        self._application = Application.getInstance()
        self._version_string = self._application.getVersion()
        self._application.engineCreatedSignal.connect(self._engineCreated)

    def _engineCreated(self):
        # set window title
        try:
        	engine = Application.getInstance()._qml_engine
        except AttributeError:
        	engine = Application.getInstance()._engine
        mainWindow = engine.rootObjects()[0]
        mainWindow.setTitle(mainWindow.title() + " " + self._version_string)

