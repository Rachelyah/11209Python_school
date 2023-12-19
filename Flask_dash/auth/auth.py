from flask import Blueprint,render_template, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, EmailField, BooleanField, DateField
from wtforms.validators import DataRequired, Length,Regexp,Optional

blueprint_auth = Blueprint('auth', __name__,url_prefix='/auth')

class MyForm(FlaskForm):
    name = StringField('姓名', validators=[DataRequired()])


@blueprint_auth.route('/',methods=["GET", "POST"])
@blueprint_auth.route('/login' , methods=["GET", "POST"])
def login():
    form = MyForm()
    if request.method == "POST" and form.validate_on_submit():
        if request.form['name'] == '12345' and request.form['password'] == '12345':
            print('登入成功')
            return redirect('/auth/success')
        else:
            print('密碼錯誤')
        
    return render_template("/auth/login.html", form = form)

@blueprint_auth.route('/success')
def success():
    return render_template('/auth/success.html')

class UserRegistrationForm(FlaskForm):
    uName = StringField("姓名",validators=[DataRequired(message='此欄位必須有資料'), Length(min=2, max=20)])
    uGender = SelectField('性別', choices=[('女', '女'),('男', '男'),('其他','其他')])
    uPhone = StringField('聯絡電話', validators=[Regexp(r'\d\d\d\d-\d\d\d-\d\d\d' , message='格式不正確')])
    uEmail = EmailField('電子郵件',validators=[DataRequired()])
    isGetEmail = BooleanField('是否接受促銷信件',default=False)
    uBirthday = DateField('出生年月日', validators=[Optional()],format='%Y-%m-%d')
    
@blueprint_auth.route('/registor', methods=['GET', 'POST'])
def registor():
    form = UserRegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            uName = form.uName.data
            form.uName.data = ''
            print('姓名',uName)
            
            uGender = form.uGender.data
            print('性別', uGender)
            
            uPhone = form.uPhone.data
            form.uPhone.data = ''
            print('連絡電話', uPhone)
            
            uEmail =  form.uEmail.data
            form.uEmail.data = ''
            print('Email',uEmail)
            
            isGetEmail:bool = form.isGetEmail.data
            print('是否接受促銷信件','接受' if isGetEmail else '不接受')
            
            uBirthday = form.uBirthday.data
            print('生日', uBirthday)
            
        else:
            print('驗證失敗')
            
    return render_template('/auth/registor.html',form=form)