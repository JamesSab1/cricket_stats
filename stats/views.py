from django.shortcuts import render

from . import scrapes
from .forms import SearchForm

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
    base_url = "http://stats.espncricinfo.com/ci/engine/stats/index.html?"
    cd = {}
    populated_cd = {}
    batting_list = []
    bowling_list = []
    fielding_list = []
    list_range = []
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            populated_cd = {key: value for key, value in cd.items() if value != ' '}

            # change class_type and discipline to class and type
            if populated_cd['class_type']:
                populated_cd['class'] = populated_cd.pop('class_type')
            if populated_cd['discipline']:
                populated_cd['type'] = populated_cd.pop('discipline')

            # build url
            for key, value in populated_cd.items():
                base_url = base_url + key + '=' + value + ';'
            base_url = base_url + 'template=results'

            # scrape depending on case
            if populated_cd['class'] == '1' and populated_cd['type'] == 'batting' and populated_cd['team'] in ('29', '140'):
                batting_list = scrapes.scrape(base_url, 15)
                list_range = range(len(batting_list))
                print(batting_list)
            if populated_cd['class'] == '1' and populated_cd['type'] == 'batting' and populated_cd['team'] in ('9', '25'):
                batting_list = scrapes.scrape(base_url, 16)
                list_range = range(len(batting_list))
                print(batting_list)
            if populated_cd['class'] == '1' and populated_cd['type'] == 'batting':
                batting_list = scrapes.scrape(base_url, 12)
                list_range = range(len(batting_list))
            elif populated_cd['class'] == '2' and populated_cd['type'] == 'batting' and cd['result'] in ('2', '3'):
                batting_list = scrapes.scrape(base_url, 16)
                list_range = range(len(batting_list))
            elif populated_cd['class'] == '2' and populated_cd['type'] == 'batting' and cd['team'] in ('3', '29'):
                batting_list = scrapes.scrape(base_url, 16)
                list_range = range(len(batting_list))
            elif populated_cd['class'] == '2' and populated_cd['type'] == 'batting':
                batting_list = scrapes.scrape(base_url, 14)
                list_range = range(len(batting_list))
            elif populated_cd['class'] == '3' and populated_cd['type'] == 'batting':
                batting_list = scrapes.scrape(base_url, 16)
                list_range = range(len(batting_list))
            elif populated_cd['class'] == '1' and populated_cd['type'] == 'bowling':
                bowling_list = scrapes.scrape(base_url, 15)
                list_range = range(len(bowling_list))
            elif populated_cd['class'] == '2' and populated_cd['type'] == 'bowling' and cd['result'] == '3':
                bowling_list = scrapes.scrape(base_url, 15)
                list_range = range(len(bowling_list))
            elif populated_cd['class'] == '2' and populated_cd['type'] == 'bowling':
                bowling_list = scrapes.scrape(base_url, 14)
                list_range = range(len(bowling_list))
                print(bowling_list)
            elif populated_cd['class'] == '3' and populated_cd['type'] == 'bowling':
                bowling_list = scrapes.scrape(base_url, 15)
                list_range = range(len(bowling_list))
                # edge case where only 1 result doesn't return span - t20 England tie
            elif populated_cd['type'] == 'fielding' and cd['result'] == '3' and populated_cd['class'] == '3':
                fielding_list = scrapes.scrape(base_url, 11)
                list_range = range(len(fielding_list))
                print(fielding_list)
                print(len(list_range))
            elif populated_cd['type'] == 'fielding':
                fielding_list = scrapes.scrape(base_url, 12)
                list_range = range(len(fielding_list))
                print(fielding_list)
                print(len(list_range))

    else:
        form = SearchForm()

    context = {'title': title, 'form': form, 'populated_cd': populated_cd, 'batting_list': batting_list,
               'bowling_list': bowling_list, 'fielding_list': fielding_list, 'list_range': list_range}
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
