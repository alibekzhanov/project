import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings

genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('models/gemini-1.5-pro-latest')


def home(request):
    response_text = None
    prompt_text = None

    if request.method == "POST":
        prompt_text = request.POST.get("prompt", "").strip()
        if prompt_text:
            try:
                response = model.generate_content(prompt_text)
                response_text = response.text
            except Exception as e:
                response_text = f"Error: {str(e)}"

    return render(request, 'main/home.html', {
        "response": response_text,
        "prompt": prompt_text,
    })
