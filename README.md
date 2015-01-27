# Gyroscope

## About 
Gyroscope is a website monitoring and testing tool written in Python 3. It is
configured using two JSON files. One of these, the sites file, contains a list of websites and their pages. Gyroscope 
will cycle through each site and their pages in turn, sending a HTTP request for the address. The following types of 
assets can also be configured for retrieval:

- Images
- External stylesheets
- External scripts

For each page and asset that's retrieved Gyroscope can report the following things to its log output:

- "Nasty" HTTP response messages (currently supported are 400, 403, 404 and 500).
- Responses that take longer than a configured acceptable time in seconds.
- Responses that are bigger than a configured size in kilobytes.
- Any HTTP response that's not either 200 or already handled as a "nasty" response.

Additionally, Gyroscope can be configured to send cookie data and form data when making its request. Gyroscope can be 
configured to request pages a second time if the first request was too slow.

## Dependencies
In addition to Python 3, the following Python libraries are required:

- BeautifulSoup
- jsmin
- urllib3

## Issues, Feature Requests etc.

Please see this project's issue tracker.