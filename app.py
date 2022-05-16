from flask import Flask, render_template, request

from dto.birthday.birthday_dto import BirthdayDto
from dto.roulette.roulette_dto import RouletteDto
from dto.football.football_dto import FootballDto

from service.birthday.birthday_service import calculate_probability
from service.roulette.roulette_service import RouletteService
from service.football.football_service import footballService, get_teams
from service.football.football_service import footballService, get_team_statistics
from service.football.football_service import footballService, probability_to_win

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


if __name__ == '__main__':
    app.run()
