import time
import Data_PreProcessing
import Average_rating
import Similarity_Calculate
import Recommender_Ratings

############################################
#Input: user_name
#Output: Recommended list
############################################
def basic_recommender(needed_user_name, training_data_set):
    
    #start_time = time.clock()
    
    #obtain the simplified user list
    #user_restaurant_rating=Data_PreProcessing.read_user()
    #obtain the simplified restaurant list
    restaurant_list=Data_PreProcessing.read_restaurant()   
    
    #specify a user
    user_name=needed_user_name
    
    #obtain the user's id
    user_id=Data_PreProcessing.name_id(user_name)
    #print user_id
    
    #find the specific user's restaurant and ratings
    specific_user_rating_ary=Data_PreProcessing.find_user_star(training_data_set,user_id)
    #print specific_user_rating_ary
    
    #obtain the neighbors' names
    neighbors_name_list=Data_PreProcessing.find_cluster(user_name)
    
    #Transform neighbors' name to its id
    neighbor_id_list=[]
    for each_neighbor in neighbors_name_list:
        neighbor_id=Data_PreProcessing.name_id(each_neighbor)    
        neighbor_id_list.append(neighbor_id)
    #print neighbor_id_list
    
    #find the neighbor's restaurant and ratings
    specific_user_neighbor_star_ary=Data_PreProcessing.find_neighbour_star(training_data_set,neighbor_id_list)
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
    #print Predicted_Ratings_sorted
    
    #elapsed_time = (time.clock() - start_time)
    #print("Time used:",elapsed_time)
    return Predicted_Ratings_sorted


#needed_user_name=1361

#Result=Basic_Recommender(needed_user_name)
#print Result
