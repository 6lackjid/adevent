
```mermaid
erDiagram
USER ||--o{ EVENT : ""
EVENT ||--|| JENRE : ""
USER ||--|| MYPAGE : "" 




USER {  
number id  
string name  
string address  
string email  
string password  
number phonenumber 
}


EVENT {  
number id  
string eventTitle
date eventDate  
time eventTime  
string location  
string eventHost
string eventOverView

}  


JENRE {  
string jenre  
}

MYPAGE {  
string joinedHistory  
string hostedHistory
}
```