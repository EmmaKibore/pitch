class UpdateProfile(FlaskForm):
    bio = textAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')
