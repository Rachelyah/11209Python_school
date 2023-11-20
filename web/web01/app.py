from flask import Flask, url_for,  render_template
import pandas as pd
from auth import auth
from bs import bootstrap

app = Flask(__name__)
app.register_blueprint(auth.bp)
app.register_blueprint(bootstrap.bp)

#根目錄
@app.route('/') 
def index():
    name = 'Rachel'
    dataFrame = get_dataFrame()
    return render_template('index.html', name=name, dataFrame=dataFrame)

#也可以自訂function呼叫
#二維的list，list裡面又有list
def get_dataFrame()->pd.DataFrame:
    data = [['徐國堂', 67, 99, 12],
            ['王小白', 77, 88, 11],
            ['李組長', 77, 11, 44]
            ]
    return pd.DataFrame(data, columns=['姓名', '國文', '英文', '數學'])

