from django.shortcuts import render
import time

def home(request):
    # Check if the session variable 'greeting' is already set
    if 'greeting' not in request.session:
        # Set the session variable 'greeting'
        request.session['greeting'] = 'Hello, Django Sessions!'
    else:
        # Check if the session has timed out
        if 'timeout' not in request.session:
            # Set the session timeout (15 seconds)
            request.session['timeout'] = time.time() + 10
        elif time.time() > request.session['timeout']:
            # If session has timed out, remove the 'greeting' session variable
            del request.session['greeting']
            # Clear the session timeout
            del request.session['timeout']
            # Render a different template to indicate session timeout
            return render(request, 'app_one/session_timeout.html')
    
    # Render the main template
    return render(request, 'app_one/app.html')
