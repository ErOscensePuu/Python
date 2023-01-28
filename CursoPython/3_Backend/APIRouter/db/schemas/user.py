def user_chema(user) -> dict:
   return  {"id":str(user["id"]),
            "username":user["username"],
            "email":user["email"]} 
