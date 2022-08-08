
def generate_name (name) :
    name = name.split('_')

    if (name != [""]) : 
        fname = name[0].capitalize()
        lname = name[1][::].capitalize()
                        
        full_name = fname + " " + lname
    
    else :
        full_name = ""
        
    return(full_name)