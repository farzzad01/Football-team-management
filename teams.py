import tkinter as tk
from tkinter import messagebox

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
        

    
class PlayerGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.player = Player()

        self.title("Player Information")
        self.geometry("400x300")

        player_name_label = tk.Label(self, text="Player Name:")
        player_name_label.pack()
        self.player_name_entry = tk.Entry(self)
        self.player_name_entry.pack()

        player_age_label = tk.Label(self, text="Player Age:")
        player_age_label.pack()
        self.player_age_entry = tk.Entry(self)
        self.player_age_entry.pack()

        player_position_label = tk.Label(self, text="Player Position:")
        player_position_label.pack()
        self.player_position_entry = tk.Entry(self)
        self.player_position_entry.pack()

        save_button = tk.Button(self, text="Save", command=self.save_player)
        save_button.pack(pady=10)

        display_button = tk.Button(self, text="Display", command=self.display_player)
        display_button.pack()

    def save_player(self):
        name = self.player_name_entry.get()
        age = int(self.player_age_entry.get())
        position = self.player_position_entry.get()

        self.player.set_name(name)
        self.player.set_age(age)
        self.player.set_position(position)

        self.player_name_entry.delete(0, tk.END)
        self.player_age_entry.delete(0, tk.END)
        self.player_position_entry.delete(0, tk.END)

        print("Player information saved.")

    def display_player(self):
        name = self.player.get_name()
        age = self.player.get_age()
        position = self.player.get_position()

        print("Player Information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Position: {position}")


class Player:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.position = ""

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_position(self, position):
        self.position = position

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_position(self):
        return self.position


if __name__ == "__main__":
    player_app = PlayerGUI()
    player_app.mainloop()




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

class TeamGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Team Information")
        self.geometry("400x400")

        self.team = Team()

        self.create_widgets()

    






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

    

    

league = League()

while True:
    print("========== League Menu ==========")
    print("1. Read team information")
    print("2. Display all teams")
    print("3. Display team by code")
    print("4. Display team by coach")
    print("5. Display team by player")
    print("6. Display players by name")
    print("7. Display players over 30")
    print("8. Display coaches with teams")
    print("9. Player statistics")
    print("10. Player with most goals")
    print("11. Player with most passes")
    print("12. Player with most shots on goal")
    print("13. Team with goalkeeper with most clean sheets")
    print('14. display most violent team')
    print('15. get player nationality')
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        league.read_team_info()
    elif choice == "2":
        league.display_all_teams()
    elif choice == "3":
        league.display_team_by_code()
    elif choice == "4":
        league.display_team_by_coach()
    elif choice == "5":
        league.display_team_by_player()
    elif choice == "6":
        league.display_players_by_name()
    elif choice == "7":
        league.display_players_over_30()
    elif choice == "8":
        league.display_coaches_with_teams()
    elif choice == "9":
        league.display_players_height()
    
    elif choice == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.\n")

