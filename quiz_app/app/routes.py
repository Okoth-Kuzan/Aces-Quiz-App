from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Handle form submission (quiz logic)
        pass
    return render_template('quiz.html')
