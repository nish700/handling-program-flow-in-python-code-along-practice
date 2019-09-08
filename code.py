# --------------
import json
from collections import Counter
with open(path) as f:
    data = json.load(f)

#data 
 
# Code starts here

# #  Can you find how many deliveries were faced by batsman  `SC Ganguly`.
first_inning_deliveries = data['innings'][0]['1st innings']['deliveries']


def number_of_delivers(player):
    count_deliveries=0
    batsman = []
    for delivery in first_inning_deliveries:    
        for delivery_no, delivery_info in delivery.items():
            if delivery_info['batsman'] == player:
                batsman.append(delivery_info['batsman'])
                count_deliveries +=1
    print("{0} deliveries played by {1}".format(count_deliveries,batsman[0]))
    return count_deliveries

deliveries = number_of_delivers('BB McCullum')

# #  Who was man of the match and how many runs did he scored ?
info_details = data['info']
man_of_the_match = info_details['player_of_match'][0]
print("Man of the match is {}".format(man_of_the_match))

count_runs=0
for delivery in first_inning_deliveries:
    for delivery_no,delivery_info in delivery.items():
        if delivery_info['batsman'] == man_of_the_match:
            count_runs+= delivery_info['runs']['batsman']
print("{0} scored {1}".format(man_of_the_match,count_runs))
            


#  Which batsman played in the first inning?
batsman_list=[]
for delivery in first_inning_deliveries:
    for delivery_no,delivery_info in delivery.items():
        if delivery_info['batsman'] not in batsman_list:
            batsman_list.append(delivery_info['batsman'])
            ## can also be done by using set
            ## batsman_list = set(batsman_list)
print(batsman_list)

number_of_deliverss = [ number_of_delivers(batsman) for batsman in batsman_list]
print(number_of_deliverss)

# Which batsman had the most no. of sixes in first inning ?
sixes_scored_batsman=[]
six_count=0
for delivery in first_inning_deliveries:    
    for delivery_no,delivery_info in delivery.items():
            if delivery_info['runs']['batsman'] == 6:
                sixes_scored_batsman.append(delivery_info['batsman'])
                #six_count+=1
                #six_scored= (delivery_info['batsman'], six_count)
sixes_dict = Counter(sixes_scored_batsman)
max_6_player = max(sixes_dict,key=sixes_dict.get)
print(max_6_player)


# Find the names of all players that got bowled out in the second innings.

second_inning_bowled_out = []

second_inning_deliveries = data['innings'][1]['2nd innings']['deliveries']

for delivery in second_inning_deliveries:    
    for delivery_no,delivery_info in delivery.items():
        if ('wicket' in delivery_info) and (delivery_info['wicket']['kind']=='bowled'):
            second_inning_bowled_out.append(delivery_info['wicket']['player_out'])
print(second_inning_bowled_out,'bowled out')


# # How many more "extras" (wides, legbyes, etc) were bowled in the second innings as compared to the first inning?
# for delivery in second_inning_deliveries:    
#     for delivery_no,delivery_info in delivery.items():
#         if 'extras' in delivery_info:
#             #print(delivery_info)

first_inning_extras = len([delivery_info for delivery in first_inning_deliveries
                             for delivery_no,delivery_info in delivery.items()
                             if 'extras' in delivery_info
                            ])

second_inning_extras = len([delivery_info for delivery in second_inning_deliveries 
                              for delivery_no,delivery_info in delivery.items() 
                              if 'extras' in delivery_info])



print("Extra runs in First Innings are {0} and extra runs in second innings are {1}. More extras are {2}".format(first_inning_extras,second_inning_extras,(second_inning_extras-first_inning_extras)))



# Code ends here


