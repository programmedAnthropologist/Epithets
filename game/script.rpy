
define fuy = Character("Fuyuhiko", color="#8ceffa")
define har = Character("Haruki", color="#fa8c8c")
define rei = Character("Rei", color="#93fa8c")
define him = Character("Hime", color="#faf48c")
define yoi = Character("Yoikishi", color="#8c95fa")
define tfuy = Character("Fuyuhiko", color="#1d8f5f")
define thar = Character("Haruki", color="#1d8f5f")
define trei = Character("Rei", color="#1d8f5f")
define thim = Character("Hime", color="#1d8f5f")
define tyoi = Character("Yoikishi", color="#1d8f5f")
define nar = Character("")
transform left:
    xalign 0.25
    yalign 1.0
transform right:
    xalign 0.75
    yalign 1.0
transform farleft:
    xalign 0.05
    yalign 1.0
transform farright:
    xalign 0.95
    yalign 1.0
transform center:
    xalign 0.5
    yalign 1.0
transform truecenter:
    xalign 0.5
    yalign 0.5
#Spacer

#Basic introduction into the gist of the story
label start:
    #Flag Defines
    $ HarukiChat = False
    $ YoikishiChat = False
    $ HimeChat = False
    $ ReiChat = False
    $ WorkChat = False
    #Spacer
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "Ah, San Francisco, the salty air of the sea mixed with the salty attitudes of young adults experiencing true independence for the first time in their lives."
    nar "Five of these young adults attend the local university, hailing from across the sea, here to expand their minds and hearts."
    nar "Ah, here comes one now. Arriving home after a long day of less than enjoyable work. perhaps the saltiest of them all, Fuyuhiko Shiro."
    scene apartment night
    show fuyu really
    with Dissolve(0.5)
    fuy "I can't believe that woman!"
    fuy "She always thinks she knows what's best for me. She's not my fucking mom!"
    nar "He stomps across his small apartment and flips open a laptop, furiously scrolling through social media."
    nar "perhaps we should have him recall a few of his companions to take his mind off of things."
    nar "Noncanonically, of course."
    jump recallMenu
#Spacer

#Recall menu, featuring the descriptions of the other Epithets
label recallMenu:
    menu:
        "Haruki Supai":
            show fuyu what
            with Dissolve(0.5)
            fuy "Haruki? He's a Computer Science Major. I've known him for the longest. He's been a chaotic bastard since the day we met."
            show fuyu really
            with Dissolve(0.5)
            fuy "He's arrogant, somewhat violent, and worse of all, flirty. Guy's gay and he owns it, maybe a bit too much."
            fuy "Sometimes it feels like everything he says is specifically meant to make me uncomfortable, or annoyed."
            jump recallMenu
        "Yoikishi Konpeki":
            show fuyu neut
            with Dissolve(0.5)
            fuy "A History Major. He's obsessed with both the Code of Chivalry and the Bushido Code, especially famous upholders of each."
            fuy "Not to mention he's super immature. Lately, he's taken to naming us after seasons."
            fuy "He's also very protective of his sister, Hime. It's hard to imagine him without her, and it's clear he has a great love for her."
            jump recallMenu
        "Himiko Konpeki":
            show fuyu neut
            with Dissolve(0.5)
            fuy "Right, Himiko. She goes by Hime, and she's the only one of us that doesn't attend college."
            fuy "She works as a Graffiti Artist and Cashier and hates that part-time job as much as I."
            show fuyu smile
            with Dissolve(0.5)
            fuy "She's even told me that she started tagging the area around her workplace."
            show fuyu neut
            with Dissolve(0.5)
            fuy "Her nickname comes from a childhood love of princesses, and it stuck. Thanks to her brother, that is."
            jump recallMenu
        "Rei Amanshi":
            show fuyu neut
            with Dissolve(0.5)
            fuy "A Theology Major. He practices some weird niche religon, one that his family holds a lot of power in."
            show fuyu down
            with Dissolve(0.5)
            fuy "Sometimes, I pity him in a weird way. We were both put in such a bad situation by our parents."
            fuy "But Rei doesn't seem to notice that the pressure on him is unhealthy and barely listens to me when I talk to him about it."
            fuy "Worse yet, he was one of the people to see me at my worst earlier today."
            jump recallMenu
        "Move Foward":
            jump textMessage
