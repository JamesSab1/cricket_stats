from django.shortcuts import render

from . import scrapes


# Tuples to be passed to scrape

div1_batting = ("http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=12179;type=tournament", 15)
div1_bowling = ("http://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=12179;type=tournament", 17)
div2_batting = ("http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=12180;type=tournament", 15)
div2_bowling = ("http://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=12180;type=tournament", 17)
eng_test_batting = ("http://stats.espncricinfo.com/england/engine/records/averages/batting.html?class=1;id=1;type=team", 11)
eng_test_bowling = ("http://stats.espncricinfo.com/england/engine/records/averages/bowling.html?class=1;id=1;type=team", 16)
eng_odi_batting = ("http://stats.espncricinfo.com/england/engine/records/averages/batting.html?class=2;id=1;type=team", 15)
eng_odi_bowling = ("http://stats.espncricinfo.com/england/engine/records/averages/bowling.html?class=2;id=1;type=team", 15)


# Views

def index(request):
    title = 'Cricket Stats'
    context = {'title': title}
    return render(request, 'stats/index.html', context)


def county_div1(request):
    batting_list = scrapes.scrape(*div1_batting)
    bowling_list = scrapes.scrape(*div1_bowling)
    list_range = range(len(batting_list))
    title = 'CC Div 1 Stats'
    context = {'batting_list': batting_list, 'bowling_list': bowling_list, 'list_range': list_range, 'title': title}
    return render(request, 'stats/county.html', context)


def county_div2(request):
    batting_list = scrapes.scrape(*div2_batting)
    bowling_list = scrapes.scrape(*div2_bowling)
    list_range = range(len(batting_list))
    title = 'CC Div 2 Stats'
    context = {'batting_list': batting_list, 'bowling_list': bowling_list, 'list_range': list_range, 'title': title}
    return render(request, 'stats/county.html', context)


def eng_test(request):
    batting_list = scrapes.scrape(*eng_test_batting)
    bowling_list = scrapes.scrape(*eng_test_bowling)
    list_range = range(len(batting_list))
    title = 'England All Time Test Stats'
    context = {'batting_list': batting_list, 'bowling_list': bowling_list, 'list_range': list_range, 'title': title}
    return render(request, 'stats/eng_test.html', context)


def eng_odi(request):
    batting_list = scrapes.scrape(*eng_odi_batting)
    bowling_list = scrapes.scrape(*eng_odi_bowling)
    list_range = range(len(batting_list))
    title = 'England All Time ODI Stats'
    context = {'batting_list': batting_list, 'bowling_list': bowling_list, 'list_range': list_range, 'title': title}
    return render(request, 'stats/eng_odi.html', context)
