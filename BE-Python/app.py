import os
from datetime import datetime, date
from decimal import Decimal
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
app.url_map.strict_slashes = False

# CORS
CORS(app, origins=['http://localhost:5500', 'http://127.0.0.1:5500', 'http://localhost:3000', 'http://localhost', 'http://163.223.12.120'],
     supports_credentials=True,
     allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

# Max upload size 20MB
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024

# Custom JSON serializer for datetime and Decimal
class CustomJSONProvider(app.json_provider_class):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)

app.json_provider_class = CustomJSONProvider
app.json = CustomJSONProvider(app)

# Serve uploaded files
@app.route('/uploads/<path:filename>')
def serve_upload(filename):
    return send_from_directory('uploads', filename)

# Register blueprints (routes)
from routes.auth_routes import auth_bp
from routes.task_routes import task_bp
from routes.submission_routes import submission_bp
from routes.evaluation_routes import evaluation_bp
from routes.leaderboard_routes import leaderboard_bp
from routes.subscription_routes import subscription_bp
from routes.student_routes import student_bp
from routes.company_routes import company_bp
from routes.admin_routes import admin_bp

app.register_blueprint(auth_bp, url_prefix='/api/auth')
app.register_blueprint(task_bp, url_prefix='/api/tasks')
app.register_blueprint(submission_bp, url_prefix='/api/submissions')
app.register_blueprint(evaluation_bp, url_prefix='/api/evaluation')
app.register_blueprint(leaderboard_bp, url_prefix='/api/leaderboard')
app.register_blueprint(subscription_bp, url_prefix='/api/subscription')
app.register_blueprint(student_bp, url_prefix='/api/student')
app.register_blueprint(company_bp, url_prefix='/api/company')
app.register_blueprint(admin_bp, url_prefix='/api/admin')

# Health check
@app.route('/api/health')
def health():
    return jsonify({'status': 'OK', 'timestamp': datetime.now().isoformat()})

# Error handlers
@app.errorhandler(500)
def internal_error(e):
    return jsonify({'message': 'Internal server error'}), 500

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message': 'Not found'}), 404

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    print(f'SkillRank server running on port {port}')
    app.run(host='0.0.0.0', port=port, debug=True)
