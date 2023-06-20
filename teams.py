import tkinter as tk

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
        while True:
            try:
                year = int(input("Enter birth year: "))
                if 1970 <= year <= 2010:
                    self.birthdate = year
                    break
                else:
                    print("The birth year should be between 1970 and 2010.")
            except ValueError:
                print("Invalid input. Please enter a valid birth year.")

    def show_fullname(self):
        print("Full name:", self.fname, self.lname)

    def show_idcode(self):
        print("ID code:", self.idcode)

    def show_birthdate(self):
        print("Birthdate:", self.birthdate)

    def show_birthdate(self):
        print("Birthdate:", self.birthdate)


class Coach(Person):
    def __init__(self):
        super().__init__()
        self.card_type = []

    def read_card_and_ranking(self):
        valid_cards = ["A", "B", "C"]
        while True:
            card = input("Enter the coaching card type (A/B/C): ")
            if card.upper() in valid_cards:
                self.card_type = card.upper()
                break
            else:
                print("Invalid coaching card type. Please choose one of the following: A, B, C.")

        self.team_ranking = int(input("Enter the team's ranking: "))

    def show_card_type(self):
        print("Card type:", self.card_type)
    
    def read_coach_info(self):
        self.read_fname()
        self.read_lname()
        self.read_birthdate()
        self.read_idcode()
        self.read_card_and_ranking()
    
    def show_caoch_info(self):
        super().show_fullname()
        super().show_idcode()
        super().show_birthdate()
        print("Card Type: ", self.card_type)
        print("ranking: ", self.team_ranking)



class Player(Person):
    def __init__(self):
        super().__init__()
        self.post = []
        self.goal = []
        self.height = []
        self.weight = []
        self.nationality = []
        self.goal = 0
        self.passes = 0
        self.scored_goal = False
        self.ball_taken = 0
        self.passes_given = 0
        self.clean_sheets = 0
        self.shot = 0
        self.is_foreign = False
        self.has_card = False
        self.num_cards = 0
        self.num_foul = 0
        

    
    def read_post(self):
        valid_modes = ["attack", "midfielder", "defense", "goalkeeper"]
        while True:
            mode = input("Enter player's position (attack/midfielder/defense/goalkeeper): ")
            if mode.lower() in valid_modes:
                self.post = mode.lower()
                break
            else:
                print("Invalid position. Please choose one of the following: attack, midfielder, defense, goalkeeper.")
    

    def read_stats(self):
        if self.post.lower() == "attack":
            self.goal = int(input("Enter the number of goals scored this season: "))
            self.shot = int(input("Enter the number of successful shots this season: "))

        elif self.post.lower() == "midfielder":
            self.passes = int(input("Enter the number of passes made this season: "))
            self.shot = int(input("Enter the number of successful shots this season: "))

            choice = input("Did the player score a goal this season? (y/n): ")
            if choice == 'y':
                self.goal= int(input('how many goals? '))

            choice = input("Did he make a foul on the opponent?? (y/n): ")
            if choice == 'y':
                self.num_foul= int(input('how many fouls? '))

        elif self.post.lower() == "defense":
            self.num_foul = int(input("Enter the number of times the opponent has been fouled "))
            self.ball_taken = int(input("Enter the number of times the ball was taken from opponents: "))
            self.passes_given = int(input("Enter the number of passes given to team mates: "))
            card_option = input("Did the player receive a card this season? (y/n): ")
            if card_option == "y":
                self.has_card = True
                self.num_cards = int(input("Enter the number of cards received: "))

        elif self.post.lower() == "goalkeeper":
            self.clean_sheets = int(input("Enter the number of clean sheets made this season: "))
   
   

    def read_goal(self):
        self.goal = input('enter player goals')
    
    def read_height(self):
        while True:
            try:
                height = int(input("Enter height : "))
                if 160 <= height <= 210:
                    self.height = height
                    break
                else:
                    print("The height should be between 160 and 210.")
            except ValueError:
                print("Invalid input.")

    def read_weight(self):
        while True:
            try:
                weight = int(input("Enter weight : "))
                if 50 <= weight <= 110:
                    self.weight = weight
                    break
                else:
                    print("The weight should be between 50 and 110.")
            except ValueError:
                print("Invalid input.")

    def read_nationality(self):
        self.nationality = input("Enter player's nationality: ")
        foreign_option = input("Is the player a foreign player? (y/n): ")
        if foreign_option.lower() == "y":
            self.is_foreign = True



    def read_palyer_info(self):
        self.read_fname()
        self.read_lname()
        self.read_idcode()
        self.read_birthdate()
        self.read_height()
        self.read_weight()
        self.read_nationality()
        self.read_post()
        self.read_stats()
        
    def show_height(self):
        print(self.height)


    def show_player_info(self):
        super().show_fullname()
        super().show_idcode()
        super().show_birthdate()
        print("post:", self.post)
        print("Height:", self.height)
        print("Weight:", self.weight)
        print("Nationality:", self.nationality)
        if self.post.lower() == "attack":
            print('goal count ', self.goal)
            print('shot count ', self.shot)
        elif self.post.lower() == 'midfielder':
            print('pass count', self.passes)
            print('shot count', self.shot)
            print('goal count' , self.goal)
            print('Foul count' , self.num_foul)
        elif self.post.lower() == 'defense':
            print('ball_taken', self.ball_taken)
            print('passes_given', self.passes_given)
            print('has_card', self.has_card)
            print('num card', self.num_cards)
        elif self.post.lower() == 'goalkeeper':
            print('clean_sheets' , self.clean_sheets)
        
        # elif self == self.team.captain:
        #     print('Captain')
        


