from django.http import HttpResponse
from django.template import loader
from sensors.models import Store
# Create your views here.


def index(request):
    # get a list of unique topics

    data = []
    template = loader.get_template('sensors/mainpage.html')
    topics = [i['topic'] for i in Store.objects.values("topic").distinct()]
    for topic in topics:
        item = Store.objects.filter(topic__exact=topic).latest()
        tmp = {
            'datetime': item.timestamp,
            'topic': topic,
            'payload': item.payload,
        }
        data.append(tmp)
    context = {
        'sense_items': data,
    }
    return HttpResponse(template.render(context, request))
