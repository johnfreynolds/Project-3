import os
import webapp2

signup_form="""
<head>
    <style>
        .error {
            color: red;
        }
    </style>
</head>
<body>
<h1>Signup</h1>
    <form method="post">
        <table>
            <tr>
                <td><label for="username">Username</label></td>
                <td>
                    <input name="username" type="text" value="" required>
                    <span class="error"></span>
                </td>
            </tr>
            <tr>
                <td><label for="password">Password</label></td>
                <td>
                    <input name="password" type="password" required>
                    <span class="error"></span>
                </td>
            </tr>
            <tr>
                <td><label for="verify">Verify Password</label></td>
                <td>
                    <input name="verify" type="password" required>
                    <span class="error"></span>
                </td>
            </tr>
            <tr>
                <td><label for="email">Email (optional)</label></td>
                <td>
                    <input name="email" type="email" value="">
                    <span class="error"></span>
                </td>
            </tr>
        </table>
        <input type="submit">
    </form>
</body>
"""

welcome_form="""
<head>
    <title>Congratulations, You have successfully signed up.</title>
</head>
<body>
    <h2>Welcome, {{username}}!</h2>
</body>
"""

#USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
#def valid_username(username):
#    return username and USER_RE.match(username)

#PASS_RE = re.compile(r"^.{3,20}$")
#def valid_password(password):
#    return password and PASS_RE.match(password)

#EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
#def valid_email(email):
#    return not email or EMAIL_RE.match(email)

#class Handler(webapp2.RequestHandler):
#    def write(self):
#        self.response.out.write(*a, **kw)

class MainPage(Handler):
    def write_form(self, username="", password="", email=""):
        self.response.out.write(signup_form % {"username": username,"password": password, "email": email})

    def get(self):
        self.write(write_form)
        #username = self.request.get('username')
        #if valid_username(username):
        #    self.response.out.write(welcome_form % "username": username)
        #else:
        #    self.response.out.write(signup_form % {"username": username, "password": password, "email": email})

        #have_error = False
        #username = self.request.get('username')
        #password = self.request.get('password')
        #verify = self.request.get('verify')
        #email = self.request.get('email')

        #params = dict(username = username,
        #              email = email)

        #if not valid_username(username):
        #    params['error_username'] = "That's not a valid username."
        #    have_error = True

        #if not valid_password(password):
        #    params['error_password'] = "That wasn't a valid password."
        #    have_error = True
        #elif password != verify:
        #    params['error_verify'] = "Your passwords didn't match."
        #    have_error = True

        #if not valid_email(email):
        #    params['error_email'] = "That's not a valid email."
        #    have_error = True

        #if have_error:
        #    self.response.out.write(form % {"username": username, "password": password, "email": email})
        #else:
        #    self.response.out.write(welcome_form % "username": username)

class WelcomePage(Handler):
    def post(self):
        self.write(welcome_form)

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