class Team:
    MAX_PLAYERS_PER_TEAM = 11

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
        print("Team name: ", self.team_name)

    def show_team_code(self):
        print("Team code: ", self.team_code)

    def read_team_info(self):
        self.read_team_name()
        self.read_team_code()
        print("---------------------------")
        print("Coach Info:")
        self.coach.read_coach_info()
        print("---------------------------")
        num_players = int(input("Enter the number of players in the team: "))
        for i in range(num_players):
            print("Player", i+1, "Info:")
            player = Player()
            player.read_palyer_info()
            self.players.append(player)
            print("---------------------------")

        print("---------------------------")
        print("Choose Captain:")
        self.choose_captain()


    def choose_captain(self):
        if self.players:
            print("Select the captain from the following players:")
            for i, player in enumerate(self.players):
                print(f"{i+1}. {player.fname} {player.lname}")

            choice = int(input("Enter the number of the chosen captain: "))

            if 1 <= choice <= len(self.players):
                captain = self.players[choice - 1]
                print('--------------------------------------')
                print(f"{captain.fname} {captain.lname} is the captain of {self.team_name}.")
                print('--------------------------------------')
                return captain
            else:
                print("Please try again there is no captain.")
        else:
            print("No players in the team. Cannot choose a captain.")

        return None   
        
            # if num_players > 11:
            #     choice = input("Do you want to add a reserve player? (y/n): ")
            #     if choice.lower() == "y":
            #         print("Reserve Player Info:")
            #         reserve_player = Player()
            #         reserve_player.read_player_info()
            #         self.players.append(reserve_player)
            #         print("---------------------------")
            #     else:
            #         break

    def show_team_info(self):
        print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
        self.show_team_name()
        self.show_team_code()
        print("\n---------------------------")
        print("Coach Info:")
        self.coach.show_caoch_info()
        print("\n---------------------------")
        for i, player in enumerate(self.players):
            print("\nPlayer", i+1, "Info:")
            player.show_player_info()
            print("\n---------------------------")




    # def transfer_player(self, player, new_team):
    #     if player in self.players:
    #         if len(new_team.players) < MAX_PLAYERS_PER_TEAM:
    #             self.players.remove(player)
    #             new_team.players.append(player)
    #             player.team = new_team
    #             print(f"Player {player.fname} {player.lname} transferred from {self.team_name} to {new_team.team_name}.")
    #             return True
    #         else:
    #             print(f"The new team {new_team.team_name} has reached the maximum number of players.")
    #     else:
    #         print(f"Player {player.fname} {player.lname} is not in {self.team_name}.")

    #     return False
    

    def player_statistics(self):
        for i, player in enumerate(self.players):
            print("\nPlayer", i+1, "Info:")
            player.show_player_info(self)
            print("\n---------------------------")

    def get_foreign_players_count(self):
            foreign_players_count = 0
            for player in self.players:
                if player.is_foreign:
                    foreign_players_count += 1
            return foreign_players_count


