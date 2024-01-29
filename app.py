from flask import Flask, render_template, request, redirect, flash, session
from surveys import surveys

app = Flask(__name__)
app.config['SECRET_KEY'] = "idklol"

responses = []

@app.route("/choose")
def choose_survey():
    return render_template("choose.html", survey_names = surveys.keys())

@app.route("/handleSurveyPick", methods=["POST"])
def handle_survey_pick():
    survey_name = request.form.get("survey")
    session["survey_name"] = survey_name
    return redirect("/")

@app.route("/")
def start_survey():
    survey_name = session.get("survey_name", "satisfaction")
    survey = surveys[survey_name]

    return render_template("start.html", title = survey.title, instructions = survey.instructions)

@app.route("/resetSession", methods=["POST"])
def reset_session():
    session["responses"] = []
    return redirect("/questions/0")

@app.route("/questions/<int:index>")
def handle_question(index):
    survey_name = session.get("survey_name", "satisfaction")
    survey = surveys[survey_name]

    responses = session["responses"]

    print(session["responses"])
    
    #if they have finished the survey
    if len(responses) == len(survey.questions):
        return redirect("/thankyou")
    #if they are trying to access question that they're not on
    if index != len(responses):
        flash("Can't access invalid question")
        #redirects them to correct question
        return redirect(f"/questions/{len(responses)}")
    
    question_obj = survey.questions[index]
    return render_template("question.html", question=question_obj.question, choices=question_obj.choices, allow_text=question_obj.allow_text, index=index)

@app.route("/answer", methods=["POST"])
def post_answer():
    survey_name = session.get("survey_name", "satisfaction")
    survey = surveys[survey_name]

    #gets comment
    comment = request.form.get("comment", "")
    #gets selected answer
    answer = request.form.get("answer")
    #sets full answer to answer & comment dict
    full_answer = {"answer": answer,
                   "comment": comment}

    

    #appends it to responses
    responses = session["responses"]
    responses.append(full_answer)
    session["responses"] = responses

    #if all questions are answered, redirect to thank you route
    if len(responses) == len(survey.questions):
        return redirect("/thankyou")
    else:
        #goes to next question route
        return redirect(f"/questions/{len(responses)}")
    
@app.route("/thankyou")
def thanks_you():
    survey_name = session.get("survey_name", "satisfaction")
    survey = surveys[survey_name]
    responses = session["responses"]

    return render_template("thankyou.html", responses=responses, survey=survey, questions=survey.questions,)
    

