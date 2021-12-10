from django.http import HttpResponse

from pybo.models import Question


def index(request):
    questions = Question.objects.order_by('-id')

    html = "<ul>\n"

    for q in questions:
        html += f'<li>{q.id} / {q.create_date} / {q.subject}</li>\n'

    html += "</ul>\n"

    return HttpResponse(html)