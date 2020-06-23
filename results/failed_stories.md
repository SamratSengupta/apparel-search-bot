## happy path 1
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_ask_user_type -->


## happy path 2
* greet: hello there!
    - utter_greet
* mood_great: amazing
    - utter_happy   <!-- predicted: utter_ask_user_type -->
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_ask_user_type -->


## sad path 1
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_ask_user_type -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes
    - utter_happy


## sad path 2
* greet: hello
    - utter_greet
* mood_unhappy: not good
    - utter_cheer_up   <!-- predicted: utter_ask_user_type -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really
    - utter_goodbye


## sad path 3
* greet: hi
    - utter_greet
* mood_unhappy: very terrible
    - utter_cheer_up   <!-- predicted: utter_ask_user_type -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no
    - utter_goodbye


## say goodbye
* goodbye: bye-bye!
    - utter_goodbye   <!-- predicted: utter_greet -->


