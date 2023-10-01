from django.shortcuts import render

def chatbox(request, chat_box_name):
    return render(request,'chat.html', {"chat_box_name": chat_box_name})
