from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import os
import openai

openai.api_key = "your-openAI_api_key"



# Create your views here.
def chat(request):
    return render(request, "index.html")


#this will return json response
def chatAPI(request):
    if request.method == "POST":
        prompt = request.POST['prompt']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.7,
            max_tokens=256, 
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return JsonResponse(response)
    return HttpResponse("Bad request")
