
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
import os
# from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# metrics = PrometheusMetrics(app)
app.secret_key = os.environ.get("SECRET_KEY", "your_default_secret_key")

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Use your email provider's SMTP server
app.config['MAIL_PORT'] = 587  # Port for TLS
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')  # Store email in environment variable
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')  # Store password in environment variable
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('EMAIL_USER')  # Default sender email

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



# Mail configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER")  # Must be set
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASS")  # Must be set
mail = Mail(app)

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
