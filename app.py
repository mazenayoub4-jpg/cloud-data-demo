import os
from flask import Flask, jsonify, request

app = Flask(__name__)

# Mock database / pricing dictionary
PRICING_DATABASE = {
    "A-100": {"code": "A-100", "answer": "سعر العرض 95 دينار · تنبيه: سعر الكتالوج 120 دينار"},
    "B-200": {"code": "B-200", "answer": "سعر العرض 150 دينار · تنبيه: سعر الكتالوج 180 دينار"}
}

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "cloud-data-demo"})

@app.route('/quote')
def quote():
    item_code = request.args.get('code')
    
    if not item_code:
        return jsonify({
            "error": "Missing query parameter 'code'",
            "example": "/quote?code=A-100",
            "available_codes": list(PRICING_DATABASE.keys())
        }), 400

    result = PRICING_DATABASE.get(item_code)
    
    if result:
        return jsonify([result])
    else:
        return jsonify({"error": "Code not found", "code": item_code}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
