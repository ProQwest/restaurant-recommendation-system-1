import If_Recommender
import Data_PreProcessing
import random

def obtain_list(log_user_name):
    
    Recommender_list=[]
    
    Recommender_busi_star=If_Recommender.basic_recommender(log_user_name)
    
    for item in Recommender_busi_star:
        t=item['busi']
        Recommender_list.append(t)
        
    list_length =len(Recommender_list)
    
    
    if list_length<10:
            
        user_restaurant_rating=Data_PreProcessing.read_user()
        
        while len(Recommender_list) < 10:
            
            possible_restaurant_list=random.sample(user_restaurant_rating, 20) 
            
            for item in possible_restaurant_list:
                if item['star']==5:
                    flag=0
                    for obtained_restaurant in Recommender_list:
                        if item['busi']==obtained_restaurant:
                            flag=1
                    if flag==0:
                        t=item['busi']
                        Recommender_list.append(t)
                    
        return Recommender_list[0:10]
    else:
        return Recommender_list    