#Spacer

#Text Message time
label textMessage:
    show fuyu neut
    with Dissolve(0.5)
    nar "As the boy finishes his recollection, his phone begins to buzz. When he picks it up, a message from someone appears on the screen."
    nar "A message from..."
    menu:
        "Haruki":
            jump HarukiMessage
        "Yoikishi":
            jump YoikishiMessage
        "Hime":
            jump HimeMessage
        "Rei":
            jump ReiMessage
        "Work":
            jump WorkMessage
    return
#Spacer

label HarukiMessage:
    nar "...Haruki."
    $ HarukiChat = True
    show fuyu really at farleft
    with moveinright
    show haruki smug at farright
    with Dissolve(0.5)
    thar "Heya there, Fuyu. Are you up to anything? I'd love to swing by and snatch you up~."
    tfuy "Not now Haruki, gods, especially not right now."
    show haruki frown
    with Dissolve(0.5)
    thar "What do you mean?"
    thar "Are you alright, Fuyu?"
    $ renpy.pause(2.5)
    thar "Fuyu?"
    tfuy "Stop calling me that."
    thar "What?"
    stop music fadeout 1.0
    $ renpy.pause(2.0)
    thar "What do you mean, Fuyu?"
    show fuyu snap
    tfuy "MY NAME IS FUYUHIKO."
    show fuyu really
    with Dissolve(0.5)
    tfuy "It's not \"Fuyu\"."
    tfuy "It's not \"sweetheart\" or \"doll\"."
    tfuy "It's Fuyuhiko."
    $ renpy.pause(2.0)
    thar "Fuyu..."
    tfuy "I'm done talking with you."
    play music "audio/Urban-Flight.mp3" fadeout 1.0 fadein 1.0
    nar "The boy powers off his phone. If Haruki continued messaging him, he wouldn't recieve it."
    show fuyu down at center
    with moveinleft
    hide haruki frown
    with Dissolve(0.5)
    nar "Exhausted, the boy crawls into bed, and begins to fall into unconsciousness. The events of the day racing through his head and dreams."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label YoikishiMessage:
    nar "...Yoikishi."
    $ YoikishiChat = True
    show fuyu neut at farleft
    with moveinright
    show yoikishi excited at farright
    with Dissolve(0.5)
    tyoi "winter! you HAVE to see this!"
    show yoikishi err
    with Dissolve(0.5)
    tyoi "oh right"
    tfuy "It's fine, Yoikishi."
    tyoi "if its fine then why are you calling me that! >:("
    tfuy "Okay then,"
    show fuyu smile
    with Dissolve(0.5)
    tfuy "Fall."
    show fuyu neut
    show yoikishi hap
    with Dissolve(0.5)
    tyoi "there you go!"
    show yoikishi excited
    with Dissolve(0.5)
    tyoi "oh right! i had a video to show you, you'll love it!"
    scene black
    with Dissolve(0.5)
    nar "The boys continued chatting about nothing of importance. It was a nice distraction for Fuyuhiko, one he really needed."
    jump Day2
#Spacer

