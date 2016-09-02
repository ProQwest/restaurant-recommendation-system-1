import math

def similarity_calculate(specific_user_rating_ary, specific_user_neighbor_star_ary, neighbor_id_list, average_rating_in_cluster):
    
    user_neighbor_similarity_list=[]
    #print specific_user_rating_ary 
    
    ###Calculate the user's itself rating###
    #user_accumulate_rating=0;
    #num=0
    #for item in specific_user_rating_ary:
    #    user_accumulate_rating=user_accumulate_rating+item['star']
    #    num=num+1
    #user_average_rating=user_accumulate_rating/num
    
    #neighbor_list=[]
    n_id = set()
    for item in specific_user_neighbor_star_ary:
        n_id.add(item['user'])
    neighbor_list=n_id
 
    #print neighbor_list
         
    ###Calculate the similarity###
    for neighbor in neighbor_list:
        
        #for item in average_rating_in_cluster:
        #    if item['user']==neighbor:
        #        neighbor_average_rating=item['average_star']
        
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
            pair_similarity=1.0/(1+math.sqrt(distance))  
            temp={'user':neighbor,'similarity':pair_similarity}        
            user_neighbor_similarity_list.append(temp)
      
    #print user_neighbor_similarity_list
    return user_neighbor_similarity_list
