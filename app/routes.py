from flask import Blueprint, render_template, request
from .ai_engine import generate_ai_response
from .patient_summary import generate_patient_summary

main = Blueprint("main", __name__)


@main.route("/")
def home():

    return render_template("index.html")


@main.route("/chat", methods=["GET","POST"])
def chat():

    answer = None

    if request.method == "POST":

        question = request.form["question"]

        answer = generate_ai_response(question)

    return render_template("chat.html", answer=answer)


@main.route("/summary", methods=["GET","POST"])
def summary():

    result = None

    if request.method == "POST":

        name = request.form["name"]
        age = request.form["age"]
        symptoms = request.form["symptoms"]

        result = generate_patient_summary(name, age, symptoms)

    return render_template("summary.html", result=result)