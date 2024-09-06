import requests
import xml.etree.ElementTree as ET


def get_sites(url):
    sites = []

    # Fetch the sitemap
    response = requests.get(f'{url}/sitemap.xml')
    
    if response.status_code != 200:
        print(f"Failed to fetch sitemap: {response.status_code}")
        return sites

    # Parse the sitemap
    try:
        sitemap = ET.fromstring(response.content)
    except ET.ParseError:
        print("Failed to parse sitemap XML")
        return sites

    # Define the namespace
    namespace = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    # Iterate through all the <loc> elements and extract the URLs
    for url_elem in sitemap.findall(".//sm:loc", namespaces=namespace):
        site_url = url_elem.text
        if site_url:
            sites.append(site_url.strip())

    return sites
