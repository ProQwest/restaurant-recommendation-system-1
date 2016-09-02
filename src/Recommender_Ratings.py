def recommender_ratings(specific_user_neighbor_similarity,specific_user_rating_ary,specific_user_neighbor_star_ary,average_rating_in_cluster):
        
    ###Calculate the user's itself rating###
    user_accumulate_rating=0;
    num=0
    for item in specific_user_rating_ary:
        user_accumulate_rating=user_accumulate_rating+item['star']
        num=num+1
    if num!=0:
        user_average_rating=user_accumulate_rating/num
    #print user_average_rating

    ###search the possible restaurant### 
    possible_restaurant=set()
    for item in specific_user_neighbor_star_ary:
    
        flag=0
        temp=item['busi']
        for user in specific_user_rating_ary:
            if temp==user['busi']:
                flag=1
        
        if flag==0:
            possible_restaurant.add(temp)
                
    
    predicted_restaurant_rating=[]            
    for restaurant in possible_restaurant:
        
        denominator=0
        numerator=0
        
        for item in specific_user_neighbor_star_ary:
            if restaurant==item['busi']:
                neighbor=item['user']
                for average in average_rating_in_cluster:
                    if average['user']==neighbor:
                        similar_average=average['average_star']       
                for weight in specific_user_neighbor_similarity:
                    if weight['user']==neighbor:
                        similar_weight=weight['similarity']
                        denominator=denominator+similar_weight
                        numerator=numerator+similar_weight*(item['star']-similar_average)
    
        if denominator!=0:    
            predicted_star=user_average_rating+(numerator*1.0)/denominator
            if predicted_star>5:
                predicted_star=5
                
            temp = {'busi':restaurant,'pre_star':predicted_star}
            predicted_restaurant_rating.append(temp)
           
        
    return predicted_restaurant_rating