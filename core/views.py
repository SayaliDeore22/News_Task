
import requests
from django.shortcuts import render
from .models import Search


def search_articles(request):
    if request.method == 'POST':
        keyword = request.POST.get('keyword')

        # Save the search keyword to the database
        Search.objects.create(keyword=keyword)

        # Fetch news articles from the API
        api_key = 'dc5aabde798c4cd38695cdc085ba9a7a'
        url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
        response = requests.get(url)
        articles = response.json().get('articles', [])

        context = {
            'keyword': keyword,
            'articles': articles
        }
        return render(request, 'search_results.html', context)

    return render(request, 'search_form.html')

def search_history(request):
    searches = Search.objects.all().order_by('-timestamp')
    return render(request, 'search_history.html', {'searches': searches})
