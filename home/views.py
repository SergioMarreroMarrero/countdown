from django.shortcuts import render
from datetime import datetime

def countdown(request):
    arrival_date = datetime(2025, 2, 20, 14, 0)  # Corrección: antes se llamaba homeback_date
    now = datetime.now()
    countdown = arrival_date - now

    return render(request, 'home/index.html', {
        'arrival_date': arrival_date,  # <-- Ahora se envía a la plantilla
        'days': countdown.days,
        'hours': (countdown.seconds // 3600) % 24,
        'minutes': (countdown.seconds // 60) % 60,
        'seconds': countdown.seconds % 60
    })