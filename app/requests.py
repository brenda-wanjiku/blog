import urllib.request, json
from .models import Quote


def get_quotes():
    quote_url ='http://quotes.stormconsultancy.co.uk/random.json'
    ''' 
    Function that gets json response for the url request
    '''
    with urllib.request.urlopen(quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        quote_results = None

        if quote_response:
            quote_results = process_quotes(quote_response)

        return quote_results

def process_quotes(quote_item):
    '''
    Function  that processes the sources result and transform them to a list of Objects
    Args:
        sources_list: A list of dictionaries that contain sources details
    Returns :
        sources_results: A list of sources objects
    '''
    id = quote_item.get('id')
    author = quote_item.get('author')
    quote = quote_item.get('quote')

    quote_object = Quote(id,author, quote)

    return quote_object
        
