# ============================================================================
# HEXORA CLOUD SOLUTIONS - ML API BACKEND
# Wrapping our AI in a Flask Server
# ============================================================================

from flask import Flask, request, jsonify

# 1. Initialize the Flask App (Booting up the "Waiter")
app = Flask(__name__)

# Mock Machine Learning Model (Using the math we learned yesterday!)
# CPU_Load = (20.01 * API_Requests) + 0.55
def predict_cpu_load(api_requests_in_hundreds):
    weight = 20.01
    intercept = 0.55
    predicted_load = (weight * api_requests_in_hundreds) + intercept
    # Final CPU Load Equation: CPU% = (20.01 × API Requests) + 0.55
    return predicted_load

# ============================================================================
# ENDPOINT 1: THE HEALTH CHECK (GET REQUEST)
# ============================================================================
# Why we use this: Load balancers ping this URL to make sure the server hasn't crashed.

@app.route('/status', methods=['GET'])
def server_status():
    # We return a JSON dictionary. JSON is the universal language of APIs.
    return jsonify({
        "company": "Hexora Cloud Solutions",
        "status": "Online",
        "version": "1.0.0",
        "message": "API is actively listening for requests."
    }), 200  # 200 is the HTTP status code for "OK"



@app.route('/ping', methods=['GET'])
def server_ping():
    # We return a JSON dictionary. JSON is the universal language of APIs.
    return jsonify({
        "ping": "pong"
    }),200


# ============================================================================
# ENDPOINT 2: THE AI PREDICTION ENGINE (POST REQUEST)
# ============================================================================
# Why we use this: A client sends us their live traffic data, and our AI 
# calculates if their server is about to crash.

@app.route('/predict-load', methods=['POST'])
def predict_load():
    try:
        # 1. Catch the incoming data (The Waiter taking the order)
        # We expect the user to send us JSON data
        incoming_data = request.get_json()
        
        # 2. Extract the specific variable we need
        current_traffic = incoming_data.get('api_requests')
        
        if current_traffic is None:
            return jsonify({"error": "Missing 'api_requests' in JSON payload"}), 400
        
        # 3. Pass the data to the "Kitchen" (Our ML Model)
        ai_prediction = predict_cpu_load(current_traffic)
        
        # 4. Format the response
        warning_flag = "CRITICAL" if ai_prediction > 90 else "STABLE"
        
        # 5. Send the meal back to the customer
        return jsonify({
            "received_traffic": current_traffic,
            "predicted_cpu_load_percent": round(ai_prediction, 2),
            "system_status": warning_flag
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500 # 500 means Internal Server Error

# ============================================================================
# START THE SERVER
# ============================================================================
if __name__ == '__main__':
    print("🚀 Hexora Cloud API booting up on Port 5000...")
    # debug=True means the server will auto-restart if we change the code!
    app.run(host='0.0.0.0', port=5000, debug=True)