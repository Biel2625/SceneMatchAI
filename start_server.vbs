Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd %USERPROFILE%\Documents\SceneMatchAI && python server.py", 0
