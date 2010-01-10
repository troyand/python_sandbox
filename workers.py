
def get_title(url):
    """
    get_title -- get the title string of the url
    
    url -- url in the form of 'http://example.com/'

    >>> get_title('http://example.com/')
    u'Example Web Page'
    """

    from BeautifulSoup import BeautifulSoup
    import urllib2
    response = urllib2.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html)
    print '[ok]',url
    return soup.find('title').string


if __name__ == '__main__':
    
    #import doctest
    #doctest.testmod()
    
    import time
    print time.ctime()
    
    from multiprocessing import Pool
    pool = Pool(processes=10)
    urls = [
            'http://www.example.com/',
            'http://ripe.net/',
            'http://www.yandex.ua/',
            'http://usic.org.ua/',
            'http://ukma.kiev.ua/',
            'http://habrahabr.ru/',
            'http://cisco.com/',
            'http://developers.org.ua/',
            'http://plazerazzi.org/',
            ]
    titles = pool.map(get_title, urls)
    
    for pair in zip(urls, titles):
        url, title = pair
        print url, title
    
    print time.ctime()
