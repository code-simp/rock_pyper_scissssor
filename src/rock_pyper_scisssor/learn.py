"""
This file has all the logic for learning methods to beat the player
"""


TRAINING_DATA = [
    's',
    's',
    'p',
    'r',
    'p',
    's',
    's',
    'r',
    'r',
    'p',
    's',
    'r',
    's',
    'r',
    's',
]

SAMPLE_DATA = [
    'r',
    's',
    'p',
    'p',
    'p',
    's',
    's',
    'r',
    'r',
    's',
]


from config import get_config

cfg = get_config()


#################################################
#                                               #
# A simple probability based learning algorithm #
#                                               #
#################################################

# This section has a try hard algorithm that learns what the user would choose next
# by allocating weights to each outcome


def try_hard():

    from play import randomize_outcome, user_won

    # weights for Rock -> r, Paper -> p, Scissors -> s
    r, p, s = 100, 100, 100

    weights = {
        "Rock!!": 100,
        "Paper!!": 100,
        "Scissors!!": 100
    }

    weight_reduction = 40
    weight_increase = 30

    computer_win_count = 0
    considered_rounds = 0


    ##############################
    # training section
    ##############################

    def _train_data(user_inp, weights_dict):
        weights_dict[user_inp] -= weight_reduction

        for key in weights_dict.keys():
            if key == user_inp:
                continue
            weights_dict[key] += weight_increase
        
        return weights_dict

    for input_key in TRAINING_DATA:
        
        user_input = cfg.get('KEY_MAP')[input_key]
        weighted_outcomes = []

        # create weighted outcomes
        for key, weight in weights.items():
            weighted_outcomes += [key]*round(weight, 0)

        generated_outcome = randomize_outcome(weighted_outcomes)

        # now we reduce the weights of the the user_input that has just occured
        weights = _train_data(user_input, weights)
    
    ##############################
    # TRY HARD section
    ##############################

    print("\n\n====================================================")
    print("                     GAME START                     ")
    print("====================================================")

    for input_key in SAMPLE_DATA:

        user_input = cfg.get('KEY_MAP')[input_key]
        generated_outcome = randomize_outcome(weighted_outcomes)

        if user_input == generated_outcome:
            continue

        # Finally add the win count if computer wins
        computer_win_count += 1 if not user_won(generated_outcome, user_input) else 0
        considered_rounds += 1

    print("\n\n\nFinal weights -> ", weights)

    print(f"\n\n{computer_win_count} of {considered_rounds} won by computer\n\n")


if __name__ == "__main__":
    try_hard()
