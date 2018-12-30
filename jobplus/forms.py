from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField, IntegerField
from wtforms.validators import Length, Email, EqualTo, Required, URL, NumberRange
from jobplus.models import db, User


class LoginForm(FlaskForm):
    email = StringField('Emial', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit') 

    def validate_email(self, field):
        if field.data and not User.query.filter_by(email=field.data).first():
            raise ValidationError('The email is not registered!')

    def validate_password(self, field):
        user = User.query.filter_by(email=self.email.data).first()
        if user and not user.check_password(field.data):
            raise ValidationError('Password error!')



class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[Required(), Length(3, 24)])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required(), Length(6, 24)])
    repeat_password = PasswordField('Repeat password', validators=[Required(), EqualTo('password')])
    submit = SubmitField('Submit') 

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already  exists!')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already  exists!')


    def create_user(self):
        user = User(username=self.username.data,
                    email=self.email.data,
                    password=self.password.data)
        db.session.add(user)
        db.session.commit()
        return user


class UserProfileForm(FlaskForm):
    real_name = StringField('RealName')
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Password(If not filled, remain unchanged)')
    phone = StringField('Phone Number')
    work_years = IntegerField('Working Years')
    resume_url = StringField('Resume Url')
    submit = SubmitField('Submit')

    def validate_phone(self, field):
        phone = field.data
        if phone[:2] not in ('13', '15', '18') and len(phone) != 11:
            raise ValidationError('Please input valid mobile phone number')

    def update_profile(self, user):
        user.real_name = self.real_name.data
        user.email = self.email.data
        if self.password.data:
            user.password = self.password.data
        user.phone = self.phone.data
        user.work_years = self.work_years.data
        user.resume_url = self.resume_url.data
        db.session.add(user)
        db.session.commit()
