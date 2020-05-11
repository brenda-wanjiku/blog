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

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about yourself', validators=[Required()])
    submit = SubmitField('Submit')

class AddComment(FlaskForm):
    text = TextAreaField('Leave a comment')
    submit = SubmitField('Submit')