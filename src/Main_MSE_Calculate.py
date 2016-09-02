import Data_PreProcessing
import json
import math
import random
import Basic_Recommender_Test
import If_Recommender_Test

cluster_name=13899     
percent=0.8

cluster_id=Data_PreProcessing.name_id(cluster_name)

whole_data_set=Data_PreProcessing.read_user()

with open ('output-final_3234.json','r') as f:
    data = json.load(f)
    for key in data:
        if key==str(cluster_name):
            specific_user_cluster=data[key]
     
with open ('map_userid.json','r') as f:
    user_id_name_map = json.load(f) 
        
#Transform neighbors' name to its id
cluster_id_list=[]
for each_neighbor in specific_user_cluster:
    cluster_id=Data_PreProcessing.name_id(each_neighbor)    
    cluster_id_list.append(cluster_id)
#print neighbor_id_list
        
Cluster_data_set=Data_PreProcessing.find_neighbour_star(whole_data_set,cluster_id_list)
Cluster_data_set_length=len(Cluster_data_set)

test_data_set_length= math.ceil( (1-percent)*Cluster_data_set_length )

#obtain test data set and training data set
test_data_set=random.sample(Cluster_data_set, int(test_data_set_length)) 
training_data_set=[]
for item in Cluster_data_set:
    flag=0
    for item2 in test_data_set:
        if item['user']==item2['user'] and item['busi']==item2['busi']:
            flag=1
    if flag==0:
        training_data_set.append(item)

print test_data_set
print training_data_set

MSE_BR=0
MSE_IF=0
Num_MSE_BR=0
Num_MSE_IF=0

for item in test_data_set:
    specific_user=item['user']
    needed_user_name=user_id_name_map[specific_user] 
    
    print needed_user_name       
    BR_results=Basic_Recommender_Test.basic_recommender(needed_user_name, training_data_set)
    IF_results=If_Recommender_Test.basic_recommender(needed_user_name, training_data_set)

    print BR_results
    print IF_results
    for BR_each_result in BR_results:
        if BR_each_result['busi']==item['busi']:
            MSE_BR=MSE_BR+math.pow((BR_each_result['pre_star']-item['star']),2)
            Num_MSE_BR=Num_MSE_BR+1
            
    for IF_each_result in IF_results:
        if  IF_each_result['busi']==item['busi']:
            MSE_IF=MSE_IF+math.pow((IF_each_result['pre_star']-item['star']),2)       
            Num_MSE_IF=Num_MSE_IF+1

BR_MSE_final=math.sqrt(MSE_BR/Num_MSE_BR)
IF_MSE_final=math.sqrt(MSE_IF/Num_MSE_IF)
#average_rating_list=average_rating(training_data_set, neighbor_id_list)
print BR_MSE_final
print IF_MSE_final








