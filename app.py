from flask import Flask, render_template, request, redirect, url_for

import api

app = Flask(__name__)

# 设置密码变量


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/Error')
def Error():
    return render_template('Error.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    option = request.form['option']
    # 执行查询操作并获取结果
    result = api.url(option,query)
    return render_template('index.html', result=result)

@app.route('/protected', methods=['GET', 'POST'])
def protected():
    password = api.Judgment()[1]
    if request.method == 'POST':
        entered_password = request.form['password']
        # 验证密码
        if entered_password == password:
            return render_template('protected_page.html')
        else:
            return render_template('Error.html')
    else:
        return render_template('protected.html')
@app.route('/nbsearch', methods=['POST'])
def nbsearch():
    query = request.form['query']
    # 执行查询操作并获取结果
    result = api.Enquiries(query)
    print(result)
    return render_template('protected_page.html', result=result)
if __name__ == '__main__':
    app.run(host='127.0.0.1',port=8080)
