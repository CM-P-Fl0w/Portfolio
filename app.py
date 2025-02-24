
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os
# from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)
app.secret_key = os.getenv("SECRET_KEY", "fallback_default_key")

if not app.secret_key:
    raise ValueError("No SECRET_KEY set for Flask application. Did you set it in your environment?")

app.config["MAIL_SERVER"] = "smtp.sendgrid.net"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "apikey" 
app.config["MAIL_PASSWORD"] = os.environ.get("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")  # Store API key in environment variables
app.config["MAIL_DEFAULT_SENDER"] = "cjmanleywork@gmail.com" 

mail = Mail(app)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def blog():
    return render_template('about.html')



@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        message_content = request.form.get('message', '').strip()

        if not name or not email or not message_content:
            flash("All fields are required!", "danger")
            return redirect('/contact')

        recipient_email = os.environ.get('EMAIL_USER', 'default@example.com')

        msg = Message(subject=f"New Contact form submission from {name}",
                      sender=email,
                      recipients=[recipient_email],
                      body=f"From: {name} <{email}>\n\n{message_content}")
        try:
            mail.send(msg)
            flash("Message sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending email: {str(e)}", "danger")

        return redirect('/contact')

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
