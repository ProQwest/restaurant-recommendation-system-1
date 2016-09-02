import Basic_Recommender
import Data_PreProcessing
import Average_rating
import Similarity_Calculate
import Recommender_Ratings
import json

thershold=0
cluster_number=13932       #13824,13956,13960,13701,        13932:140      
#13824:   one obvious influence people
#13956:
#[{'user': 12567, 'IF': 1}, 
#{'user': 11437, 'IF': 12}, 
#{'user': 2253, 'IF': 1}, 
#{'user': 3462, 'IF': 1}, 
#{'user': 4290, 'IF': 1},
#{'user': 6902, 'IF': 1}, 
#{'user': 7694, 'IF': 1}, 
#{'user': 8179, 'IF': 1}, 
#{'user': 10535, 'IF': 1}, 
#{'user': 11124, 'IF': 1}, 
#{'user': 9817, 'IF': 1}, 
#{'user': 1614, 'IF': 1}, 
#{'user': 4940, 'IF': 13}, 
#{'user': 13956, 'IF': 1}]

#obtain the neighbors' names
cluster_name_list=Data_PreProcessing.find_cluster(cluster_number)
cluster_name_list.append(cluster_number)
#print cluster_name_list    

#obtain the simplified user list
user_restaurant_rating=Data_PreProcessing.read_user()
#Transform neighbors' name to its id
#cluster_id_list=[]
#for each_user in cluster_name_list:
#    cluster_id=Data_PreProcessing.name_id(each_user)    
#    cluster_id_list.append(cluster_id)
#print cluster_id_list
user_influence=[]
for user in cluster_name_list:
    
    IF_Indicator=1
    
    for item in cluster_name_list:
        if item!=user:
            Recommend_Results_With_User=Basic_Recommender.basic_recommender(item)
            
            ##########################Basic recommender results without the user######################
                       
            #specify a user
            user_name=item
    
            #obtain the user's id
            user_id=Data_PreProcessing.name_id(user_name)
            #print user_id
    
            #find the specific user's restaurant and ratings
            specific_user_rating_ary=Data_PreProcessing.find_user_star(user_restaurant_rating,user_id)
            #print specific_user_rating_ary
    
            #obtain the neighbors' names
            neighbors_name_list=Data_PreProcessing.find_cluster(user_name)
            neighbors_name_list.remove(user) ###MUST REMOVE THE USER
            
            #Transform neighbors' name to its id
            neighbor_id_list=[]
            for each_neighbor in neighbors_name_list:
                neighbor_id=Data_PreProcessing.name_id(each_neighbor)    
                neighbor_id_list.append(neighbor_id)
            #print neighbor_id_list
            
            #find the neighbor's restaurant and ratings
            specific_user_neighbor_star_ary=Data_PreProcessing.find_neighbour_star(user_restaurant_rating,neighbor_id_list)
            #print specific_user_neighbor_star_ary
    
            ######################Calculate the average ratings in the cluster###################
            average_rating_in_cluster=Average_rating.average_rating(specific_user_neighbor_star_ary, neighbor_id_list)
            #print average_rating_in_cluster
            #####################################################################################
    
            ################################Calculate the similarity#############################
            specific_user_neighbor_similarity=Similarity_Calculate.similarity_calculate(specific_user_rating_ary, specific_user_neighbor_star_ary, neighbor_id_list, average_rating_in_cluster)
            #####################################################################################
            #print specific_user_neighbor_similarity
    
            Predicted_Ratings=Recommender_Ratings.recommender_ratings(specific_user_neighbor_similarity,specific_user_rating_ary,specific_user_neighbor_star_ary,average_rating_in_cluster)
            #print Predicted_Ratings
            ##############################Obtain the recommendation list#########################
            #####################################################################################
            Predicted_Ratings_sorted = sorted(Predicted_Ratings,key = lambda x:x['pre_star'],reverse=True)
            ##########################################################################################
            
            Recommend_Results_Without_User=Predicted_Ratings_sorted
            
            print Recommend_Results_With_User
            print ("+++++++++++++")
            print Recommend_Results_Without_User
            ##########################################################################################
            ##########################################################################################
            ##########################################################################################
            for result_with_user in Recommend_Results_With_User:
                specific_restaurant=result_with_user['busi']
                flag=0
                for result_without_user in Recommend_Results_Without_User:
                    if result_without_user['busi']==specific_restaurant:
                        flag=1
                        if abs(result_without_user['pre_star']-result_with_user['pre_star'])>thershold:
                            IF_Indicator=IF_Indicator+1
                if flag==0:
                    IF_Indicator=IF_Indicator+1
            ##########################################################################################
            ##########################################################################################
            ##########################################################################################
    temp = {'user':user,'IF':IF_Indicator}
    user_influence.append(temp)
    print user_influence
    
accumulated_influence=0    
for item in user_influence:
    accumulated_influence=accumulated_influence+item['IF']  
#print accumulated_influence 
for item in user_influence:
    numerator=item['IF']*1.0
    item['IF']=numerator/accumulated_influence
#    print item['IF']
    
print(user_influence)

#JSON_Object={"user":item['user'],"IF":item['IF']}
# Writing JSON data
with open('user_influence.json', 'w') as f:
    json.dump(user_influence, f)