from flask import Flask, request, render_template, redirect
# from flask_debugtoolbar import DebugToolbarExtension
from stories import story_list, get_story

app = Flask(__name__)
# app.config['SECRET_KEY'] = "oh-so-secret"


# debug = DebugToolbarExtension(app)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template("index.html", stories=story_list)
    if request.method == 'POST':
        story_id = request.form["story"]
        print(story_id)
        return redirect(f'/story/{story_id}')

@app.route('/story/<story_id>', methods=["GET", "POST"])
def story(story_id):
    if request.method == 'GET':
        # story_id = request.args["story"]
        print(story_id)
        # find the story object in the story list
        this_story = get_story(story_id)
        
        # send the prompts to a template to make a form out of
        return render_template("story_form.html", story=this_story)
    
    if request.method == 'POST':
        form_data = request.form
        answers = {}
        for each in form_data:
            answers[each] = form_data[each]
        print(answers)

        this_story = get_story(story_id)
        result = this_story.generate(answers)

        return render_template("view_story.html", result=result)