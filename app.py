import os
from flask import Flask, render_template, request, redirect, url_for, flash
from markupsafe import Markup
import markdown
import re

app = Flask(__name__)
app.secret_key = "yoursecretkey"  # needed for flash messages

import re

def load_posts():
    posts = []
    post_dir = "posts"
    for i, filename in enumerate(sorted(os.listdir(post_dir)), start=1):
        filepath = os.path.join(post_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                continue

            lines = content.splitlines()
            title = lines[0].lstrip("# ").strip() if lines else f"Untitled {i}"
            html_content = markdown.markdown(content)

            # 🔎 Extract chapter number from filename
            # match = re.search(r"chapter\s*_?(\d+)", filename.lower())  
            match = re.search(r"chapter[_\s]?(\d+)", filename.lower())
            if match:
                chap_num = int(match.group(1))
            else:
                chap_num = 0

            # 📚 Assign part automatically
            if 1 <= chap_num <= 5:
                part = "part1"
            elif 6 <= chap_num <= 12:
                part = "part2"
            elif 13 <= chap_num <= 16:
                part = "part3"
            elif 17 <= chap_num <= 22:
                part = "part4"
            elif 23 <= chap_num <= 27:
                part = "part5"
            else:
                part = "misc"

            posts.append({
                # "id": i,
                "id": str(i), 
                "title": title,
                "content": html_content,
                "filename": filename,
                "category": f"ai/{part}",
                "part": part
            })
    return posts


posts = load_posts()
print("=== Loaded Posts ===")
for p in posts:
    print(p["filename"], "->", p["part"], "| id:", p["id"], "| title:", p["title"])


@app.route("/")
def home():
    return render_template("home.html", title="Home", posts=posts)

# @app.route("/ai")
# def ai():
#     return render_template("ai.html", title="AI")


@app.route("/mathematics")
def mathematics():
    return render_template("math_index.html")  

@app.route("/mathematics/section-<int:num>")
def math_section(num):
    # Right now just a placeholder
    return f"<h1>This is Mathematics Section {num}</h1>"


@app.route('/mathematics/Class-12')
def section_1():
    return render_template('Class-12.html')

@app.route('/mathematics/Class-12/ncert')
def section_1_ncert():
    chapters = [
        {"num": 1, "title": "Relations and Functions"},
        {"num": 2, "title": "Inverse Trigonometric Functions"},
        {"num": 3, "title": "Matrices"},
        {"num": 4, "title": "Determinants"},
        {"num": 5, "title": "Continuity and Differentiability"},
        {"num": 6, "title": "Application of Derivatives"},
        {"num": 7, "title": "Integrals"},
        {"num": 8, "title": "Application of Integrals"},
        {"num": 9, "title": "Differential Equations"},
        {"num": 10, "title": "Vector Algebra"},
        {"num": 11, "title": "Three Dimensional Geometry"},
        {"num": 12, "title": "Linear Programming"},
        {"num": 13, "title": "Probability"},
    ]
    return render_template("Class-12-ncert.html", chapters=chapters)


@app.route("/mathematics/class-12/ncert/chapter-<int:ch_num>")
def ncert_chapter(ch_num):
    try:
        filepath = os.path.join("content", "ncert", f"chapter_{ch_num}.md")
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        html = markdown.markdown(content, extensions=["fenced_code", "tables"])
        return render_template(
            "chapter_template.html",
            content=Markup(html),
            chapter=ch_num
        )
    except FileNotFoundError:
        return f"<h1>Chapter {ch_num} not found</h1>", 404



@app.route('/mathematics/Class-12/cbse')
def section_1_cbse():
    return render_template('Class-12-cbse.html')

@app.route('/mathematics/Class-12/icse')
def section_1_icse():
    return render_template('Class-12-icse.html')

@app.route("/ai")
def ai_index():
    # Just show available parts
    parts = {
        "part1": "Foundations",
        "part2": "Supervised Learning in Depth",
        "part3": "Unsupervised & Self-Supervised Learning",
        "part4": "Advanced & Specialized Topics",
        "part5": "Practice & Deployment"
    }
    return render_template("ai_index.html", parts=parts)


@app.route("/ai/<part>")
def ai_part(part):
    # Get all posts (chapters) inside this part
    # chapters = [p for p in posts if p["category"] == f"ai/{part}"]
    chapters = [p for p in posts if p.get("part") == part]
    # Sort by filename (chapter1.md, chapter2.md, …)
    chapters.sort(key=lambda x: int(re.search(r"(\d+)", x["filename"]).group(1)))
    return render_template("ai_part.html", part=part, chapters=chapters)

@app.route("/ai/chapter/<chapter_id>")
def ai_chapter_by_id(chapter_id):
    # find the post with this id
    post = next((p for p in posts if p["id"] == str(chapter_id)), None)
    if not post:
        return "<h1>Chapter not found</h1>", 404

    return render_template(
        "chapter.html",
        content=Markup(post["content"]),
        title=post["title"]
    )
    

@app.route("/ai/<part>/<post_id>")
def ai_chapter_in_part(part, post_id):
    post = next((p for p in posts if p["id"] == str(post_id) and p["part"] == part), None)
    if not post:
        return "Chapter not found", 404

    return render_template("post.html", post=post)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog", posts=posts)

@app.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post:
        return render_template("post.html", title=post["title"], post=post)
    else:
        return "<h2>Post Not Found</h2>", 404

# ✅ NEW CONTACT ROUTE
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # for now, just confirm we received the form
        flash(f"Thanks {name}, your message has been received!")

        # you could also save this data to a file or DB
        return redirect(url_for("contact"))

    return render_template("contact.html", title="Contact")

if __name__ == "__main__":         # for the auto update on the server
    app.run(debug=True)

