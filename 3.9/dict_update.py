from hints import print_json

i_want_it_that_way = {"You are my fire": "The one desire"}
tell_me_why = {"Believe when I say": "I want it that way"}

i_want_it_that_way.update(tell_me_why)

print_json(i_want_it_that_way)