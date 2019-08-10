from flask import Flask
from pattern.en import suggest
from flask import jsonify
import json
from flask import request

check = Flask(__name__)

#allow both GET and POST requests
@check.route('/pySpellCheck', methods=['GET', 'POST'])

def spell():
    if request.method == 'POST':  #this block is only entered when the form is submitted
        word = request.form.get('word')

        return jsonify({'data':json.dumps(suggest(word))})

    return '''<form method="POST">
                  Word: <input type="text" name="word"><br>
                  <input type="submit" value="Submit"><br>
              </form>'''

if __name__ == '__main__':
    check.run(debug=True)
