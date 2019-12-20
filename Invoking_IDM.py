from subprocess import call

IDM = r'C:\Program Files (x86)\Internet Download Manager\IDMan.exe'
baseUrl='https://ll1.7639616.com'
DownUrl = r'https://secure-appldnld.apple.com/itunes12/091-76333-20180329-6D5B026C-32F7-11E8-A675-99BAB071F5CF/iTunes64Setup.exe'
DownPath = r'J:\T'
OutPutFileName = 'iTunes64Setup.exe'
call([IDM, '/d',DownUrl, '/p',DownPath, '/f', OutPutFileName, '/n', '/a'])