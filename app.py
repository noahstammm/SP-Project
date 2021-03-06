import pandas as pd
from flask import Flask, render_template, request
from pandas import DataFrame

import json
import plotly
import plotly.express as px

from dto.birthday.birthday_dto import BirthdayDto
from dto.roulette.roulette_dto import RouletteDto
from dto.football.football_dto import FootballDto

from service.birthday.birthday_service import calculate_probability
from service.roulette.roulette_service import RouletteService
from service.football.football_service import footballService, get_teams, \
    get_season_ids, get_standingsrel_current, get_standingsch_current, get_standingsregular_current, \
    get_standingsregular_last, get_standingsch_last, get_standingsrel_last, get_season_idf
from service.football.football_service import footballService, get_team_statistics
from service.football.football_service import footballService, probability_to_win

app = Flask(__name__)
# Load Configurations
app.config.from_object('config_flask')


@app.route('/')
def home() -> str:
    return render_template(template_name_or_list='index.html')


@app.route('/football')
def football() -> str:
    teams = get_teams()

    return render_template(template_name_or_list='football/football.html', teams=teams)


@app.route('/football/result', methods=['POST'])
def calculate_football():
    team = request.form.get('teams_select')
    team_stat = get_team_statistics(team)
    print(team_stat)
    wins = team_stat[0]
    lost = team_stat[1]
    hint = team_stat[2]
    prob = probability_to_win(wins, lost)

    football_dto = FootballDto(team=team, wins=wins, lost=lost, probability=prob, hint=hint, )

    return render_template(template_name_or_list='football/football_result.html', dto=football_dto)


@app.route('/football/standings')
def standings_football():
    season_all = get_season_ids()

    return render_template(template_name_or_list='football/football_standings.html',
                           tables=[season_all.to_html(classes='data')],
                           titles=season_all.columns.values)


@app.route('/football/standings/result', methods=['POST'])
def standings_football_result():
    l = get_season_idf()

    selected_season = request.form.get('season')

    selected = request.form.get('season_phase')
    df1 = get_standingsregular_last()
    title: str = ""
    text1: str = " "

    if selected_season == 'current':
        if selected == 'tables_regular':
            df1 = get_standingsregular_current()
        elif selected == 'tables_champ':
            df1 = get_standingsch_current()
        elif selected == 'tables_releg':
            df1 = get_standingsrel_current()

    elif selected_season == 'last':
        text1 = "Season 2022/2023 hasn't begun yet"
        if selected == 'tables_regular':
            df1 = get_standingsregular_last()
        elif selected == 'tables_champ':
            df1 = get_standingsch_last()
        elif selected == 'tables_releg':
            df1 = get_standingsrel_last()

    fig = px.bar(df1, x='Played Games', y='Points', color='Name',
                 barmode='group')
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template(template_name_or_list='football/football_standings_result.html',
                           tables=[df1.to_html(classes='data')],
                           titles=df1.columns.values, text=text1, graphJSON=graphJSON)


if __name__ == '__main__':
    app.run()