label HimeMessage:
    nar "...Hime."
    $ HimeChat = True
    show fuyu neut at farleft
    with moveinright
    show hime yo at farright
    with Dissolve(0.5)
    thim "You are going to love what I just did."
    nar "Hime sends a image of her tagging her store along with a transcription."
    show fuyu smile
    with Dissolve(0.5)
    tfuy "Amazing."
    thim "I know right!?"
    show hime cool
    with Dissolve(0.5)
    thim "I've been waiting to do this for so long."
    tfuy "What broke the camel's back?"
    $ renpy.pause(2.0)
    show hime uncomfy
    with Dissolve(0.5)
    thim "My asshat of a manager threatened my job because I refused to go out with him."
    show fuyu down
    with Dissolve(0.5)
    tfuy "Oh."
    thim "Yeah."
    $ renpy.pause(3.0)
    show fuyu neut
    with Dissolve(0.5)
    tfuy "I tried to get out of my \"Accessibility Benefits\" again today."
    show hime cool
    with Dissolve(0.5)
    thim "And how'd that go?"
    tfuy "Not great."
    thim "Our bosses suck, huh?"
    show fuyu neut
    with Dissolve(0.5)
    tfuy "Yup"
    thim "I'll see you tomorrow, Fuyuhiko."
    hide hime cool
    with Dissolve(0.5)
    tfuy "You too, Hime."
    show fuyu down at center
    with moveinleft
    fuy "I really need to work on my people skills."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label ReiMessage:
    nar "...Rei."
    $ ReiChat = True
    show fuyu down at farleft
    with moveinright
    show rei cautious at farright
    with Dissolve(0.5)
    trei "Shiro, are you there?"
    $ renpy.pause(3.0)
    trei "Shiro, please."
    $ renpy.pause(1.0)
    trei "Shiro."
    tfuy "What do you want, Rei?"
    trei "I just wanted to make sure you were okay."
    tfuy "I'm fine. Leave me alone."
    trei "Are you sure, Shiro?"
    tfuy "Don't make me block you, Rei."
    $ renpy.pause(1.0)
    nar "Fuyu sits for a few moments, waiting for a text that will never come."
    scene black
    with Dissolve(0.5)
    nar "Instead, he simply powers off his phone and heads to bed, trying to forget the events of the day."
    jump Day2
#Spacer

label WorkMessage:
    nar "...Her."
    $ WorkChat = True
    hide fuyu neut
    show the email at truecenter
    with Dissolve(0.5)
    nar "It was her."
    show fuyu snap
    hide the email
    fuy "That fucking bitch."
    fuy "She just aired our private conversation to the whole cafe!"
    fuy "It's bad enough putting up with her shit when it was just us."
    fuy "I bet she thinks she's doing what's best for me."
    fuy "I'M NOT A FUCKING KID ANYMORE DAD!"
    $ renpy.pause(2.0)
    show fuyu what
    with Dissolve(0.5)
    fuy "I-"
    $ renpy.pause(2.0)
    show fuyu down
    with Dissolve(0.5)
    fuy "I need some sleep."
    scene black
    with Dissolve(0.5)
    jump Day2
#Spacer

label Day2:
    nar "End of Day 1."
    nar "Start of Day 2."
    scene apartment day
    with Dissolve(0.5)
    nar "The next day passed mostly uneventfully"
    scene hallway day
    with Dissolve(0.5)
    nar "The same classes in the same order and the same motions."
    scene classroom evening
    with Dissolve(0.5)
    nar "That was until after school."
    show yoikishi hap at left
    show hime cool at farleft
    show rei distracted at right
    show haruki smug at farright
    with Dissolve(0.5)
    #checks if Haruki was texted last night
    if HarukiChat:
        show haruki frown at farright
        with Dissolve(0.5)
    nar "Club time, that is."
    show fuyu neut at center
    with Dissolve(0.5)
    fuy "Really, our club was just an excuse to use this classroom after school hours, we never really did anything with it."
    fuy "But club  time does bring up the question of who to spend it with."
    menu:
        "Yoikishi and Hime":
            hide haruki
            hide rei
            with Dissolve(0.5)
            show yoikishi at farright
            with moveinleft
            show hime at farleft
            with moveinleft
            jump YoikishiandHime
        "Haruki and Rei":
            hide yoikishi
            hide hime
            with Dissolve(0.5)
            show haruki at farright
            with moveinright
            show rei at farleft
            with moveinright
            jump HarukiandRei
        "Nobody":
            hide yoikishi
            hide hime
            hide rei
            hide haruki
            with Dissolve(0.5)
            jump Nobody
