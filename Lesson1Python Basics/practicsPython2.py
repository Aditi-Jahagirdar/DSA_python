def show_excitement():
    text = "I am super excited for this course!"
    show = []
    
    for i in range (5):
        stringText = text + " "
        output = ""
        show.append(stringText)
        for i in range(len(show)):
            output = output + show[i]            
    return output

print (show_excitement())