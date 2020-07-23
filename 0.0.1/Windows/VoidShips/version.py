with open("version.txt", 'r') as f:
	global major, minor, patch, build
	major, minor, patch, build = f.read().strip().split('.')
	major, minor, patch, build = int(major), int(minor), int(patch), int(build)

def save():
	version = str(major)+'.'+str(minor)+'.'+str(patch)+'.'+str(build)
	with open("version.txt", 'w') as f:
		f.write(version)

def get_version():
	return str(major)+'.'+str(minor)+'.'+str(patch)+'.'+str(build)

def get_public_version():
	return str(major)+'.'+str(minor)+'.'+str(patch)

def bump_major():
	global major, minor
	print("bumping major")
	major +=1
	minor = 0
	save()
def bump_minor():
	global minor
	print("bumping minor")
	minor +=1
	save()
def bump_patch():
	global patch
	print("bumping patch")
	patch +=1
	save()
def bump_build():
	global build
	print("bumping build")
	build +=1
	save()
