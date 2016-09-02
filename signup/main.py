import os
import re
import webapp2

signup="""
<head>

</head>
<body>
<h1>Signup</h1>
    <form method="post">
        <table>
            <tr>
                <td><label for="username">Username</label></td>
                <td>
                    <input name="username" type="text" required>
                    <span style="color: red">%(error_username)s</span>
                </td>
            </tr>
            <tr>
                <td><label for="password">Password</label></td>
                <td>
                    <input name="password" type="password">
                    <span style="color: red">%(error_password)s</span>
                </td>
            </tr>
            <tr>
                <td><label for="verify">Verify Password</label></td>
                <td>
                    <input name="verify" type="password">
                    <span style="color: red">%(error_verify)s</span>
                </td>
            </tr>
            <tr>
                <td><label for="email">Email (optional)</label></td>
                <td>
                    <input name="email" type="email">
                    <span style="color: red">%(error_email)s</span>
                </td>
            </tr>
        </table>
        <input type="submit">
    </form>
</body>
"""

welcome="""
<head>
    <title>Congratulations, You have successfully signed up.</title>
</head>
<body>
    <h2>Welcome, %(username)s!</h2>
</body>
"""

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
def valid_username(username):
    return username and USER_RE.match(username)

PASS_RE = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and PASS_RE.match(password)

EMAIL_RE  = re.compile(r'^[\S]+@[\S]+\.[\S]+$')
def valid_email(email):
    return not email or EMAIL_RE.match(email)


class MainPage(webapp2.RequestHandler):
    def write_form(self, username="", password="", verify="", email="", error_username="",
                   error_password="", error_verify="", error_email=""):
        self.response.out.write(signup % {"username": username,
                                          "password": password,
                                          "verify": verify,
                                          "email": email,
                                          "error_username": error_username,
                                          "error_password": error_password,
                                          "error_verify": error_verify,
                                          "error_email": error_email})

    def get(self):
        self.write_form()

    def post(self):
        have_error = False
        error_username = ""
        error_password = ""
        error_verify = ""
        error_email = ""
        username = self.request.get('username')
        password = self.request.get('password')
        verify = self.request.get('verify')
        email = self.request.get('email')

        if not valid_username(username):
            error_username = "That's not a valid username."
            have_error = True
            error_category = 1

        if not valid_password(password):
            error_password = "That wasn't a valid password."
            have_error = True
            error_category = 2
        elif password != verify:
            error_verify = "Your passwords didn't match."
            have_error = True
            error_category = 3

        if not valid_email(email):
            error_email = "That's not a valid email."
            have_error = True
            error_category = 4


        if have_error:
            if error_category == 1:
                self.response.out.write(signup % {"username": username,
                                                  "password": password,
                                                  "verify": verify,
                                                  "email": email,
                                                  "error_username": error_username,
                                                  "error_password": error_password,
                                                  "error_verify": error_verify,
                                                  "error_email": error_email})
            elif error_category == 2:
                self.response.out.write(signup % {"username": username,
                                                  "password": password,
                                                  "verify": verify,
                                                  "email": email,
                                                  "error_username": error_username,
                                                  "error_password": error_password,
                                                  "error_verify": error_verify,
                                                  "error_email": error_email})
            elif error_category == 3:
                self.response.out.write(signup % {"username": username,
                                                  "password": password,
                                                  "verify": verify,
                                                  "email": email,
                                                  "error_username": error_username,
                                                  "error_password": error_password,
                                                  "error_verify": error_verify,
                                                  "error_email": error_email})

        else:
            self.redirect("/Welcome?username={}".format(username))

class WelcomePage(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('username')
        self.response.out.write(welcome % {"username": username})

app = webapp2.WSGIApplication([('/', MainPage), ('/Welcome', WelcomePage)], debug=True)
