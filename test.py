details_damage_price = {"energy gun": 100}
details_survive_price = {"shield": 50}

users_bot = {}
player_list = []


def player_maker(player_list):
    user_choose = "yes"
    while user_choose == "yes" or user_choose == "y":
        user_input = input("Input a Player name – ")
        if len(user_input) < 3:
            continue
        player_list.append(str.capitalize(user_input))
        user_choose = input("More players – Y/N – ")
    print(f"Players – {str(player_list)[1:-1]}")


def bot_maker(start_sum, player_list):
    for player in player_list:
        wallet = start_sum
        users_bot[player] = {}
        while wallet >= min(details_damage_price.values()):
            string_1 = f"{player}, you have {wallet}coins"
            print(f"{string_1:=^82}")
            string_2 = "You can buy:"
            print(f"{string_2:-^82}")
            print("{detail:^^80}".format(detail="Damage deal details"))
            for gun, price in details_damage_price.items():
                print(f"{gun} – {price}")
            print("{detail:^^80}".format(detail="Survive details"))
            for survive_detail, price in details_survive_price.items():
                print(f"{survive_detail} – {price}")
            user_choose = str.lower(input("Choose the detail – "))
            if user_choose in users_bot[player].keys():
                print("{string:!^80}".format(string="Your bot has this detail"))
                continue
            if user_choose in details_damage_price.keys():
                if wallet < details_damage_price[user_choose]:
                    print("{string:!^80}".format(string="Not enough coins"))
                    continue
                wallet -= details_damage_price[user_choose]
                users_bot[player][user_choose] = details_damage_price[user_choose]
            else:
                if user_choose in details_survive_price.keys():
                    if wallet < details_survive_price[user_choose]:
                        print("{string:!^80}\n".format(string="Not enough coins"))
                        continue
                    wallet -= details_survive_price[user_choose]
                    users_bot[player][user_choose] = details_survive_price[user_choose]
                else:
                    print("\nYour choose is wrong!\n")
                    continue
            print(f"\n\n{player} bot details:{str(users_bot[player].keys())[11:-2]} \n\n")
    for player in player_list:
        print(f"{player} bot details:{str(users_bot[player].keys())[11:-2]}")


player_maker(player_list)
start_sum = int(input("Input start capital – "))
max_start_sum = sum(details_damage_price.values()) + sum(details_survive_price.values())
min_start_sum = min(details_damage_price.values())
if start_sum > max_start_sum:
    start_sum = max_start_sum
if start_sum < min_start_sum:
    start_sum = min_start_sum
bot_maker(start_sum=start_sum, player_list=player_list)
