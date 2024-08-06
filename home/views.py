from django.shortcuts import render
import numpy as np
import joblib

model_response = joblib.load('./savedModels/response.pkl')
model_severity = joblib.load('./savedModels/severity.pkl')

def about(request):
    return render(request, 'about.html')

def effects(request):
    return render(request, 'effects.html')

def references(request):
    return render(request, 'references.html')


def index(request):
    if request.method == 'POST':
        try:
            # Retrieve and convert inputs
            species = request.POST.get('species', '0')
            organism = request.POST.get('organism', '0')
            uv_type = request.POST.get('uv_type', '0')
            exposure_intensity = request.POST.get('exposure_intensity', '0')
            exposure_time = request.POST.get('exposure_time', '0')
            organelle = request.POST.get('organelle', '0')
            metabolites = request.POST.get('metabolites', '0')
            proteins = request.POST.get('proteins', '0')
            genes = request.POST.get('genes', '0')
            studied_tissue = request.POST.get('studied_tissue', '0')

            # Create input array
            # Convert features to DataFrame
            final_features = pd.DataFrame(features)

            # Make predictions
            severity_prediction = model_severity.predict(final_features)
            response_prediction = model_response.predict(final_features)

            return render_template('index.html', 
                                severity_prediction=severity_prediction[0],
                                response_prediction=response_prediction[0])

            return render(request, 'home.html', {'result': y_pred})

        except ValueError as e:
            # Handle the case where input conversion fails
            return render(request, 'index.html', {'error': f'Invalid input data: {e}'})
    
    return render(request, 'index.html')
