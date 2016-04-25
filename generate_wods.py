#!/usr/bin/env python
import random
import os
import sys

from django.conf import settings

import django


TITLES = [
    '12 DAYS OF CHRISTMAS',
    '21-15-9 COMPLEX',
    'AIR FORCE',
    'BASELINE',
    'BEAR COMPLEX',
    'ANNIE, ARE YOU OK?',
    'BEAST 12',
    'BLACK AND BLUE',
    'BLACKJACK',
    'BROOMSTICK MILE',
    'CHRISTINA',
    'BRANDON\'S BAD DAY',
    'CROSSFIT TOTAL',
    'CROSSFIT TOTAL II',
    'CINDY FULL OF GRACE'
]

INITIAL_NOTES = [
    'As Many Reps as Possible (AMRAP) in 31 minutes. With a Partner',
    'For Time',
    '2 Rounds For Time',
    '5 Rounds for Time',
    'AMRAP in 30 minutes'
]

EXERCISES = [
    '8 Deadlifts (155/105 lbs)',
    '7 Cleans (155/105 lbs)',
    '6 Snatches (155/105 lbs)',
    '8 Pull-Ups',
    '7 Chest-to-Bar Pull-Ups',
    '6 Bar Muscle-Ups',
    '6 Deadlifts (155/105 lbs)',
    '5 Cleans (155/105 lbs)',
    '4 Snatches (155/105 lbs)',
    '6 Pull-Ups',
    '5 Chest-to-Bar Pull-Ups',
    '4 Bar Muscle-Ups',
    '4 Deadlifts (155/105 lbs)',
    '3 Cleans (155/105 lbs)',
    '2 Snatches (155/105 lbs)',
    '4 Pull-Ups',
    '3 Chest-to-Bar Pull-Ups',
    '2 Bar Muscle-Ups'
    '30 Jumping Pull-Ups',
    '30 Kettlebell Swings (35/26 lbs)',
    '30 Lunges',
    '30 Knees-to-Elbows',
    '30 Push Press (45/35 lbs)',
    '30 Back Extensions',
    '30 Wall Balls (20/14 lbs)',
    '3 Rounds, For Total Reps in	17 minutes ',
    '1 Minute Burpees',
    '1 Minute Power Snatch (75/55 lbs)',
    '1 Minute Box Jump (24/20 in)',
    '1 Minute Thruster (75/55 lbs)',
    '1 Minute Chest-to-Bar PullUps',
    '1 Minute Rest'
]

FOOT_NOTES = [
    'Complete each exercise in ascending order then work back down to 1, adding one exercise per round. Like this: 1; 2-1; 3-2-1; 4-3-2-1; etc - for a total of 364 reps. There are many variations of this WOD and the movements and weights may be changed to suit the athlete.',
    'Athlete will perform 21 reps (8+7+6=21) of Deadlift/Clean/Snatch then Pull-Ups/Chest-to-Bar PullUps/Bar Muscle-Ups; then	15 reps (6+5+4=15); then 9 reps (4+3+2=9).'
]


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")

    django.setup()

    from wodly.wods.models import Wod, Exercise

    # Generamos 10 WODs para el usuario 1

    for x in xrange(1, 10):
        w = Wod(title=random.choice(TITLES), initial_note=random.choice(INITIAL_NOTES),
                foot_note=random.choice(FOOT_NOTES), user_id=2)
        w.save()
        for y in xrange(1, random.choice(xrange(3, 10))):
            w.exercise_set.create(description=random.choice(EXERCISES))

    print 'Hecho!'
