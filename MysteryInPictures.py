# Mystery in Pictures - Part 1

# Intro story
print("When the calendar showed 2025 October 15th, Clara and her friends were chatting in class, as usual. " \
"Just then, Clara's eye caught the top of the locker. She noticed a rope hanging from it and went over to it. " \
"It was a camera! She didn't know whose it was, but she wanted to take a picture anyway. " \
"She secretly took Jessica's picture, but when she looked at it, she saw she wasn't there. " \
"How could this be? She tried again and again, and the result was always the same." \
"Should she show it to her friends? Should she take it home and examine it herself? Or should she put the camera back in its place?")
# First choice: 1-Show friends, 2-Investigate alone, 3-Put it back
choice1 = int(input("1-Show it to your friends \n2-Examine it yourself \n3-Put it back \nWhat is your choice?(1,2,3): "))
if choice1 == 1:
    # Scenario: Show friends
    print("Clara decided to show the camera to her friends. " \
    "None of them believed it when she told them the story, but when they tried it, they too saw that it was true. " \
    "They wanted to understand the camera's mystery, but they had no idea how. " \
    "Should they consult their photography teacher, Julian Hawke, or should they continue taking photos themselves?")
    # Second choice: 1-Consult Julian Hawke, 2-Continue taking photos
    choice2 = int(input("1-Consult Julian Hawke \n2-Continue taking photos \nWhat is your choice?(1,2): "))
    if choice2 == 1:
        # Scenario: Consult teacher
        print("Clara and her friends decided to consult their teacher, Julian Hawke, and headed to his office. " \
              "Julian Hawke had come to the university last year and was a very kind and friendly person, well-liked by everyone. " \
              "When Clara and her friends arrived, he welcomed them in. Clara explained everything to him. " \
              "Julian asked for the camera, and he took a few photos. The results were the same as always. " \
              "He told the children that he could take the camera and examine it himself, but not to worry. " \
              "Should Clara give the camera to the teacher or take it back?")
        # Third choice: 1-Give camera to teacher, 2-Take it back
        choice3 = int(input("1-Give the camera to the teacher \n2-Take it back \nWhat is your choice?(1,2): "))
        if choice3 == 1:
            # Scenario: Give the camera to teacher
            print("Clara and her friends decided to give the camera to their teacher, Julian. Days and weeks passed. " \
            "Clara and her friends hadn't heard from their teacher. When they went back to his office, they found he wasn't there. " \
            "They checked with the receptionist and learned that Julian Hawke had left the school a few days ago. They were all shocked and angry. " \
            "How could he have taken the camera without telling them? What was behind it? They all wanted to know.")
        elif choice3 == 2:
            # Scenario: Refuse to give the camera
            print("Clara hesitated for a moment, then decided not to give the camera to Julian. "
            "She politely told him that she would keep it for herself. "
            "Julian’s kind smile faded for a second, but he quickly covered it up. "
            "'As you wish,' he said, but his eyes followed the camera as Clara put it back in her bag. "
            "On the way out, Robin whispered to Clara: 'Did you see that? He really wanted the camera… almost too much.' "
            "Clara now wondered: Should she trust her teacher at all, or was Julian hiding something?")
    elif choice2 == 2:
        # Scenario: Friends continue investigating on their own
        print("Clara and her friends decide to go it alone, without consulting their teacher. " \
             "What should they photograph next? The view out the school window, the whole classroom, or just a selfie?")
        choice4 = 0
        # Loop until classroom is chosen
        while choice4 != 2:
            choice4 = int(input("1-School window \n2-Whole classroom \n3-Selfie \nWhat is your choice?(1,2,3): "))
            if choice4 == 1:
                print("They took photos from the school window. The photo was almost identical to the original, but some of the trees and cars were incorrectly placed. " \
                "Clara and her friends couldn't understand anything about it.")
            elif choice4 == 2:
                print("They took a photo of the whole class. Something was different. " \
                    "The board was different, the desks had been replaced, and the cabinets were in a different location. " \
                    "What was that? The calendar hanging on the wall read October 15, 2035. That was exactly 10 years from now. " \
                    "Clara and her friends were very surprised. Could the camera really be showing 10 years into the future?")
            elif choice4 == 3:
                print("Clara and her friends took a selfie together, but again, none of them were in the photo. They couldn't understand anything about this situation.")
            else:
                print("This was a wrong choise. Try again.")
# Scenario: Clara investigates alone at home
elif choice1 == 2:
    print("Clara decided to investigate the camera herself and put it in her bag. " \
    "The first thing she did when she got home was go up to her room and continue examining the camera. " \
    "As she examined the camera, a date written in small numbers caught her eye: October 15, 2035. " \
    "Exactly 10 years from now. Why such a date? Clara was very confused. What should Clara do? " \
    "Should she tell her best friend Robin or should she search the Internet for this camera?")
    choice5 = 0
    # Loop until Internet research is chosen
    while choice5 != 2:
        choice5 = int(input("1-Tell Robin \n2-Research on Internet \nWhat is your choice?(1,2): "))
        if choice5 == 1:
            print("Clara told her friend Robin about the situation and invited her over. Robin was shocked to hear the news. " \
            "The two of them began investigating together. They meticulously examined every inch of the camera but found nothing new.")
        elif choice5 == 2:
            print("Clara decided to research the camera online. She found a user sharing a camera very similar to one she'd found on an old forum. " \
            "That user also explained that the photos had nothing to do with the environment they were shooting in, and that she didn't understand why at first. " \
            "But then Clara saw that the camera had written about capturing moments 10 years later. How could that be possible?")
        else:
            print("This was a wrong choise. Try again.")
# Scenario: Put the camera back
elif choice1 == 3:
    print("Clara chose to put the camera back in its place. "
      "This was a true act of honesty, but Clara could not solve the mystery of the camera in this way. "
      "For days, she kept thinking about it. Who did the camera really belong to? "
      "And had she just lost her only chance to uncover its secrets?")