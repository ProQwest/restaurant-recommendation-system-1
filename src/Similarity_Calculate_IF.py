import math


def similarity_calculate(specific_user_rating_ary, specific_user_neighbor_star_ary, neighbor_id_list, average_rating_in_cluster,
                          IF_list):
    
    user_neighbor_similarity_list=[]
    
    n_id = set()
    for item in specific_user_neighbor_star_ary:
        n_id.add(item['user'])
    neighbor_list=n_id
 
    #print neighbor_list
         
    ###Calculate the similarity###
    for neighbor in neighbor_list:
        
        neighbor_restaurant_list=[]
        for item in specific_user_neighbor_star_ary:
            if neighbor==item['user']:
                neighbor_restaurant_list.append(item)
        
        #print ("############################################\n")
        #print neighbor_restaurant_list
        #print ("############################################\n") 
              
        distance=0
        flag=0 
        for user_restaurant in specific_user_rating_ary:
            for neighbor_restaurant in neighbor_restaurant_list:
                if user_restaurant['busi']==neighbor_restaurant['busi']:
                    flag=1
                    distance=distance+math.pow(int(user_restaurant['star'])-int(neighbor_restaurant['star']),2)
        
        if flag==1:
            
            #++++++++++++++++++++++++++++++++++++++++++++++++
            #++++++++++++++++++++++++++++++++++++++++++++++++
            for item in IF_list:
                if neighbor==item['user']:
                    IF=100*item['IF']
            #++++++++++++++++++++++++++++++++++++++++++++++++
            #++++++++++++++++++++++++++++++++++++++++++++++++
            
            pair_similarity=(1.0/(1+math.sqrt(distance)))*IF  
           
            temp={'user':neighbor,'similarity':pair_similarity}        
            user_neighbor_similarity_list.append(temp)
    
    #print user_neighbor_similarity_list 
    return user_neighbor_similarity_list
