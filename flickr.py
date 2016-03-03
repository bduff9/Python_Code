import flickrapi, xml.etree.ElementTree, os.path
from urllib import urlretrieve

def get_flickr_images(query=['astley'], num_images=100, target="./tiles/" ):

	# Make sure the target directory exists.
	if not os.path.exists(target):
		os.mkdir(target)

	# this prints information about what images we are downloading
	print("Querying flickr for %d images with tag %s" % (num_images, query))

	# Register our account with Flickr here ################################

	# search for the images here ##########################################

	# determine how many images we actually got.  Take the minimum of the total
	# and the number that was requested. #######################################

	# here we print information about how many images we are downloading
	print "Downloading %s images." % image_count

	# this list contains the paths to all of the images that we download
	paths = []

	# we just use this to keep track of which image is being downloaded.  It's
	# not really that important
	index = 0

	# URL format: http://farm{farm-id}.static.flickr.com/{server-id}/{id}_{secret}_[mstb].jpg
	# We'll grab medium images- they're in need of cropping/resizing, but aren't huge.
	url_format = r"http://farm%s.static.flickr.com/%s/%s_%s_m.jpg"

	# loop through our photos
	for photo in photos_xml:
		# this prints out an informative message.  Some of the image titles cause
		# problems, so we have to catch exceptions
		try:
			print("Downloading %d/%s: %s" % (index, image_count, photo.attrib["title"]))
		except:
			print("Downloading %d/%s" % (index, image_count))

		# form the url based off of photo attributes
		url = url_format % (photo.attrib["farm"], photo.attrib["server"], photo.attrib["id"],
									photo.attrib["secret"])

		# this is the name of the file that the image should be saved to
		filename = "%s/%s.jpg" % (target, photo.attrib["id"])

		# here you want to actually download the image.  Remember doing this in
		# the internet lesson? #################################################

		# create the proper path
		paths.append(os.path.abspath(filename))
		# increment our image index
		index += 1

	# here we need to return the paths of the images #############################
