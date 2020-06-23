<!-- ## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye -->

## bot challenge
* bot_challenge
  - utter_iamabot

## product search happy path + product_type + user_type
* greet
  - utter_greet
* product_search{"product_type":"shirt", "user_type":"men"}
  - action_product_search
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_thank

## product search happy path + user_type
* greet
  - utter_greet
* product_search{"product_type":"shirt"}
  - utter_ask_user_type
* inform_user_type{"user_type":"men"}
  - action_product_search
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_thank

## product search happy path
* greet
  - utter_greet
* product_search
  - utter_ask_product_type
* inform_product_type{"product_type":"shirt"}
  - utter_ask_user_type
* inform_user_type{"user_type":"men"}
  - action_product_search
  - utter_did_that_help
* affirm
  - utter_happy
* thank
  - utter_thank

## product search sad path
* greet
  - utter_greet
* product_search{"product_type":"shirt", "user_type":"men"}
  - action_product_search
  - utter_did_that_help
* deny
  - utter_goodbye

## product search sad path + user_type
* greet
  - utter_greet
* product_search{"product_type":"shirt"}
  - utter_ask_user_type
* inform_user_type{"user_type":"men"}
  - action_product_search
  - utter_did_that_help
* deny
  - utter_goodbye

## product search sad path
* greet
  - utter_greet
* product_search
  - utter_ask_product_type
* inform_product_type{"product_type":"shirt"}
  - utter_ask_user_type
* inform_user_type{"user_type":"men"}
  - action_product_search
  - utter_did_that_help
* deny
  - utter_goodbye