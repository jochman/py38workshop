from hints import backstreet_singer

tell_me_why = "Tell me why"
tell_me_why1 = {"Ain't nothin' but a heartache": tell_me_why}
tell_me_why2 = {"Ain't nothin' but a mistake": tell_me_why}
tell_me_why3 = {"I never wanna hear you say": tell_me_why}
i_want_it_that_way = "I want it that way"

backstreet_singer(tell_me_why1 | tell_me_why2 | tell_me_why3)  # TODO: sing the chorus