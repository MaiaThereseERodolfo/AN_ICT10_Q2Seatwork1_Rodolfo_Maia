from pyscript import document, display

first_name= {"Maia", "Stephanie", "DJ", "Suzanne", "Holly", "James", "Avery", "Bella", "Edward", "George"}
last_name= {"Rodolfo", "Meyer", "Tanner", "Collins", "Jackson", "Grambs", "Swan", "Cullen", "Martin"}

def check(e):
    first=document.getElementById("first_name").value.strip()
    last=document.getElementById("last_name").value.strip()
    message= document.getElementById("message")

    if first in first_name and last in last_name:
        message.innerHTML= "Welcome, " + str(first) + " " + str(last) + " you are part of the OBMC Book Club!"
    elif first not in first_name or last not in last_name:
        message.innerHTML= "Sorry it appears you are not part of this club!"