#Spacer

#Yoikishi/Hime's Club time conversation
label YoikishiandHime:
    if HimeChat:
        yoi "Hey Winter!"
        him "Nice to see you, Fuyuhiko."
        show fuyu smile
        with Dissolve(0.5)
        fuy "You too, Hime"
        show yoikishi excited
        with Dissolve(0.5)
        yoi "Hey! Can you help us resolve something?"
        yoi "Which is stronger, the pen or the sword?"
        show fuyu waht
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but Yoikishi, did you just ask the blind kid about art vs fighting?"
        show yoikishi err
        with Dissolve(0.5)
        yoi "Just because he's going to pick the much cooler swords doen't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, strength is such an arbitary thing, and I. Can't. See. Shit."
        fuy "But, for the sake of agruement, Hime wins."
        show yoikshi huh
        with None
        show hime yo
        with Dissolve(0.5)
        yoi "what"
        show yoikishi err
        with Dissolve(0.5)
        yoi "But whyyyyy."
        him "Just face the fact that I'm better, bro."
        yoi "No fair!"
        show fuyu smile
        with Dissolve(0.5)
        fuy "That's just the way the sword crumbles."
        him "Oh, Fuyuhiko, do you wanna ahng out at ours after club?"
        show hime cool
        show yoikishi so
        with Dissolve(0.5)
        nar "Yoikishi grumbles incoherantly, which Hime assures Fuyuhiko is a yes."
        fuy "Sure, as long as he doesn't try to kill me."
        show yoikishi murder
        with Dissolve(0.5)
        yoi "..."
        him "He won't."
        show hime ugh
        with Dissolve(0.5)
        him "Probably."
        jump KonpekiHouse
    if YoikishiChat:
        yoi "Winter, Hey!!!"
        him "Hanging out with the cool kids huh, Fuyuhiko."
        show fuyu smile
        with Dissolve(0.5)
        fuy "You know it."
        show yoikishi excited
        with Dissolve(0.5)
        yoi "Hey! Can you help us resolve something?"
        yoi "Which is stronger, the pen or the sword?"
        show fuyu waht
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but Yoikishi, did you just ask the blind kid about art vs fighting?"
        show yoikishi err
        with Dissolve(0.5)
        yoi "Just because he's going to pick the much cooler swords doen't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, strength is such an arbitary thing, and I. Can't. See. Shit."
        show fuyu smile
        with Dissolve(0.5)
        fuy "But, for the sake of arguement, Yoikishi wins."
        show yoikishi excited
        show hime ugh
        with Dissolve(0.5)
        yoi "Yes!"
        yoi "Beat that Hime!"
        show hime cool
        with Dissolve(0.5)
        him "I want a recounting of the votes. This is election fraud."
        fuy "Too bad, your bother is just a master of gerrymandering."
        show yoikishi hap
        with Dissolve(0.5)
        yoi "Hey! Speaking of gerrymandering, do you wanna come over tonight Winter!?"
        show hime ugh
        him "Wha-"
        fuy "Sure."
        him "Hey!"
        show fuyu neut
        with Dissolve(0.5)
        him "He's not the only one who lives in that house."
        yoi "Someone's a sore loooserrr."
        him "Only 'cause you're a sore winner."
        fuy "So, are you okay with me coming over Hime?"
        him "Well, since you asked so nicely..."
        show hime cool
        with Dissolve(0.5)
        him "Sure."
        yoi "So it's settled then!"
        jump KonpekiHouse
    else:
        yoi "Hey Winter!"
        him "Hanging out with the cool kids huh, Fuyuhiko."
        show fuyu smile
        with Dissolve(0.5)
        fuy "You know it."
        show yoikishi excited
        with Dissolve(0.5)
        yoi "Hey! Can you help us resolve something?"
        yoi "Which is stronger, the pen or the sword?"
        show fuyu what
        with Dissolve(0.5)
        him "No offense Fuyuhiko, but Yoikishi, did you just ask the blind kid about art vs fighting?"
        show yoikishi err
        with Dissolve(0.5)
        yoi "Just because he's going to pick the much cooler swords doen't mean he's biased."
        nar "Normally this would be the point in the the story where a couple text boxes show up for who Fuyuhiko should agree with."
        nar "Unfortunately..."
        show fuyu neut
        with Dissolve(0.5)
        fuy "Yeah that is pretty stupid."
        fuy "I mean, strength is such an arbitary thing, and I. Can't. See. Shit."
        fuy "So, you both lose."
        show yoikishi huh
        show hime ugh
        with None
        yoi "what"
        show yoikishi err
        show hime cool
        with Dissolve(0.5)
        yoi "You can't do that!"
        fuy "That's just what happens when you give one person all the power."
        him "Going full robber baron huh, Fuyuhiko."
        fuy "I'm just teaching someone a very important lesson about captalism."
        show yoikishi so
        with Dissolve(0.5)
        yoi "If you're so smart..."
        show yoikishi excited
        with Dissolve(0.5)
        yoi "Then beat me at Zenshin Tactics!"
        him "Alternatively..."
        show hime yo
        with Dissolve(0.5)
        him "Hang out with someone who doesn't constantly suggest activites you can't do."
        show yoikishi err
        with Dissolve(0.5)
        yoi "Oh."
        him "Waddya say?"
        fuy "Sure. Once club is over."
        him "Great."
        jump KonpekiHouse
