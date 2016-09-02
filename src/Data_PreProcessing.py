import json

#-------------------------Restaurant Data Process---------------------
###Obtain the restaurant with (Restaurant_name, ID)
def read_restaurant():
    dataread = []

    for line in open('rest_pitt.json','r'):
        temp_line = json.loads(line)
        dataread.append(temp_line)

    restaurant_list = []

    for item in dataread:
        t = {'name':item['name'].encode('utf-8'),'busi':item['business_id'].encode('utf-8')}
        restaurant_list.append(t)
    return restaurant_list

###Obtain the restaurant name with specific ID
def find_restaurant_name(restaurant_Dic,restaurant_id):
    for restaurant in restaurant_Dic:
        if restaurant['busi']==restaurant_id:
            name_restaurant=restaurant['name']
            #break
            return name_restaurant
#---------------------------------------------------------------------

#-------------------------User Data Process---------------------------
###Obtain the user with (user_name, busi_ID, Star)  ###
def read_user():
    dataread = []

    for line in open('user_pitt.json','r'):
        t = json.loads(line)
        dataread.append(t)

    user_item_list = []

    for item in dataread:
        t = {'user':item['user_id'].encode('utf-8'),'busi':item['business_id'].encode('utf-8'),'star':item['stars']}
        user_item_list.append(t)
    return user_item_list

###Obtain the user name with specific ID
def name_id(user_name):
    with open ('map_userid.json','r') as f:
        data = json.load(f)
        for key in data:
            if user_name==data[key]:
                return key.encode('utf-8')
#---------------------------------------------------------------------

#----------------------Find neighbours in the cluster-----------------
def find_cluster(user_id):
    with open ('output-final_3234.json','r') as f:
        data = json.load(f)
        for key in data:
            specific_user_cluster=data[key]
            if user_id in specific_user_cluster:
                specific_user_cluster.remove(user_id)
                return specific_user_cluster
#----------------------------------------------------------------------

#---------------------User_id and stars of restaurants-----------------
#find busi id and star for the target user
def find_user_star(user_restaurant_list,user_id):
    specific_user_rating_ary=[]
    for item in user_restaurant_list:
        if item['user']==user_id:
            specific_user_rating_ary.append(item)

    return specific_user_rating_ary

#find busi id and star for specific user's neighbors
def find_neighbour_star(user_restaurant_list,specific_user_cluster):
    specific_user_neighbor_star_ary=[]
        
    for item in user_restaurant_list:
        for neighbour in specific_user_cluster:
        
            if item['user']==neighbour:
                specific_user_neighbor_star_ary.append(item)
    return specific_user_neighbor_star_ary
#-----------------------------------------------------------------------

#---------------------User_id and stars of restaurants------------------
def cluster_IF_search(user_name):
    with open ('output-final_3234.json','r') as f:
        data = json.load(f)
        for key in data:
            specific_user_cluster=data[key]
            if user_name in specific_user_cluster:
                cluster_number=key 
                #print cluster_number
            
    if cluster_number=='13633':
        
        with open ('pr13633.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                #print key.encode('utf-8')
                user_ID=name_id(int(key.encode('utf-8')))
                 
                #print user_ID                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list
           
    elif cluster_number=='13701':

        with open ('pr13701.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                user_ID=name_id(int(key.encode('utf-8')))
                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list

    elif cluster_number=='13864':

        with open ('pr13864.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                user_ID=name_id(int(key.encode('utf-8')))
                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list

    elif cluster_number=='13873':
        
        with open ('pr13873.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                user_ID=name_id(int(key.encode('utf-8')))
                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list
        
    elif cluster_number=='13899':
    
        with open ('pr13899.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                user_ID=name_id(int(key.encode('utf-8')))
                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list
    
    elif cluster_number=='13916':
        
        with open ('pr13916.json','r') as f:
            data = json.load(f)
    
            IF_list=[]
            for key in data:
                
                user_ID=name_id(int(key.encode('utf-8')))
                
                t = {'user':user_ID,'IF':data[key]}
                IF_list.append(t)
    
        return IF_list
    
    else:
        Error = 'Invalid User' 
        print Error
#------------------------------------------------------------------------


