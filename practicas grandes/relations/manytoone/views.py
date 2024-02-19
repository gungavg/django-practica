from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter,Article
from datetime import date

def create (request):
    rep = Reporter(first_name='jose', last_name='sabedra',email='jose_reportero@gmail.com')
    rep.save()
    
    art1= Article(headline='Lorem ipsum dolot', pub_date=date(2022,5,5), reporter=rep)
    art2= Article(headline='Lorem ipsum dolooooooooot', pub_date=date(2022,10,5), reporter=rep)
    art3= Article(headline='Lorem ipsuuuuuum dolot', pub_date=date(2022,8,5), reporter=rep)
    art1.save()
    art2.save()
    art3.save()
    # query = art1.reporter.first_name
    
    query = rep.article_set.all()
    return HttpResponse(query)