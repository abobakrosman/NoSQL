import pymongo

# establishing connection
connection = pymongo.MongoClient("mongodb://localhost")

# handling db and collection
db = connection.school
students = db.students


# function to count the number of students in the collection 
def students_count():
    print("Update All With Low Score ")
    #query = { }

    cnt = 0
    try:
        #counts = students.find(query).count()
        cursor = students.find()
        
        for doc in cursor:
            hw1=doc['scores'][2]['score']
            hw2=doc['scores'][3]['score']
            
            scores_list = []                                    # a null array list
            scores_list.append(doc['scores'][0])                     # 
            scores_list.append(doc['scores'][1])                     # 
            if(hw1>hw2): 
                scores_list.append({"type":"homework","score":hw1})
            else:
                scores_list.append({"type":"homework","score":hw2})
            students.update_one({'_id':cnt}, {'$set': {'scores':scores_list}})
            cnt+=1

    except Exception as ex:
        print("Unexpected Error: ", type(ex), ex)


    
def main():
    students_count()

if __name__ == "__main__":
        main()
# function call
#count = students_count()
#students_detail(count)
