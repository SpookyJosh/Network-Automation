#Method to use to tell python script to ignore SSL/TLS warning on an unverified cert

import requests
requests.packages.uurllib3.disable_warnings()