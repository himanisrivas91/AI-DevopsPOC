students = ["Anand",20,"Mohan",7,"Himani",7]
print(f"Length of list: {len(students)}")
print(f"My second element is: {students[1]}")


# Trying Dictionary data type

server_details = {
    "server1" :
{
    "servername" :"Test1" ,
    "servertype" : "t2.micro" , 
    "imageid": "ami-123"
},
    "server2" :
{    
    "servername" : "Test2" ,
    "servertype" : "t3.micro" ,
    "imageid" : "ami-123"

}
}
print(f"My first servername of dictionary is: {server_details["server1"]["servername"]}")
print(f"My servertype of second server is: {server_details["server2"]["servertype"]}")