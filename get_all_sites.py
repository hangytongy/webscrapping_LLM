import requests
import xml.etree.ElementTree as ET


def get_sites(url):

    sites = []

    # Fetch the sitemap
    response = requests.get(f'{url}/sitemap.xml')

    # Parse the sitemap
    sitemap = ET.fromstring(response.content)

    # Iterate through all the <loc> elements and print the URLs
    for urls in sitemap.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc"):
        sites.append(urls)
    
    return sites
