from django import forms

TYPE = [(' ', ' '), ('1', 'Test'), ('2', 'Odi'), ('3', 'T20'), ]

TEAMS = [(' ', ' '), ('1', 'England'), ('2', 'Australia'),
         ('3', 'South Africa'), ('4', 'West Indies'),
         ('5', 'New Zealand'), ('6', 'India'), ('7', 'Pakistan'),
         ('8', 'Sri Lanka'), ('9', 'Zimbabwe'),
         ('25', 'Bangladesh'), ('140', 'World XI'),
         ('29', 'Ireland'), ]

DISCIPLINE = [(' ', ' '), ('batting', 'Batting'), ('bowling', 'Bowling'), ('fielding', 'Fielding'), ]

HOME_OR_AWAY = [(' ', ' '), ('1', 'Home'), ('2', 'Away'), ('3', 'Neutral'), ]

RESULT = [(' ', ' '), ('1', 'Win'), ('2', 'Loss'), ('3', 'Tie'), ('4', 'Draw'), ]


class SearchForm(forms.Form):
    class_type = forms.CharField(label='Format', widget=forms.Select(choices=TYPE))
    discipline = forms.CharField(widget=forms.Select(choices=DISCIPLINE))
    team = forms.CharField(widget=forms.Select(choices=TEAMS))
    opposition = forms.CharField(widget=forms.Select(choices=TEAMS))
    home_or_away = forms.CharField(widget=forms.Select(choices=HOME_OR_AWAY))
    #host = forms.CharField(widget=forms.Select(choices=TEAMS))
    ground = forms.CharField(widget=forms.Select(choices=TEAMS))
    dates = forms.CharField(widget=forms.Select(choices=TEAMS))
    season = forms.CharField(widget=forms.Select(choices=TEAMS))
    result = forms.CharField(widget=forms.Select(choices=RESULT))
