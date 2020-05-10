from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class AddBlog(FlaskForm):
    title = StringField('Blog title ', validators=[Required()])
    description = TextAreaField('Blog:', validators=[Required()])
    submit = SubmitField('Post')

class SubscriberForm(FlaskForm):
    email = StringField(validators=[Required()],render_kw={"placeholder":"Enter your email.."})
    submit = SubmitField('Submit')