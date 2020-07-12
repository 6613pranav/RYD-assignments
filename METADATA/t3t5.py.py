def Task3(text):
    total = 0
    hindi = 0
    english = 0

    for i in text:
        if ord(i) in range(ord('\u0900'),ord('\u097F')+1):
            hindi+=1
        else:
            english+=1
        total+=1

    if (hindi/total) > 25:
        return "Hindi"

    else:
        return "English"

def Task5(text):
    
    #search for headings to find start and ending of the questions

    
