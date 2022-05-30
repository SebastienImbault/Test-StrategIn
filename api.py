# -*- coding: utf-8 -*-
"""
Created on Fri May 13 17:55:03 2022

@author: seble
"""
import flask
from flask import request
import re

app = flask.Flask(__name__)

app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def health():

    return "<h1> health :</h1><p>API is ready.</p>"


@app.route('/longestCommonStreak', methods=['GET'])
def api_id23():
    """
    string1 = "apple pie available"
    string2 = "come have some apple pies"
    match = SequenceMatcher(None, string1, string2).find_longest_match()
    print(match) # -> Match(a=0, b=15, size=9)
    print(string1[match.a:match.a + match.size]) # -> apple pie
    print(string2[match.b:match.b + match.size]) # -> apple pie
    """
    
    string1="python"
    string2="pyjjjthojjj"
    if 'string2' in request.args:
        string1 = request.args['string1']

        string2 = request.args['string2']

    len1, len2 = len(string1), len(string2)
    answer = ""
    if len1 <= len2:
        
        for lettre in range(len1):
            
            i=len1 -1

            while len1-i != len1:
        
                if string1[lettre:i] in string2:
                    
                    if len(string1[lettre:i]) > len(answer):
                        answer = string1[lettre:i]
                    # if string1[:i] 
                    break
                i-=1
            else:
                print ("rien")
    else:
        
        for lettre in range(len2):
            i=len2 -1
            while len2-i != len2:
                
                if string2[lettre:i] in string1:
                    if len(string2[lettre:i]) > len(answer):
                        answer = string2[lettre:i]
                    break
                i-=1
            else:
                print ("rien")
                
    return answer
    
    

@app.route('/emailValidation', methods=['GET'])

def emailValidation():

    your_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
    pattern = re.compile(your_pattern)

    # here is an example list of email to check it at the end
    email= ""
    if 'email' in request.args:
        email = request.args['email']
    if not re.match(pattern, email):
        is_valid= "False"
    else:
        is_valid= "True"

    return is_valid



app.run(host='0.0.0.0', port = 5001)