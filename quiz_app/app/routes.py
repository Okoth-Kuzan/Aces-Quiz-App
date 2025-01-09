from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegistrationForm
from .models import User

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('quiz/index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login successful!', 'success')
        return redirect(url_for('main.home'))
    return render_template('auth/login.html', form=form)

@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration successful!', 'success')
        return redirect(url_for('main.login'))
    return render_template('auth/register.html', form=form)
