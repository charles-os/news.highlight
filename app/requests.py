import urllib.request,json
from .models import News, Articles
#getting the api key
api_key = None

#getting the news base url
base_url = None

#getting the articlces url
articles_url = None



def configure_request(app):
    global api_key,base_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']
    articles_url = app.config['ARTICLES_API_BASE_URL']
    
#getting news through category
def get_news(category):
    '''
    Function that gets the json response to the url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_news(news_results_list)

    return news_results

def process_news(news_list):

    news_results = []

    for source_item in news_list:
        id = source_item.get('id') 
        name = source_item.get('name')
        image = source_item.get("image")
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')


        if source_item:
            news_object = News(id,name,description,url,category,country,language,image)
            news_results.append(news_object)
            

    return news_results

# FETCH ARTICLES, 

def get_articles(id):
    '''
    Function that processes the articles and returns a list of articles objects
    '''
    get_articles_url = articles_url.format(id,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        articles_results = json.loads(url.read())
        
        articles_object = None
        if articles_results['articles']:
            articles_object = process_articles(articles_results['articles'])

    return articles_object
    

# PROCESS ARTICLES
def process_articles(articles_list):
    articles_object = []
    for article_item in articles_list:
        id = article_item.get('id')
        author = article_item.get('author')
        title = article_item.get('title')
        description = article_item.get('description')
        url = article_item.get('url')
        image = article_item.get('urlToImage')
        date = article_item.get('publishedAt')
        
        if image:
            articles_result = Articles(id,author,title,description,url,image,date)
            articles_object.append(articles_result) 
        
    return articles_object