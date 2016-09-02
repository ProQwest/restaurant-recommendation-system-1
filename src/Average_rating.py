def average_rating(specific_user_neighbor_star_ary, neighbor_id_list):
    average_rating_list=[]
    for each_neighbor_in_cluster in neighbor_id_list:
        num=0
        accumulated_rating=0
        for item in specific_user_neighbor_star_ary:
            if each_neighbor_in_cluster==item['user']:
                accumulated_rating=accumulated_rating+item['star']
                num=num+1;
        
        if num!=0:
            average_rating=accumulated_rating/num
            temp={'user':each_neighbor_in_cluster,'average_star':average_rating}
            average_rating_list.append(temp)
    return average_rating_list






