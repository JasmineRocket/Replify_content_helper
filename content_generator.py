import random
theme = ["betrayal", "apology", "trust issues", "regret", "open-ended",
         "rumors", "tension", "guilt", "Love triangle", "escape", "revenge",
         "toxic friendship", "emotional manipulation", "secrets from the past",
         "forgiveness", "rivalry", "jealousy", "second chances",  ]
key_word = ["Miscommunication","secrets", "Late-night texts", "movie", 
                "cheating", "promises", "overthinking", "deleting", "sex",
                "flirting","gay","lesbian", "awkward pauses", "red flags", 
                "love letters", "unplanned pregnancy", "blind date", 
                "suspicious behavior", "texting the wrong person", "overnight",
                "jealous best friend", "temporary break-up", "unplanned meetup",
                "revenge dating", "unforgivable lie"]
characters = ["stepsister","bestie", "mother-in-law", "bro", "gf","bf",
              "teammate", "roommate", "neighbor", "delivery driver", "ex-wife",
              "gym buddy", "babysitter", "uncle"]

print("theme: " + theme[random.randint(0,len(theme)-1)])
print("key word: " + key_word[random.randint(0,len(key_word)-1)])
print("characters: " + characters[random.randint(0,len(characters)-1)])