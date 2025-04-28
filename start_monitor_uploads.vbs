Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "cmd /c cd %USERPROFILE%\Documents\SceneMatchAI && python monitor_uploads.py", 0
Set WshShell = Nothing
