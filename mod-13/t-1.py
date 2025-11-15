from flask import Flask, jsonify
import math

app = Flask(__name__)

def is_prime(value: int) -> bool:
    if value <= 1:
        return False
    for i in range(2, int(math.sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True

@app.get("/alkuluku/<int:number>")
def check_prime(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)