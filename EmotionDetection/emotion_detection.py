import requests
import json

def emotion_detector(text_to_analyze):
    """
    Envía texto a la API de Watson NLP Emotion Predict y devuelve 
    un diccionario formateado con las puntuaciones de las emociones.
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    
    # Enviar la solicitud POST a la API
    response = requests.post(url, headers=headers, json=input_json)
    
    # Convertir el texto de respuesta en un diccionario
    formatted_response = json.loads(response.text)
    
    # Extraer el diccionario de emociones de la respuesta
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Encontrar la emoción dominante (la que tiene el valor más alto)
    emotion_scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    
    # Formatear la salida final
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result