class League:
    def __init__(self):
        self.teams = []
        self.player = Player()

    def read_team_info(self):
        team = Team()
        team.read_team_info()
        self.teams.append(team)

    def display_all_teams(self):
        for team in self.teams:
            team.show_team_info()
    
    def display_coaches_with_teams(self):
        for team in self.teams:
            print(f"Team: {team.team_name}")
            team.coach.show_caoch_info()
            print("---------------------------")

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
                    print(Player.show_fullname(), "(", age, "years old )")
                    print("---------------------")
    
    def display_players_height(self):
        for team in self.teams:
            for player in team.players:
                print(player.show_fullname(), "(", player.height, "CM)")


    def get_team_with_most_foreign_players(self):
        team_with_most_foreign_players = None
        max_foreign_players_count = 0

        for team in self.teams:
            foreign_players_count = team.get_foreign_players_count()

            if foreign_players_count > max_foreign_players_count:
                max_foreign_players_count = foreign_players_count
                team_with_most_foreign_players = team

        return team_with_most_foreign_players

    def get_player_with_most_goals(self):
        player_with_most_goals = None
        max_goals = 0

        for team in self.teams:
            for player in team.players:
                if player.goal > max_goals:
                    max_goals = player.goal
                    player_with_most_goals = player

        return player_with_most_goals
    
    def get_player_with_most_passes(self):
        player_with_most_passes = None
        max_passes = 0

        for team in self.teams:
            for player in team.players:
                if player.passes > max_passes:
                    max_passes = player.passes
                    player_with_most_passes = player

        return player_with_most_passes
    
    def get_player_with_most_shots_on_goal(self):
        player_with_most_shots = None
        max_shots = 0

        for team in self.teams:
            for player in team.players:
                if player.shot > max_shots:
                    max_shots = player.shot
                    player_with_most_shots = player

        return player_with_most_shots
    
    
    def get_goalkeeper_with_most_clean_sheets(self):
            goalkeeper_with_most_clean_sheets = None
            max_clean_sheets = 0

            for team in self.teams:
                for player in team.players:
                    if isinstance(player) and player.clean_sheets > max_clean_sheets:
                        max_clean_sheets = player.clean_sheets
                        goalkeeper_with_most_clean_sheets = player

            return goalkeeper_with_most_clean_sheets

    def get_team_with_most_fouls(self):
            max_fouls = 0
            fouling_team = None

            for team in self.teams:
                total_fouls = 0
                for player in team.players:
                    total_fouls += player.fouls

                if total_fouls > max_fouls:
                    max_fouls = total_fouls
                    fouling_team = team

            return fouling_team

    # def get_players_nationality(self):
    #         nationalities = []
    #         for player in self.players:
    #             nationalities.append(player.nationality)
    #         return nationalities

class TeamInfoGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Team Information")

        self.teams = []
        self.coaches = []
        self.players = []

        self.team_name_label = tk.Label(self.window, text="Team Name:")
        self.team_name_entry = tk.Entry(self.window)
        self.team_code_label = tk.Label(self.window, text="Team Code:")
        self.team_code_entry = tk.Entry(self.window)

        self.coach_name_label = tk.Label(self.window, text="Coach Name:")
        self.coach_name_entry = tk.Entry(self.window)
        self.coach_last_name_label = tk.Label(self.window, text="Coach Last Name:")
        self.coach_last_name_entry = tk.Entry(self.window)
        self.coach_dob_label = tk.Label(self.window, text="Date of Birth:")
        self.coach_dob_entry = tk.Entry(self.window)
        self.coach_id_label = tk.Label(self.window, text="ID Code:")
        self.coach_id_entry = tk.Entry(self.window)
        self.coach_card_label = tk.Label(self.window, text="Card Type:")
        self.coach_card_entry = tk.Entry(self.window)
        self.coach_rank_label = tk.Label(self.window, text="Team Rank:")
        self.coach_rank_entry = tk.Entry(self.window)

        self.player_name_label = tk.Label(self.window, text="Player Name:")
        self.player_name_entry = tk.Entry(self.window)
        self.player_last_name_label = tk.Label(self.window, text="Player Last Name:")
        self.player_last_name_entry = tk.Entry(self.window)
        self.player_dob_label = tk.Label(self.window, text="Date of Birth:")
        self.player_dob_entry = tk.Entry(self.window)
        self.player_id_label = tk.Label(self.window, text="ID Code:")
        self.player_id_entry = tk.Entry(self.window)
        self.player_position_label = tk.Label(self.window, text="Player Position:")
        self.player_position_entry = tk.Entry(self.window)

        self.get_team_info_button = tk.Button(self.window, text="Get Team Info", command=self.show_team_info)
        self.get_coach_info_button = tk.Button(self.window, text="Get Coach Info", command=self.show_coach_info)
        self.get_player_info_button = tk.Button(self.window, text="Get Player Info", command=self.show_player_info)

        self.info_label = tk.Label(self.window, text="")



        self.team_name_label.grid(row=0, column=0, sticky=tk.E)
        self.team_name_entry.grid(row=0, column=1)
        self.team_code_label.grid(row=1, column=0, sticky=tk.E)
        self.team_code_entry.grid(row=1, column=1)

        self.coach_name_label.grid(row=0, column=2, sticky=tk.E)
        self.coach_name_entry.grid(row=0, column=3)
        self.coach_last_name_label.grid(row=1, column=2, sticky=tk.E)
        self.coach_last_name_entry.grid(row=1, column=3)
        self.coach_dob_label.grid(row=2, column=2, sticky=tk.E)
        self.coach_dob_entry.grid(row=2, column=3)
        self.coach_id_label.grid(row=3, column=2, sticky=tk.E)
        self.coach_id_entry.grid(row=3, column=3)
        self.coach_card_label.grid(row=4, column=2, sticky=tk.E)
        self.coach_card_entry.grid(row=4, column=3)
        self.coach_rank_label.grid(row=5, column=2, sticky=tk.E)
        self.coach_rank_entry.grid(row=5, column=3)

        self.player_name_label.grid(row=0, column=4, sticky=tk.E)
        self.player_name_entry.grid(row=0, column=5)
        self.player_last_name_label.grid(row=1, column=4, sticky=tk.E)
        self.player_last_name_entry.grid(row=1, column=5)
        self.player_dob_label.grid(row=2, column=4, sticky=tk.E)
        self.player_dob_entry.grid(row=2, column=5)
        self.player_id_label.grid(row=3, column=4, sticky=tk.E)
        self.player_id_entry.grid(row=3, column=5)
        self.player_position_label.grid(row=4, column=4, sticky=tk.E)
        self.player_position_entry.grid(row=4, column=5)

        self.get_team_info_button.grid(row=6, column=0, columnspan=2)
        self.get_coach_info_button.grid(row=6, column=2, columnspan=2)
        self.get_player_info_button.grid(row=6, column=4, columnspan=2)

        self.info_label.grid(row=7, column=0, columnspan=6)

        self.display_all_teams_button = tk.Button(self.window, text="Display All Teams", command=self.display_all_teams)
        self.display_team_by_code_button = tk.Button(self.window, text="Display Team by Code", command=self.display_team_by_code)
        self.display_team_by_coach_button = tk.Button(self.window, text="Display Team by Coach", command=self.display_team_by_coach)
        self.display_team_by_player_button = tk.Button(self.window, text="Display Team by Player", command=self.display_team_by_player)
        self.display_players_by_name_button = tk.Button(self.window, text="Display Players by Name", command=self.display_players_by_name)
        self.display_players_over_30_button = tk.Button(self.window, text="Display Players Over 30", command=self.display_players_over_30)
        self.display_coaches_with_teams_button = tk.Button(self.window, text="Display Coaches with Teams", command=self.display_coaches_with_teams)
        self.display_players_height_button = tk.Button(self.window, text="Display Players Height", command=self.display_players_height)

        self.display_all_teams_button.grid(row=8, column=0, columnspan=2)
        self.display_team_by_code_button.grid(row=8, column=2, columnspan=2)
        self.display_team_by_coach_button.grid(row=8, column=4, columnspan=2)
        self.display_team_by_player_button.grid(row=9, column=0, columnspan=2)
        self.display_players_by_name_button.grid(row=9, column=2, columnspan=2)
        self.display_players_over_30_button.grid(row=9, column=4, columnspan=2)
        self.display_coaches_with_teams_button.grid(row=10, column=0, columnspan=2)
        self.display_players_height_button.grid(row=10, column=2, columnspan=2)

    def show_team_info(self):
        team_name = self.team_name_entry.get()
        team_code = self.team_code_entry.get()

        team_info = f"Team Name: {team_name}\nTeam Code: {team_code}"
        self.teams.append(team_info)

        self.team_name_entry.delete(0, tk.END)
        self.team_code_entry.delete(0, tk.END)

        self.info_label.config(text="Team information saved.")

    def show_coach_info(self):
        coach_name = self.coach_name_entry.get()
        coach_last_name = self.coach_last_name_entry.get()
        coach_dob = self.coach_dob_entry.get()
        coach_id = self.coach_id_entry.get()
        coach_card = self.coach_card_entry.get()
        coach_rank = self.coach_rank_entry.get()

        coach_info = f"Name: {coach_name}\nLast Name: {coach_last_name}\nDOB: {coach_dob}\nID: {coach_id}\nCard: {coach_card}\nRank: {coach_rank}"
        self.coaches.append(coach_info)

        self.coach_name_entry.delete(0, tk.END)
        self.coach_last_name_entry.delete(0, tk.END)
        self.coach_dob_entry.delete(0, tk.END)
        self.coach_id_entry.delete(0, tk.END)
        self.coach_card_entry.delete(0, tk.END)
        self.coach_rank_entry.delete(0, tk.END)

        self.info_label.config(text="Coach information saved.")

    def show_player_info(self):
        player_name = self.player_name_entry.get()
        player_last_name = self.player_last_name_entry.get()
        player_dob = self.player_dob_entry.get()
        player_id = self.player_id_entry.get()
        player_position = self.player_position_entry.get()
        info = f"Player Name: {player_name}\nLast Name: {player_last_name}\nDate of Birth: {player_dob}\nID Code: {player_id}\nPosition: {player_position}"
        self.info_label.config(text=info)

    def save_player_info(self):
        player_name = self.player_name_entry.get()
        player_last_name = self.player_last_name_entry.get()
        player_dob = self.player_dob_entry.get()
        player_id = self.player_id_entry.get()
        player_position = self.player_position_entry.get()

        player_info = f"Name: {player_name}\nLast Name: {player_last_name}\nDOB: {player_dob}\nID: {player_id}\nPosition: {player_position}"
        self.players.append(player_info)

        self.player_name_entry.delete(0, tk.END)
        self.player_last_name_entry.delete(0, tk.END)
        self.player_dob_entry.delete(0, tk.END)
        self.player_id_entry.delete(0, tk.END)
        self.player_position_entry.delete(0, tk.END)

        self.info_label.config(text="Player information saved.")

    def display_all_teams(self):
        if self.teams:
            team_info = "\n".join(self.teams)
            self.info_label.config(text=team_info)
        else:
            self.info_label.config(text="No team information available.")
        self.info_label.config(text=team_info)
        

    def display_team_by_code(self):
        team_code = self.team_code_entry.get()
        team_info = [team for team in self.teams if team_code in team]
        if team_info:
            team_info_str = "\n".join(team_info)
            self.info_label.config(text=team_info_str)
        else:
            self.info_label.config(text="No team found with the provided code.")

    def display_team_by_coach(self):
        coach_name = self.coach_name_entry.get()
        coach_info = [coach for coach in self.coaches if coach_name in coach]
        if coach_info:
            coach_info_str = "\n".join(coach_info)
            self.info_label.config(text=coach_info_str)
        else:
            self.info_label.config(text="No coach found with the provided name.")

    def display_team_by_player(self):
        player_name = self.player_name_entry.get()
        player_info = [player for player in self.players if player_name in player]
        if player_info:
            player_info_str = "\n".join(player_info)
            self.info_label.config(text=player_info_str)
        else:
            self.info_label.config(text="No player found with the provided name.")

    def display_players_by_name(self):
        if self.players:
            sorted_players = sorted(self.players)
            player_info = "\n".join(sorted_players)
            self.info_label.config(text=player_info)
        else:
            self.info_label.config(text="No player information available.")

    def display_players_over_30(self):
        player_info = [player for player in self.players if "DOB: " in player and int(player.split("DOB: ")[-1]) > 30]
        if player_info:
            player_info_str = "\n".join(player_info)
            self.info_label.config(text=player_info_str)
        else:
            self.info_label.config(text="No players over 30 found.")

    def display_coaches_with_teams(self):
        if self.coaches:
            coach_info = "\n".join(self.coaches)
            self.info_label.config(text=coach_info)
        else:
            self.info_label.config(text="No coach information available.")

    def display_players_height(self):
        player_info = [player for player in self.players if "Height: " in player]
        if player_info:
            player_info_str = "\n".join(player_info)
            self.info_label.config(text=player_info_str)
        else:
            self.info_label.config(text="No player height information available.")



    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = TeamInfoGUI()
    app.run()


