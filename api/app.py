from flask import Flask, render_template, Response, request, redirect, url_for, jsonify, json

import requests

app = Flask(__name__)

from requests.structures import CaseInsensitiveDict

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

@app.route("/")
def blank():

	return render_template('/main_page.html')

