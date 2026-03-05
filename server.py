"""Flask app for emotion detection using Watson NLP API."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app:
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_emotion_detector():
    """Analyze the emotion of the given text and return the results."""
    text_to_analyze =  request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract anger, digust,fear, joy and saddness scoes and also dominant emotion
    anger_score = response['anger']
    disgust_score = response['disgust']
    fear_score = response['fear']
    joy_score = response['joy']
    sadness_score = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # If dominant emotion is None, the input was invalid
    if dominant_emotion is None:
        return 'Invalid text! Please try again!'

    return (f"For the given statement, the system response is "
        f"'anger': {anger_score}, 'disgust': {disgust_score}, "
        f"'fear': {fear_score}, 'joy': {joy_score} and "
        f"'sadness': {sadness_score}. The dominant emotion is {dominant_emotion}.")


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template('index.html')


if __name__ == "__main__":
    # executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)
