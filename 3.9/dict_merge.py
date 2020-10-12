from hints import print_json

tell_me_why = {"But we are two worlds apart": "Can't reach to your heart"}
aint_nothing_but_a_heartache = {"When you say": "That I want it that way"}

second_verse = tell_me_why | aint_nothing_but_a_heartache

print_json(second_verse)