#Spacer

#Haruki/Rei's Club time conversation
label HarukiandRei:
    if HarukiChat:
        har "Oh. Hi... Fuyuhiko."
        rei "Hello, Shiro."
        har "I was... Just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        show rei cautious
        with Dissolve(0.5)
        rei "No!"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        show haruki smug
        with Dissolve(0.5)
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's almost pitiful."
        show rei shatter
        with Dissolve(0.5)
        rei "They didn't force me into anything, HARUKI!"
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(2.0)
        har "Rei..."
        show fuyu really
        with Dissolve(0.5)
        fuy "Shut up, Haruki."
        show rei cautious
        with Dissolve(0.5)
        rei "Look. If you want to see that they didn't force me into following Lantern. Come to my house tonight Haruki."
        fuy "I don't think that's a good idea."
        nar "Haruki grumbled, he had something we wanted to say but he held himself back."
        rei "Well, how about you come over, Shiro?"
        show haruki whatever
        with Dissolve(0.5)
        har "Really? So you're just gonna invite him over. What are you planning on doing Rei?"
        rei "Nothing!"
        har "Nothing!? Because it seems to me like you're planning a little sacrifice!"
        fuy "Haruki!"
        show haruki angry
        with Dissolve(0.5)
        har "Oh fuck you too Fuyuhiko!"
        show haruki shut
        with Dissolve(0.5)
        har "I'm done with this, I'll see you all next time..."
        hide haruki
        with Dissolve(0.5)
        show rei at left
        with moveinright
        show fuyu at right
        with moveinleft
        rei "I can't believe him."
        show rei distracted
        with Dissolve(0.5)
        rei "So Shiro, are you coming over?"
        fuy "Yeah"
        rei "Good. We'll leave once club is over."
        jump ReiHouse
    elif ReiChat:
        har "Hey Fuyu~"
        rei "Shiro."
        har "I was just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's almost pitiful."
        $ renpy.pause(2.0)
        rei "Shiro. Can I talk to you, in private?"
        fuy "Oh, uh, sure."
        har "Hey, where are you going? I was just teasing Rei."
        rei "Sure you were, Supai."
        scene hallway afternoon
        hide haruki
        show rei cautious at left
        show fuyu what at right
        with Dissolve(0.5)
        rei "About last night."
        nar "Fuyuhiko groans, remembering their conversation, and what preceeded it."
        show fuyu really
        with Dissolve(0.5)
        fuy "Really, Rei? You don't have to do this, I'm fine."
        rei "I know you aren't Shiro, I saw what happened."
        rei "I just, want to know what's going on."
        show fuyu down
        with Dissolve(0.5)
        nar "Fuyuhiko doesn't respond, instead opting to sit with the other boy in scilence."
        rei "If you don't tell me, I'll just find out through Lantern."
        fuy "You can't do that."
        rei "I can, Shiro."
        fuy "Then prove it."
        rei "I- I can't not here."
        rei "Come ot my house, after club, I'll show you then, okay?"
        hide rei
        with Dissolve(0.5)
        nar "Rei went back into the classroom, but it didn't take long for someone else to emerge from the doorway"
        show haruki frown at left
        with moveinleft
        har "What was that about? I didn't mean to hurt him, honest."
        har "I just, went a little far."
        fuy "This isn't about you Haruki."
        har "What?"
        fuy "It's between me and him, he invited me over to his."
        har "Really? Are you gonna go?"
        show haruki smug
        with Dissolve(0.5)
        har "There might be another boy would love you at his house~"
        menu:
            "Yes":
                har "Well then."
                har "Suit yourself, Fuyu."
                hide haruki
                with Dissolve(0.5)
                nar "Fuyu sat in the hallway for the rest of the club time, thinking about what the hell was going to transpire at Rei's house."
                nar "Until the boy appeared to show him."
                jump ReiHouse
            "No":
                har "Well then."
                har "How come to that other boy's house?"
                show fuyu neut
                with Dissolve(0.5)
                fuyu "I don't see why not."
                jump HarukiHouse
    else:
        har "Hey Fuyu~"
        rei "Hello, Shiro."
        har "I was just getting this guy to talk about that great fire in the sky."
        show fuyu what
        with Dissolve(0.5)
        fuy "The Sun?"
        show rei cautious
        with Dissolve(0.5)
        rei "No!"
        rei "Lantern. He means Lantern."
        fuy "Lantern?"
        har "That god his parents forced our boy into worshipping."
        har "I mean seriously. You're so obsessed, it's almost pitiful."
        show rei shatter
        with Dissolve(0.5)
        rei "They didn't force me into anything, HARUKI!"
        show haruki frown
        show fuyu down
        with Dissolve(0.5)
        $ renpy.pause(2.0)
        har "Rei..."
        har "I- I was just teasing."
        rei "God can you hear yourself!"
        rei "I can't believe you. You can't even believe me, for a second!"
        show rei disappoint
        with Dissolve(0.5)
        rei "What about you Shiro, come to my house after club, I'll show you Lantern's flame."
        show haruki whatever
        with Dissolve(0.5)
        har "Don't do that, don't drag him into this."
        har "If you're going that then, Fuyu, you should come to mine. I haven't gotten a chance to really talk to lately."
        nar "This whole conversation, He's barely processed what happened. And now a choice to make?"
        nar "How about we help our Silver Boy."
        nar "Who's offer should he accept?"
        menu:
            "Haruki's":
                rei "Oh."
                show haruki smug
                with Dissolve(0.5)
                har "Good choice, Fuyu."
                nar "The rest of the time passed awkwardly, Rei eventually drifting to the Konpeki siblings."
                jump HarukiHouse
            "Rei's":
                har "Hmm, fine."
                hide haruki
                show fuyu at right
                with moveinright
                nar "Haruki left the club after what you said, the rest of you followed not soon after."
                jump ReiHouse
#Spacer

#Solo Club time + afternoon
label Nobody:
    if WorkChat:
        nar "Placeholder"
    else:
        nar "Placeholder"
#Spacer

label KonpekiHouse:
    nar "Placeholder"
#Spacer

label HarukiHouse:
    nar "Placeholder"
#Spacer

label ReiHouse:
    nar "Placeholder"
#Spacer
