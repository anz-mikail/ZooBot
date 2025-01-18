import os
from answer import *
from function import max_points


TOKEN = os.getenv("TOKEN")


text_start = ['Повторить ещё', "Начать викторину"]

text_ocean = [answer['start'][2]]
text_south = [answer['ocean'][2]]
text_pre_herb = [
    answer['start'][1], answer['start'][3], answer['start'][4], answer['start'][5], answer['ocean'][1]
]
text_predatory = [answer['pre_herb'][1]]
text_herbivores = [answer['pre_herb'][2]]
text_birds = [answer['plain_herb'][2]]
text_step_south_bats = [
    answer['start'][6], answer['south'][1], answer['south'][2], answer['south'][3]
]
text_step_wood = [
    answer['wood'][1], answer['wood'][2], answer['wood'][3], answer['wood'][4], answer['wood'][5]
]
text_step_plain = [
    answer['plain_pre'][1], answer['plain_pre'][2], answer['plain_pre'][3],
    answer['plain_herb'][1], answer['plain_herb'][3], answer['plain_herb'][4], answer['plain_herb'][5],
    answer['plain_herb'][6]
]
text_step_birds = [
    answer['birds'][1], answer['birds'][2], answer['birds'][3], answer['birds'][4], answer['birds'][5],
    answer['birds'][6]
]
text_step_1 = []
if question_2:
    text_step_1 = [answer['step_1'][1], answer['step_1'][2], answer['step_1'][3], answer['step_1'][4]]
text_step_2 = []
if question_3:
    text_step_2 = [answer['step_2'][1], answer['step_2'][2], answer['step_2'][3], answer['step_2'][4]]
text_step_3 = []
if question_4:
    text_step_3 = [answer['step_3'][1], answer['step_3'][2], answer['step_3'][3], answer['step_3'][4]]
text_step_4 = []
if question_5:
    text_step_4 = [answer['step_4'][1], answer['step_4'][2], answer['step_4'][3], answer['step_4'][4]]
text_step_5 = []
if question_6:
    text_step_5 = [answer['step_5'][1], answer['step_5'][2], answer['step_5'][3], answer['step_5'][4]]
text_step_6 = []
if question_7:
    text_step_6 = [answer['step_6'][1], answer['step_6'][2], answer['step_6'][3], answer['step_6'][4]]
text_step_7 = []
if question_8:
    text_step_7 = [answer['step_7'][1], answer['step_7'][2], answer['step_7'][3], answer['step_7'][4]]
text_step_8 = []
if question_9:
    text_step_8 = [answer['step_8'][1], answer['step_8'][2], answer['step_8'][3], answer['step_8'][4]]
text_step_9 = []
if question_10:
    text_step_9 = [answer['step_9'][1], answer['step_9'][2], answer['step_9'][3], answer['step_9'][4]]
text_step_10 = []


text_step_end = []
if max_points == 21:
    text_step_end = [answer['step_1'][1], answer['step_1'][2], answer['step_1'][3], answer['step_1'][4]]
elif max_points == 41:
    text_step_end = [answer['step_2'][1], answer['step_2'][2], answer['step_2'][3], answer['step_2'][4]]
elif max_points == 61:
    text_step_end = [answer['step_3'][1], answer['step_3'][2], answer['step_3'][3], answer['step_3'][4]]
elif max_points == 81:
    text_step_end = [answer['step_4'][1], answer['step_4'][2], answer['step_4'][3], answer['step_4'][4]]
elif max_points == 101:
    text_step_end = [answer['step_5'][1], answer['step_5'][2], answer['step_5'][3], answer['step_5'][4]]
elif max_points == 121:
    text_step_end = [answer['step_6'][1], answer['step_6'][2], answer['step_6'][3], answer['step_6'][4]]
elif max_points == 141:
    text_step_end = [answer['step_7'][1], answer['step_7'][2], answer['step_7'][3], answer['step_7'][4]]
elif max_points == 161:
    text_step_end = [answer['step_8'][1], answer['step_8'][2], answer['step_8'][3], answer['step_8'][4]]
elif max_points == 191:
    text_step_end = [answer['step_9'][1], answer['step_9'][2], answer['step_9'][3], answer['step_9'][4]]
elif max_points == 201:
    text_step_end = [answer['step_10'][1], answer['step_10'][2], answer['step_10'][3], answer['step_10'][4]]




