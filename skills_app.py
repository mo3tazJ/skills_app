from flask import Flask, render_template

skills_app = Flask(__name__)


skills_list = [
    ("Python", 95),
    ("Django", 90),
    ("HTML", 85),
    ("CSS", 80),
    ("JS", 75),
    ("Data Science", 90),
]


@skills_app.route("/")
def homepage():
    return render_template(
        "homepage.html",
        context={"title": "Homepage", "test": "TEST"},
        pagetitle="Homepage",
        testing="homepage testing",
        custom_css="home",
    )


@skills_app.route("/skills")
def skills():
    return render_template(
        "skills.html",
        pagetitle="My Skills",
        page_head="My Current Skills",
        description="These are My current Skills",
        testing="skills testing",
        custom_css="skills",
        skills_list=skills_list,
    )


@skills_app.route("/add")
def add():
    return render_template(
        "add.html",
        pagetitle="Add Skill",
        custom_css="add",
    )


@skills_app.route("/about")
def about():
    return render_template(
        "about.html",
        pagetitle="About",
        testing="about testing",
    )


if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
