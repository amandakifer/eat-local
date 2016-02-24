#Yelp Search API
import json
import oauth2
import os
import urllib
import urllib2


class Yelp:

    API_HOST = 'api.yelp.com'
    SEARCH_LIMIT = 10
    SEARCH_PATH = '/v2/search/'

    def __init__(self):
        # OAuth credential placeholders that must be filled in by users.
        self.CONSUMER_KEY = os.environ.get('YELP_CONSUMER_KEY')
        self.CONSUMER_SECRET = os.environ.get('YELP_CONSUMER_SECRET')
        self.TOKEN = os.environ.get('YELP_TOKEN')
        self.TOKEN_SECRET = os.environ.get('YELP_TOKEN_SECRET')

    def request(self, host, path, url_params=None):
        """Prepares OAuth authentication and sends the request to the API.

        Args:
            host (str): The domain host of the API.
            path (str): The path of the API after the domain.
            url_params (dict): An optional set of query parameters in the request.

        Returns:
            dict: The JSON response from the request.

        Raises:
            urllib2.HTTPError: An error occurs from the HTTP request.
        """
        url_params = url_params or {}
        url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

        consumer = oauth2.Consumer(self.CONSUMER_KEY, self.CONSUMER_SECRET)
        oauth_request = oauth2.Request(
            method="GET", url=url, parameters=url_params)

        oauth_request.update(
            {
                'oauth_nonce': oauth2.generate_nonce(),
                'oauth_timestamp': oauth2.generate_timestamp(),
                'oauth_token': self.TOKEN,
                'oauth_consumer_key': self.CONSUMER_KEY
            }
        )
        token = oauth2.Token(self.TOKEN, self.TOKEN_SECRET)
        oauth_request.sign_request(
            oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
        signed_url = oauth_request.to_url()

        print u'Querying {0} ...'.format(url)

        conn = urllib2.urlopen(signed_url, None)
        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

        return response

    def search(self, term, location, deals_filter=False):
        """Query the Search API by a search term and location.

        Args:
            term (str): The search term passed to the API.
            location (str): The search location passed to the API.
            deals_filter (bool): Set true to search for deals

        Returns:
            dict: The JSON response from the request.
        """

        url_params = {
            'term': urllib.quote_plus(term),
            'location': urllib.quote_plus(location),
            'deals_filter': deals_filter,
            'limit': self.SEARCH_LIMIT
        }
        return self.request(self.API_HOST, self.SEARCH_PATH, url_params=url_params)
