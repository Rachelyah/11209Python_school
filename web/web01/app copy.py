from flask import Flask, url_for,  render_template

app = Flask(__name__)

#根目錄
@app.route('/') 
def index():
    #print('debug') #會輸出在終端機中
    return render_template('index.html')
#用render function，才會傳出網頁中字串

#hello分頁
@app.route('/hello') 
#@app.route('Hello/<name>')
def hello(name=None):
    return 'Hello, World'

#從網址抓到使用者名稱
#在網址欄位輸入http://127.0.0.1:5000/user/Rachel
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'<h1>User {username}</h1>'

#轉換型別&運算
#在網址欄位輸入http://127.0.0.1:5000/post/10＞會出現Post 50
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'<h1>Post {post_id * 5}</h1>'

#印出路徑
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'<h1>Subpath {subpath}</h1>'

#url_for＞呼叫hello方法的路徑，常用來寫超連結
#也可以連結css檔案，注意路徑寫法&資料夾分類方式
@app.route('/url')
def url():
    print(url_for('hello'))
    print(url_for('show_user_profile',username='RachelYeh')) #傳出網址
    print(url_for('static',filename = 'css/style.css' )) #連結css檔
    return 'ABC'

#用rendering templates 內建function
