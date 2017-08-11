#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS

from core import *

app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return 'Service is running'


@app.route('/handle')
def handle():
    pass


def demo():
    s = '''
    SEARCHING FOR CALIFORNIA'S LOST VIKING TREASURE SHIP
Many parts of the California desert are now patchworks of green, unnaturally fertile land that is a reminder that long ago, there was much more water here, including the vast but now barren Lake Cahuilia.
In the rugged Colorado Desert of California, there lies buried a treasure ship sailed there hundreds of years ago by either Viking or Spanish explorers. Some say this is legend; others insist it is fact. A few have even claimed to have seen the ship, its wooden remains poking through the sand like the skeleton of a prehistoric beast.
Among those who say they’ve come close to the ship is small-town librarian Myrtle Botts. In 1933, she was hiking with her husband in the Anza-Borrego Desert, not far from the border with Mexico. It was early March, so the desert would have been in bloom, its washed-out yellows and grays beaten back by the riotous invasion of wildflowers. Those wildflowers were what brought the Bottses to the desert, and they ended up near a tiny settlement called Agua Caliente. Surrounding place names reflected the strangeness and severity of the land: Moonlight Canyon, Hellhole Canyon, Indian Gorge.
To enter the desert is to succumb to the unknowable. One morning, a prospector appeared in the couple’s camp with news far more astonishing than a new species of desert flora: He’d found a ship lodged in the rocky face of Canebrake Canyon. The vessel was made of wood, and there was a serpentine figure carved into its prow. There were also impressions on its flanks where shields had been attached—all the hallmarks of a Viking craft. Recounting the episode later, Botts said she and her husband saw the ship but couldn’t reach it, so they vowed to return the following day, better prepared for a rugged hike. That wasn’t to be, because, several hours later, there was a 6.4 magnitude earthquake in the waters off Huntington Beach, in Southern California. Botts claimed it dislodged rocks that buried her Viking ship, which she never saw again.
There are reasons to doubt her story, yet it is only one of many about sightings of the desert ship. By the time Myrtle and her husband had set out to explore, amid the blooming poppies and evening primrose, the story of the lost desert ship was already about 60 years old. By the time I heard it, while working on a story about desert conservation, it had been nearly a century and a half since explorer Albert S. Evans had published the first account. Traveling to San Bernardino, Evans came into a valley that was “the grim and silent ghost of a dead sea,” presumably Lake Cahuilla. “The moon threw a track of shimmering light,” he wrote, directly upon “the wreck of a gallant ship, which may have gone down there centuries ago.”
The route Evans took came nowhere near Canebrake Canyon, and the ship Evans claimed to see was Spanish, not Norse. Others have also seen this vessel, but much farther south, in Baja California, Mexico. Like all great legends, the desert ship is immune to its contradictions: It is fake news for the romantic soul, offering passage into some ancient American dreamtime when blood and gold were the main currencies of civic life.
The legend does seem, prima facie, bonkers: a craft loaded with untold riches, sailed by early-European explorers into a vast lake that once stretched over much of inland Southern California, then run aground, abandoned by its crew and covered over by centuries of sand and rock and creosote bush as that lake dried out…and now it lies a few feet below the surface, in sight of the chicken-wire fence at the back of the Desert Dunes motel, $58 a night and HBO in most rooms.
Totally insane, right? Let us slink back to our cubicles and never speak of the desert ship again. Let us only believe that which is shared with us on Facebook. Let us banish forever all traces of wonder from our lives.
Yet there are believers who insist that, using recent advances in archaeology, the ship can be found. They point, for example, to a wooden sloop from the 1770s unearthed during excavations at the World Trade Center site in lower Manhattan, or the more than 40 ships, dating back perhaps 800 years, discovered in the Black Sea earlier this year.
    '''

    s = '''
    Taylor Swift wasn't backing down in court
    Taylor Swift has been praised for her "sharp, gutsy and satisfying" testimony over allegations of sexual assault.
The pop star claims former radio DJ David Mueller groped her while posing for a photo at one of her concerts in 2013 - a charge which he denies.
"Just like her expertly crafted lyrics, Taylor Swift was precise, self-assured and direct," said Billboard magazine.
Speaking in court, Swift refused to back down or give ground to the DJ's lawyer.
Asked if she was critical of her bodyguard, Swift replied: "I'm critical of your client sticking his hand under my skirt and grabbing my ass".
She testified that her security team had seen Mueller "lift my skirt" but only a person on the floor "looking up my skirt" could have seen the entire act "and we didn't have anyone positioned there".
Swift also rejected the accusation that she had misidentified Mueller, saying: "I'm not going to allow you or your client to say I am to blame."
"He had a handful of my ass. It happened to me. I know it was him."
Taylor Swift: He grabbed under my skirt
Taylor Swift's mum confronts DJ in court
Swift 'certain' she was groped by DJ
Taylor Swift trial: What you need to know
Fans and critics have praised her performance on the stand.
"Taylor Swift did not sugarcoat her testimony," said Variety Magazine's Jem Aswad, singling out the moment Mueller's lawyer, Gabriel McFarland, asked why the front of her skirt did not appear to be ruffled in the photograph.
"Because," Swift replied, "my ass is located in the back of my body."
Billboard's Gil Kaufmann applauded the star for refusing to let Mr McFarland sway her interpretation of the incident.
"It happened to me. I have a 3-D rendition of what happened in my brain," he quoted her as saying. "I could have picked him out of a line of 1,000. I know exactly who did this. It is not alleged. It is a fact.
"You can ask me a million questions about it and I'm never going to say anything different."
Buzzfeed's Claudia Rosenbaum, who was in the courtroom, said Swift was at times "aggravated" and "pissed off" at "being forced to relive the details of this incident".
According to the reporter, the star bristled when she was asked why she hadn't called off the meet-and-greet following the alleged incident.
"Mueller's attorney said, 'You could have taken a break,' and Taylor Swift responded: 'And your client could have taken a normal photo with me.'"
Swift's testimony was "sharp, gutsy and satisfying," said Slate magazine's Christina Cauterucci.
"For young fans of Swift's, hearing a beloved artist speak candidly about the emotional damage of sexual assault and stand up to a courtroom of men trying to prove her wrong could be a formative moment for their developing ideas of gender, sex, and accountability."
Fox News reporter Michael Konopasek, meanwhile, noted that elements of Swift's testimony were "heartbreaking" but she "stayed strong throughout".
Fans spoke out in support of the star following her hour-long appearance on the stand.
"Proud and inspired by Taylor Swift today," wrote Alex Goldschmidt. "This is what strength looks like."
"I hope Taylor Swift wins this trial/ There's no excuse for any sexual abuse. She is taking a stand for ALL WOMEN," added Marcus Kawa.
"Taylor Swift has probably watched every single Law And Order episode," concluded one fan account. "She knows what she's doing. She came for blood."
Coincidentally, Swift had been asked in court whether she watched any police shows. "Yes!" she exclaimed. "I named my cat after Olivia Benson on Law and Order."
Following Swift to the witness stand on Thursday was radio station boss Robert Call, who fired Mueller two days after the alleged incident, acting on a complaint from Swift's radio publicist.
Call said Mueller had initially denied touching Swift, but when shown the photo in question, he responded: "Well, if it did happen, it was accidental."
Call said he fired the DJ because of his shifting accounts of the incident, and because the photo showed that Mueller's hand was "not where it was supposed to be".
Mueller, 55, testified on Tuesday that he may have made innocent contact with Swift but denied any inappropriate behaviour.
Asked if he grabbed her backside, the broadcaster replied, "No, I did not."
The trial continues.
    '''

    debug(suggest_article_images(s))


if __name__ == '__main__':
    demo()
    # app.run(threaded=True, host='0.0.0.0', port=5000, debug=DEBUG)
