import webapp2
from caesar import encrypt
import helpers

form="""
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
            p.error {
                color: red;
            }
        </style>
    </head>
    <body>
        <form method="post">
            <div>
                <label for="rot">Rotate by:</label>
                <input type="text" name="key" value="0">
                <p class="error"></p>
            </div>
            <textarea type="text" name="text">%(text)s</textarea>
            <br>
            <input type="submit">
        </form>
    </body>
"""

class MainPage(webapp2.RequestHandler):
    def write_form(self, text="", key=""):
        self.response.out.write(form % {"key": key,"text": text})

    def get(self):
        self.write_form()

    def post(self):
        key = self.request.get('key')
        text = self.request.get('text')
        encryptedanswer = encrypt(text, key)

        self.write_form(encryptedanswer)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
