from io import BytesIO
import uuid
from flask import *
import sqlite3
from datetime import datetime , timedelta
from flask_wtf import *
from sqlite3 import *
import os
import pandas as pd
import matplotlib.pyplot as plt
# from DASHSCOPE import get_AI

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME']=timedelta(days=3)

# 数据库连接函数（确保线程安全）
def get_db_connection():
    conn = sqlite3.connect("comp.sqlite", check_same_thread=False)
    conn.row_factory = sqlite3.Row  # 可选：让查询结果支持字典式访问
    return conn

@app.route('/')
def index():
    return redirect('login')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "GET":
        return render_template('login.html')
    if request.method == "POST":
        data = request.get_json()
        username = data['username']
        password = data["password"]
        
        # 修复 SQL 注入：使用占位符 ? 并传入参数元组
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE Name = ? AND Password = ?", 
                    (username, password))  # 参数列表必须是元组
        res = cur.fetchall()
        conn.close()
        
        if len(res) == 0:  
            return jsonify({"status": "fail"})
        session['USER'] = username
        return jsonify({"status": "success"})
    
@app.route('/main')
def main():
    if 'USER' not in session:
        return redirect(url_for("login"))
    return render_template('main.html')

@app.route('/changepwd',methods=["GET","POST"])
def changepwd():
    if request.method == "GET":
        if 'USER' not in session:
            return redirect(url_for("login"))
        return render_template('changepwd.html')
    if request.method == "POST":
        if 'USER' not in session:
            return jsonify({"status": "fail"})
        
        username = session["USER"]
        data = request.get_json()
        originpwd = data["originpwd"]
        changepwd = data["change"]
        
        # 修复 SQL 注入：查询原始密码
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM Users WHERE Name = ? AND Password = ?", 
                    (username, originpwd))
        res = cur.fetchall()
        
        if len(res) == 0:  
            conn.close()
            return jsonify({"status": "fail",'msg':'原始密码错误！'})
        
        # 修复 SQL 注入：更新密码
        cur.execute("UPDATE Users SET Password = ? WHERE Name = ?", 
                    (changepwd, username))
        conn.commit()
        conn.close()
        
        return jsonify({"status": "success"})

@app.route('/flow',methods=["GET",'POST'])
def flow():
    if request.method == "GET":
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM money ORDER BY ID DESC LIMIT 200')
        res = cur.fetchall()
        conn.close()
        print(res)
        return render_template("flow.html",**locals())
    
    if request.method == "POST":
        data = request.get_json()
        date = data["date"]
        date_easy = date.split(" ")[0]
        price = float(data['price'])
        person = data["person"]
        msg = data['msg']
        
        # 修复 SQL 注入：插入数据
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO money (Time, DATE, User, flow, msg) 
            VALUES (?, ?, ?, ?, ?)
        """, (date, date_easy, person, price, msg))  # 按字段顺序传入参数
        conn.commit()
        conn.close()
        
        return jsonify({'status':'success'})

@app.route("/anaData",methods = ["GET","POST"])
def anaData():
    if request.method == "GET":
        return render_template('anaData.html')
    if request.method == 'POST':
        data = request.get_json()
        type = data["type"]
        Time = data.get("Time")  # 使用 get 避免 KeyError
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        if type == '1': # 全部时间
            cur.execute("SELECT * FROM money")
        
        else: # 指定日期
            cur.execute("SELECT * FROM money WHERE DATE = ?", (Time,))  # 修复 SQL 注入
        
        res = cur.fetchall()

        conn.close()
        
        df = pd.DataFrame(res,columns=['ID','Time','Time2','User','flow','msg'])
        df_outcome = df[df['flow']<0]
        decrease_total = df_outcome['flow'].sum()
        df_income = df[df['flow']>0]
        income_total = df_income['flow'].sum()
        df2 = df.drop(['Time','User'],axis=1)
        detail = df2.values.tolist()
        
        return jsonify({
            "status":'success',
            'income':float(income_total),
            'outcome':float(decrease_total),
            'detail':detail
        })

@app.route('/group',methods=['GET','POST'])     
def group():
    if request.method == "GET":
        return render_template('group.html')
    if request.method == "POST":
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        # 验证日期
        if not start_date or not end_date:
            return jsonify({
                'status': 'fail',
                'msg': '请提供开始和结束日期'
            })

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT DATE, SUM(flow) as daily_total FROM money WHERE DATE >= ? AND DATE <= ? GROUP BY DATE ORDER BY DATE """, (start_date, end_date))

        res = cur.fetchall()
        conn.close()

        result = []
        for row in res:
            # row['DATE'] 是日期，row['daily_total'] 是当天的总收支
            result.append({
                'date': row['DATE'],
                'total': row['daily_total']
            })

        return jsonify({
            'status': 'success',
            'detail': result
        })


@app.route('/category', methods=['GET', 'POST'])
def category_comparison():

    if request.method == 'GET':
        return render_template('category.html')

    if request.method == 'POST':
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')

        if not start_date or not end_date:
            return jsonify({'status': 'fail', 'msg': '请选择完整日期范围'})

        conn = get_db_connection()
        cur = conn.cursor()

        # 只查询支出，并按类别分组求和
        cur.execute("""
            SELECT msg, ABS(SUM(flow)) as total_amount FROM money WHERE DATE >= ? AND DATE <= ? AND flow < 0  GROUP BY msg ORDER BY total_amount DESC""", (start_date, end_date))

        res = cur.fetchall()
        conn.close()

        # 直接返回 [{category: '...', amount: ...}, ...] 格式
        result = [{'category': row['msg'], 'amount': row['total_amount']} for row in res]

        return jsonify({'status': 'success', 'detail': result})


#
#  @app.route('/dashscope',methods=['POST'])
# def dashscope():
#     data = request.get_json()
#     prompt = data["ask"]
#     resp = get_AI(model='qwen-turbo',prompt=prompt,max_tokens=100)
#     if resp:
#         return jsonify({'status':'success','data':resp})
#     return jsonify({'status':'fail'})

@app.route('/export_recent_month_data')
def export_recent_month_data():
    end_date = datetime.datetime.now()
    start_date = end_date - timedelta(days=30)

    # 格式化日期为 'YYYY-MM-DD' 字符串，以便在SQL中使用
    start_date_str = start_date.strftime('%Y-%m-%d')
    end_date_str = end_date.strftime('%Y-%m-%d')

    # 2. 从数据库查询数据
    conn = get_db_connection()
    cur = conn.cursor()

    # 查询最近一个月的所有支出数据
    cur.execute("""
        SELECT id, Time, DATE, User, flow, msg
        FROM money
        WHERE DATE >= ? AND DATE <= ? AND flow < 0
        ORDER BY DATE DESC
    """, (start_date_str, end_date_str))

    data = cur.fetchall()
    conn.close()

    # 3. 如果没有数据，返回提示
    if not data:
        return "最近一个月没有消费数据可导出。"

    # 4. 使用pandas将数据转换为Excel
    # 将 sqlite3.Row 对象列表转换为字典列表
    data_list = [dict(row) for row in data]

    # 创建DataFrame
    df = pd.DataFrame(data_list)

    # 可以对列名进行美化，使其更适合在Excel中展示
    df = df.rename(columns={
        'id': '序号',
        'Time': '收支时间',
        'DATE': '日期',
        'User': '收支人',
        'flow': '流水金额',
        'msg': '备注信息'
    })
    path = f"./upload/{uuid.uuid4()}.xlsx"
    df.to_excel(path, index=False)

    # 5. 准备Excel文件并发送给前端
    return send_file(path, as_attachment=True)



@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 21985, debug=True)