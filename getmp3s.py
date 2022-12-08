import requests
import urllib

def getMP3(url):
	r = requests.get(url, allow_redirects=True)
	name = getName(url)
	with open(name, 'wb') as f:
		f.write(r.content)

def getName(url):
	l = url.split('/')
	s = urllib.parse.unquote(l[-1])
	return s

def getLinks(s):
	l = []
	content = s.split('\n')
	for line in content:
		if '.mp3\"' in line:
			idx = line.index('http')
			s = line[idx:]
			idx = s.index('"')
			s = s[:idx]
			l.append(s)
	return l

def getMP3sFromFile(filename):
	print(f'Processing file {filename} ...')
	with open(filename, 'r') as f:
		s = f.read()
	l = getLinks(s)
	print(f'Found {len(l)} elements.')
	for link in l:
		print(f'Downloading {link} ...')
		getMP3(link)
	print('Done!')

def getMP3sFromWeb(url):
	print(f'Processing Web {url} ...')
	r = requests.get(url, allow_redirects=True)
	s = str(r.content, 'UTF-8')
	l = getLinks(s)
	print(f'Found {len(l)} elements.')
	for link in l:
		print(f'Downloading {link} ...')
		getMP3(link)
	print('Done!')

getMP3sFromFile('web.html')
#getMP3sFromWeb('https://vgmrips.net/packs/pack/out-run-arcade')