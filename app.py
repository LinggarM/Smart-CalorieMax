from flask import Flask, request, render_template
import knapsack

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        number_of_item = request.form['number_of_item']
        nama_makanan = request.form['nama_makanan']
        value_makanan = request.form['value_makanan']
        harga_makanan = request.form['harga_makanan']
        uang = request.form['uang']
        return render_template(
            'index.html', 
            data= knapsack.kalkulasi(
                number_of_item,
                nama_makanan, 
                value_makanan, 
                harga_makanan, 
                uang
            )
        )
    return render_template(
        "index.html", 
        data=""
    )

if __name__ == "__main__":
    app.run()