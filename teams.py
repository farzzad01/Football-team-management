
class Person:
    def __init__(self):
        self.fname = []
        self.lname = []
        self.idcode = []
        self.birthdate = []

    def read_fname(self):
        self.fname = input("Enter first name: ")

    def read_lname(self):
        self.lname = input("Enter last name: ")

    def read_idcode(self):
        self.idcode = input("Enter ID code: ")

    def read_birthdate(self):
        self.birthdate = input("Enter birthdate (): ")

    def show_fullname(self):
        print("Full name:", self.fname, self.lname)

    def show_idcode(self):
        print("ID code:", self.idcode)

    def show_birthdate(self):
        print("Birthdate:", self.birthdate)


class Player(Person):
    def __init__(self):
        super().__init__()
        self.post = []
        self.goal = []

    def read_post(self):
        self.post = input("Enter player's post: ")
    
    def show_post(self):
        print('player post is ', self.post)
    
    def read_goal(self):
        self.goal = input('enter player goals')

    def show_player_info(self):
        super().show_fullname()
        super().show_idcode()
        super().show_birthdate()
        print("post:", self.post)
    
    def read_palyer_info(self):
        self.read_fname
        self.read_lname
        self.read_idcode
        self.read_birthdate
        self.read_post
    
    def show_coach_info(self):
        print(self.show_fullname)
        print(self.show_idcode)
        print(self.show_birthdate)
        print(self.show_post)

        


class Coach(Person):
    def __init__(self):
        super().__init__()
        self.card_type = []

    def read_card_type(self):
        self.card_type = input("Enter card type (A, B, C): ")

    def show_card_type(self):
        print("Card type:", self.card_type)
    
    def show_caoch_info(self):
        super().show_fullname()
        super().show_idcode()
        super().show_birthdate()
        print("post:", self.card_type)

    def read_coach_info(self):
        self.read_fname
        self.read_lname
        self.read_birthdate
        self.read_card_type
        self.read_idcode
    
    def show_coach_info(self):
        print(self.show_fullname)
        print(self.show_idcode)
        print(self.show_birthdate)
        print(self.show_card_type)



class Team:
    def __init__(self):
        self.team_name = []
        self.team_code = []
        self.players = []
        self.coach = Coach()

    def read_team_name(self):
        self.team_name = input("Enter team name: ")

    def read_team_code(self):
        self.team_code = input("Enter team code: ")

    def show_team_name(self):
        print("Team name:", self.team_name)

    def show_team_code(self):
        print("Team code:", self.team_code)

    def read_team_info(self):
        self.read_team_name()
        self.read_team_code()
        print("---------------------------")
        print("Coach Info:")
        self.coach.read_fname()
        self.coach.read_lname()
        self.coach.read_idcode()
        self.coach.read_birthdate()
        self.coach.read_card_type()
        print("---------------------------")
        num_players = int(input("Enter the number of players in the team: "))
        for i in range(num_players):
            print("Player", i+1, "Info:")
            player = Player()
            player.read_fname()
            player.read_lname()
            player.read_idcode()
            player.read_birthdate()
            player.read_post()
            self.players.append(player)
            print("---------------------------")

    def show_team_info(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.show_team_name()
        self.show_team_code()
        print("\n---------------------------")
        print("Coach Info:")
        self.coach.show_fullname()
        self.coach.show_idcode()
        self.coach.show_birthdate()
        self.coach.show_card_type()
        print("\n---------------------------")
        for i, player in enumerate(self.players):
            print("\nPlayer", i+1, "Info:")
            player.show_player_info()
            print("\n---------------------------")

    class Team:
        MAX_PLAYERS_PER_TEAM = 11

        def transfer_player(self, player, new_team):
            if player in self.players:
                if len(new_team.players) < MAX_PLAYERS_PER_TEAM:
                    self.players.remove(player)
                    new_team.players.append(player)
                    player.team = new_team
                    print(f"Player {player.fname} {player.lname} transferred from {self.team_name} to {new_team.team_name}.")
                    return True
                else:
                    print(f"The new team {new_team.team_name} has reached the maximum number of players.")
            else:
                print(f"Player {player.fname} {player.lname} is not in {self.team_name}.")

            return False




class League:
    def __init__(self):
        self.teams = []

    def read_team_info(self):
        team = Team()
        team.read_team_info()
        self.teams.append(team)

    def display_all_teams(self):
        for team in self.teams:
            team.show_team_info()

    def display_team_by_code(self):
        code = input("Enter team's code: ")
        found = False
        for team in self.teams:
            if team.team_code == code:
                team.show_team_info()
                found = True
                break
        if not found:
            print("No team found with that code.")


    def display_team_by_coach(self):
        id_code = input("Enter coach's ID code: ")
        found = False
        for team in self.teams:
            if team.coach.idcode == id_code:
                team.show_team_name()
                found = True
                break
        if not found:
            print("No coach found with that ID code.")


    def display_team_by_player(self):
        id_code = input("Enter player's ID code: ")
        found = False
        for team in self.teams:
            for player in team.players:
                if player.idcode == id_code:
                    team.show_team_name()
                    found = True
                    break
            if found:
                break
        if not found:
            print("No player found with that ID code.")


    def display_players_by_name(self):
        for team in self.teams:
            for player in team.players:
                if player.fname.lower() == "ali":
                    print(player.fname, player.lname, "(", team.team_name, ")")
                    print("---------------------")
        print("*************************")


    def display_players_over_30(self):
        current_year = 2023
        for team in self.teams:
            for Player in team.players:
                birth_year = int(Player.birthdate)
                age = current_year - birth_year
                if age > 30:
                    print(Player.show_fullname, "(", age, "years old )")
                    print("---------------------")



league = League()

league.read_team_info()

league.display_all_teams()

league.display_team_by_code()

league.display_team_by_coach()

league.display_team_by_player()

league.display_players_by_name()

league.display_players_over_30()
