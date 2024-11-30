from datetime import datetime
#get current date
current_date = datetime.now() .strftime("%Y-%m-%d")

#write to text file today.txt
with open("today.txt", "w") as file:
    file.write(current_date)
    
#read text file into the string today_string
with open("today.txt", "r") as file:
    today_string = file.read()
    
#parse the date
parsed_date = datetime.strptime(today_string, "%Y-%m-%d")
#print parsed date
print(parsed_date)