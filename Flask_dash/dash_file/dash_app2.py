from dash import Dash, html, dash_table, callback, Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
from . import datasource

lastest_data = datasource.lastest_datetime_data()
lastest_df = pd.DataFrame(lastest_data,columns=['站點名稱','更新時間','行政區','地址','總數','可借','可還'])
lastest_df1 = lastest_df.reset_index()
lastest_df1['站點名稱'] = lastest_df1['站點名稱'].map(lambda name:name[11:])

#建立一個Dash的實體，加入網址、style設定
dash2 = Dash(requests_pathname_prefix="/dash/app2/", external_stylesheets=[dbc.themes.BOOTSTRAP])
dash2.title='台北市'


#dash.html的layout，不適合複雜的html結構
dash2.layout = html.Div(
[
    dbc.Container([
        html.Div([
            html.Div([
                    html.H1("台北市youbike查詢"),
                ],className="col text-center")
        ],
        className="row",
        style={'paddingTop':'2rem'}),
        #第二個row，在同一個div裡面
        html.Div([
            html.Div([
                dash_table.DataTable(
                        id = 'main_table',
                        data=lastest_df1.to_dict('records'),
                        columns=[{'id':column,'name':column} for column in lastest_df1.columns],
                        page_size=20,
                        style_table={'height': '300px', 'overflowY': 'auto'},
                        fixed_rows={'headers': True},
                        style_cell_conditional=[
                                {   'if': {'column_id': 'index'},
                                 'width': '5%'
                                },
                                {   'if': {'column_id': '站點名稱'},
                                 'width': '25%'},
                                {   'if': {'column_id': '總數'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可借'},
                                 'width': '5%'},
                                {   'if': {'column_id': '可還'},
                                 'width': '5%'},
                        ], 
                        row_selectable='single', #新增可點選的欄位，推定一次點一個欄位
                        selected_rows=[]     #預設一開始不要點選，要的話可以在[]中新增預設索引值
                        ),
                ],className="col text-center")
        ],
        className="row",
        style={"paddingTop":'2rem'}),
        html.Div([
            html.H5("這是第3列",className="col",id='showMessage')
            ],
            className="row",
            style={"paddingTop":'2rem'})
        ])
    ],
    className="container-lg"
    )

@callback(
    Output('showMessage','children'),
    Input('main_table','selected_rows'),
    

)

def selected_Rows(selected_rows):
        print(selected_rows)
        print('2')
        return str(selected_rows)