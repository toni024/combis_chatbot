import logging
import requests

log = logging.getLogger('test.log')

def fetch_google_places(latitude, longitude, radius, content_type, keyword):
	api_key='AIzaSyB2T3V59a4UT2--vEUKw-KVI78lueAy9ds'
	url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+latitude+','+longitude+'&radius='+radius+'&type='+content_type+'&keyword='+keyword+'&key=AIzaSyB2T3V59a4UT2--vEUKw-KVI78lueAy9ds'
	response = requests.get(url)
	return response

if __name__ == "__main__":
    latitude = sys.argv[1]
    longitude = sys.argv[2]
    radius = sys.argv[3]
    content_type = sys.argv[4]
    keyword = sys.argv[5]
    print(fetch_google_places(latitude,longitude,radius,content_type,keyword))
