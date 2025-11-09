from flask import Flask, render_template

skills_app = Flask(__name__)


@skills_app.route("/")
def homepage():
    return render_template(
        "homepage.html",
        context={"title": "Homepage", "test": "TEST"},
        pagetitle="Homepage",
        testing="testing",
    )


@skills_app.route("/about")
def about():
    return render_template(
        "about.html",
        pagetitle="About",
        testing="testing",
    )


@skills_app.route("/skills")
def skills():
    return render_template(
        "skills.html",
        pagetitle="Skills",
        testing="testing",
    )


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
