from flask import Flask, render_template, request, redirect, flash
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "idklol"

responses = []
survey = satisfaction_survey

@app.route("/")
def start_survey():
    title = survey.title
    instructions = survey.instructions
    return render_template("start.html", title = title, instructions = instructions)

@app.route("/questions/<index>")
def handle_question(index):
    index = int(index) 
    print(responses)
    #if they have finished the survey
    if len(responses) == len(survey.questions):
        return redirect("/thankyou")
    #if they are trying to access question that they're not on
    if index != len(responses):
        flash("Can't access invalid question")
        return redirect(f"/questions/{len(responses)}")
    question_obj = survey.questions[index]
    question = question_obj.question
    choices = question_obj.choices
    return render_template("question.html", question=question, choices=choices, index=index)

@app.route("/answer", methods=["POST"])
def post_answer():
    #gets selected answer and appends it to responses
    answer = request.form.get("answer")
    responses.append(answer)

    index = int(request.form.get("index"))
    if len(responses) == len(survey.questions):
        return redirect("/thankyou")
    else:
        index += 1
        return redirect(f"/questions/{str(index)}")
    
@app.route("/thankyou")
def thanks_you():
    return render_template("thankyou.html")
    

