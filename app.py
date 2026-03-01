from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS menu (id INTEGER PRIMARY KEY, name TEXT, price REAL)')
    
    c.execute('SELECT COUNT(*) FROM menu')
    if c.fetchone()[0] == 0:
        sample_menu = [
            ('Espresso', 50.0),
            ('Americano', 55.0),
            ('Latte', 60.0),
            ('Mocha', 65.0),
            ('Matcha Green Tea', 70.0),
            ('Thai Tea', 45.0)
        ]
        c.executemany('INSERT INTO menu (name, price) VALUES (?, ?)', sample_menu)
    
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM menu')
    items = c.fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('INSERT INTO menu (name, price) VALUES (?, ?)', (name, price))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/about')
def about(): 
    text = "ร้านกาแฟของเราเริ่มต้นจากความหลงใหลในเมล็ดกาแฟไทย เราคัดสรรเมล็ดพันธุ์คุณภาพจากเกษตรกรโดยตรง บรรยากาศร้านออกแบบมาให้นั่งทำงานและพักผ่อนได้อย่างสบายใจ"
    return render_template('page.html', title="About Us", content=text)

@app.route('/contact')
def contact(): 
    text = "เบอร์โทร: 081-234-5678 | อีเมล: hello@mycafe.com | Facebook: MyCafe TH | Line Official: @mycafe"
    return render_template('page.html', title="Contact", content=text)

@app.route('/location')
def location(): 
    text = "ร้านตั้งอยู่บริเวณหน้ามหาวิทยาลัยสงขลานครินทร์ (ม.อ.) วิทยาเขตหาดใหญ่ ใกล้กับ Lotus's เดินทางสะดวก มีที่จอดรถให้บริการฟรีสำหรับลูกค้า"
    return render_template('page.html', title="Location", content=text)

@app.route('/faq')
def faq(): 
    text = "Q: มีบริการ WiFi ฟรีไหม? A: มีบริการฟรีความเร็วสูง | Q: นำสัตว์เลี้ยงเข้ามาได้ไหม? A: ยินดีต้อนรับสัตว์เลี้ยง (Pet-friendly) | Q: มีปลั๊กไฟให้บริการไหม? A: มีปลั๊กไฟทุกโต๊ะ"
    return render_template('page.html', title="FAQ", content=text)

@app.route('/gallery')
def gallery(): 
    text = "ภาพบรรยากาศร้าน (กำลังอัปเดตระบบอัลบั้มภาพ) - ร้านมีโซน Indoor แอร์เย็นฉ่ำ และโซน Outdoor สำหรับรับลมธรรมชาติ พร้อมมุมถ่ายรูปสวยๆ สไตล์มินิมอล"
    return render_template('page.html', title="Gallery", content=text)

@app.route('/promotions')
def promotions(): 
    text = "โปรโมชั่นพิเศษเดือนนี้: 1. แสดงบัตรนักศึกษาลดทันที 10% ทุกเมนู | 2. ซื้อกาแฟ 2 แก้ว แถมฟรี คุกกี้ช็อกโกแลตชิป 1 ชิ้น | 3. สะสมแต้มครบ 10 แก้ว ฟรี 1 แก้ว"
    return render_template('page.html', title="Promotions", content=text)

@app.route('/events')
def events(): 
    text = "วันเสาร์และอาทิตย์นี้ พบกับดนตรีสดแนว Acoustic Pop ฟังเพลินๆ ตั้งแต่เวลา 18:00 - 20:00 น. และเตรียมพบกับเวิร์กชอปสอนดริปกาแฟพื้นฐานในปลายเดือน"
    return render_template('page.html', title="Events", content=text)

@app.route('/reviews')
def reviews(): 
    text = "⭐️⭐️⭐️⭐️⭐️ 'กาแฟอร่อยมาก บรรยากาศดี นั่งทำงานเพลินเลย' - คุณเอ | ⭐️⭐️⭐️⭐️ 'มัทฉะลาเต้เข้มข้น หอมมาก แนะนำเลย' - คุณบี | ⭐️⭐️⭐️⭐️⭐️ 'ชอบที่พาสุนัขมาได้ พนักงานบริการดี' - คุณซี"
    return render_template('page.html', title="Reviews", content=text)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

#123
#123