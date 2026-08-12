$WshShell = New-Object -ComObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut('C:\Users\ravit\OneDrive\Desktop\SATAN Ai - Premium.lnk')
$Shortcut.TargetPath = 'D:\TiTech Prabha Solution\SATAN AI\SATAN AI\SATAN-AI---Lite-main\SATAN-AI---Lite-main\.venv\Scripts\pythonw.exe'
$Shortcut.Arguments = '"D:\TiTech Prabha Solution\SATAN AI\SATAN AI\SATAN-AI---Lite-main\SATAN-AI---Lite-main\main.py"'
$Shortcut.WorkingDirectory = 'D:\TiTech Prabha Solution\SATAN AI\SATAN AI\SATAN-AI---Lite-main\SATAN-AI---Lite-main'
$Shortcut.WindowStyle = 7
$Shortcut.Description = 'Launch SATAN Ai - Premium'
if ('D:\TiTech Prabha Solution\SATAN AI\SATAN AI\SATAN-AI---Lite-main\SATAN-AI---Lite-main\assets\SATAN_Lite_Logo.ico') { $Shortcut.IconLocation = 'D:\TiTech Prabha Solution\SATAN AI\SATAN AI\SATAN-AI---Lite-main\SATAN-AI---Lite-main\assets\SATAN_Lite_Logo.ico,0' }
$Shortcut.Save()