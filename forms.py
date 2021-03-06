from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired


class NewsCreateForm(FlaskForm):
    title = StringField('Заголовок новости', validators=[DataRequired()])
    content = TextAreaField('Текст новости', validators=[DataRequired()])
    picture = TextAreaField('Картинка новости', validators=[DataRequired()])
    submit = SubmitField('Добавить')
    
   
class CommentCreateForm(FlaskForm):
    title = StringField('Заголовок комментария', validators=[DataRequired()])
    content = TextAreaField('Текст комментария', validators=[DataRequired()])
    submit = SubmitField('Добавить')


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class UserCreateForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Создать')


class ShopForm(FlaskForm):
    scarves = IntegerField('Шарф', validators=[DataRequired()])
    hat = IntegerField('Шапка', validators=[DataRequired()])
    shirt = IntegerField('Футболка', validators=[DataRequired()])
    zna = IntegerField('Значок', validators=[DataRequired()])
    passport = IntegerField('Обложка', validators=[DataRequired()])
    rucksack = IntegerField('Рюкзак', validators=[DataRequired()])
    bre = IntegerField('Брелок', validators=[DataRequired()])
    flag = IntegerField("Флаг", validators=[DataRequired()])
    ball = IntegerField('Мяч', validators=[DataRequired()])
    submit = SubmitField('Далее')
