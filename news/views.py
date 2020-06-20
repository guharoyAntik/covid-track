from django.shortcuts import render
from newsapi.newsapi_client import NewsApiClient
import requests



def news(request):
	newsapi = NewsApiClient(api_key='149dd9c6ff0c47cfae0d743f73171729')

	news = newsapi.get_everything(q='covid', language='en')
	articles = news['articles']

	desc = []
	news = []
	img = []
	url = []

	for article in articles:
		news.append(article['title'])
		desc.append(article['description'])
		img.append(article['urlToImage'])
		url.append(article['url'])

	newslist = zip(news, desc, img, url)
	context = {"newslist": newslist}

	return render(request, template_name='news.html', context=context)

