from flask import Flask, jsonify
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

@app.route('/user/<string:name>')
def get_user(name):
    cached = cache.get(name)
    if cached:
        return jsonify({"name": name, "cached": True, "info": cached.decode('utf-8')})

    data = f"User info for {name}"
    cache.set(name, data)
    return jsonify({"name": name, "cached": False, "info": data})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

