"""Flask app for FizzBuzzAAS"""
from flask import Flask, request, render_template

app = Flask(__name__)

def is_prime(num):
    """Returns True if num is prime, False otherwise"""
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            # Not prime
            return False
    return True

@app.route('/')
def index():
    """Return homepage."""
    return render_template('index.htm')

@app.route('/fizzbuzz')
def fizzbuzz():
    """
    Returns classic fizzbuzz. Has the following query parameters:
    `limit`: Max number. Default is 100.
    `fizz`: Fizz number. Default is 3.
    `buzz`: Buzz number. Default is 5.
    """
    fizz = int(request.args.get('fizz', 3))
    if fizz < 1:
        return {'Error': 'Fizz must be greater than 0.'}, 400
    buzz = int(request.args.get('buzz', 5))
    if buzz < 1:
        return {'Error': 'Buzz must be greater than 0.'}, 400
    limit = int(request.args.get('limit', 100))
    if limit < 1:
        return {'Error': 'Limit must be greater than 0.'}, 400
    if limit > 1000:
        return {'Error': 'Limit is too large. Max is 1000.'}, 400
    fizzbuzz_list = []
    for i in range(1, limit+1):
        if i % (fizz*buzz) == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif i % fizz == 0:
            fizzbuzz_list.append('Fizz')
        elif i % buzz == 0:
            fizzbuzz_list.append('Buzz')
        else:
            fizzbuzz_list.append(i)
    return {'FizzBuzz': fizzbuzz_list}, 200

@app.route('/fizzbuzz/prime')
def fizzbuzz_prime():
    """
    Returns classic fizzbuzz. Has the following query parameters:
    `limit`: Max number. Default is 100.
    `fizz`: Fizz number. Default is 3.
    `buzz`: Buzz number. Default is 5.
    """
    fizz = int(request.args.get('fizz', 3))
    if fizz < 1:
        return {'Error': 'Fizz must be greater than 0.'}, 400
    buzz = int(request.args.get('buzz', 5))
    if buzz < 1:
        return {'Error': 'Buzz must be greater than 0.'}, 400
    limit = int(request.args.get('limit', 100))
    if limit < 1:
        return {'Error': 'Limit must be greater than 0.'}, 400
    if limit > 1000:
        return {'Error': 'Limit is too large. Max is 1000.'}, 400
    fizzbuzz_list = []
    for i in range(1, limit+1):
        if i % (fizz*buzz) == 0:
            fizzbuzz_list.append('FizzBuzz')
        elif i % fizz == 0:
            fizzbuzz_list.append('Fizz')
        elif i % buzz == 0:
            fizzbuzz_list.append('Buzz')
        elif is_prime(i):
            fizzbuzz_list.append('Prime')
        else:
            fizzbuzz_list.append(i)
    return {'FizzBuzz': fizzbuzz_list}, 200

@app.route('/fizzbuzz', methods=['POST'])
def fizzbuzz_post():
    """
    POST /fizzbuzz that takes in a JSON body with the following fields:
    `targets`: A list of string,int tuples. The string is the target word, 
    and the int is the number to replace.
    `limit`: The max number to count to. Default is 100.
    Example: {"targets": [["Fizz", 3], ["Buzz", 5]], "limit": 100}.
    """
    data = request.get_json()
    targets = data.get('targets')
    if not targets:
        return {'Error': 'Targets is required.'}, 400
    try:
        targets = [(tup[0], int(tup[1])) for tup in targets]
    except IndexError:
        return {'Error': 'Ill-formed targets array.'}, 400
    for target, num in targets:
        if num < 1:
            return {'Error': f'Target numbers must be greater than 0. Error at: [{target}, {num}]'}, 400
    limit = data.get('limit', 100)
    if not limit:
        return {'Error': 'Limit is required.'}, 400
    if limit < 1:
        return {'Error': 'Limit must be greater than 0.'}, 400
    if limit > 1000:
        return {'Error': 'Limit is too large. Max is 1000.'}, 400
    fizzbuzz_list = []
    for i in range(1, limit+1):
        target_names = [tup[0] for tup in targets if i % tup[1] == 0]
        if target_names:
            fizzbuzz_list.append(''.join(target_names))
        else:
            fizzbuzz_list.append(str(i))
    return {'Result': fizzbuzz_list}, 200
