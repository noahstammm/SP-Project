import pandas as pd
from flask import Flask, render_template, request

from dto.birthday.birthday_dto import BirthdayDto
from dto.roulette.roulette_dto import RouletteDto
from dto.football.football_dto import FootballDto

from service.birthday.birthday_service import calculate_probability
from service.roulette.roulette_service import RouletteService
from service.football.football_service import footballService, get_teams, get_standingsch, get_standingsrel
from service.football.football_service import footballService, get_team_statistics
from service.football.football_service import footballService, probability_to_win
from service.football.football_service import footballService, get_standingsregular

app = Flask(__name__)
# Load Configurations
app.config.from_object('config_flask')


@app.route('/')
def home() -> str:
    return render_template(template_name_or_list='index.html')


@app.route('/roulette')
def roulette() -> str:
    return render_template(template_name_or_list='roulette/roulette.html')


@app.route('/roulette/result', methods=['POST'])
def calculate_roulette() -> str:
    budget = int(request.form['budget'])
    bet = int(request.form['bet'])
    service = RouletteService(budget=budget, bet=bet)
    amount_rounds = service.play()
    roulette_dto = RouletteDto(budget=budget, bet=bet, amount_rounds=amount_rounds)
    return render_template(template_name_or_list='roulette/roulette_result.html', dto=roulette_dto)


@app.route('/birthday')
def birthday() -> str:
    return render_template(template_name_or_list='birthday/birthday.html')


@app.route('/birthday/result', methods=['POST'])
def calculate_birthday() -> str:
    amount_people = int(request.form['amount_people'])
    probability = calculate_probability(amount_people=amount_people)
    birthday_dto = BirthdayDto(amount_people=amount_people, probability=probability)
    return render_template(template_name_or_list='birthday/birthday_result.html', dto=birthday_dto)


@app.route('/football')
def football() -> str:
    teams = get_teams()
    print(teams)
    return render_template(template_name_or_list='football/football.html', teams=teams)


@app.route('/football/result', methods=['POST'])
def calculate_football():
    print("------------  results are calculated -----------------")
    team = request.form.get('teams_select')
    team_stat = get_team_statistics(team)
    wins = team_stat[2]
    lost = team_stat[3]
    prob = probability_to_win(wins, lost)
    football_dto = FootballDto(team=team, wins=wins, lost=lost, probability=prob)

    return render_template(template_name_or_list='football/football_result.html', dto=football_dto)


@app.route('/football/standings')
def standings_football():
    df_regular = get_standingsregular()
    df_champ = get_standingsch()
    df_releg = get_standingsrel()

    return render_template(template_name_or_list='football/football_standings.html',
                           tables_regular=[df_regular.to_html(classes='data')],
                           titles_regular=df_regular.columns.values,
                           tables_champ=[df_champ.to_html(classes="data")], titles_champ=df_champ.columns.values,
                           tables_releg=[df_releg.to_html(classes='data')], titles_releg=df_releg.columns.values)


@app.route('/football/standings/result', methods=['GET'])
def standings_football_result():
    selected = request.args.get('season_phase')
    df
    if selected == 'tables_regular':
        df = get_standingsregular()

    elif selected == 'tables_champ':
        df = get_standingsch()

    elif selected == 'tables_releg':
        df = get_standingsrel()

    return render_template(template_name_or_list='football/football_standings.html',
                           tables=[df.to_html(classes='data')],
                           titles=df.columns.values)


if __name__ == '__main__':
    app.run()
