from flask import Flask, render_template
import plotly.express as px
import pandas as pd
import json

app = Flask(__name__)

@app.route('/')
def index():
    
    #===> Scatter Plot<==#
    # Data untuk scatter plot
    scatter_data = pd.DataFrame({
        "X": [1, 2, 3, 4, 5],
        "Y": [10, 14, 23, 19, 25],
        "Category": ["A", "B", "A", "B", "A"]
    })
    
     # Membuat scatter plot dengan Plotly Express
    scatter_fig = px.scatter(
        scatter_data,
        x="X",
        y="Y",
        color="Category",
        title="Scatter Plot Example"
    )


    #===> Bar Chart<===#
    # Data untuk bar chart
    bar_data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Pineaple"],
        "Sales": [50, 75, 30, 60]
    })
    # Membuat bar chart dengan Plotly Express
    bar_fig = px.bar(
        bar_data,
        x="Fruits",
        y="Sales",
        title="Bar Chart Example",
        color="Fruits"
    )
    
    
    #===> Line Chart<===#
    # Data untuk line chart
    line_data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Pineaple"],
        "Sales": [50, 75, 30, 60]
    })
    line_fig =px.line(
        line_data,
        x="Fruits",
        y="Sales",
        title="Line Chart Example",
    )
    # Mengubah warna garis menjadi hijau
    line_fig.update_traces(line_color='green')
    
    
    #===> Pie Chart<===#
    # Data untuk Pie Chart
    pie_data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Pineaple"],
        "Sales": [50, 75, 30, 60]
    })
    
    pie_fig = px.pie(
        pie_data,
        values="Sales",
        names="Fruits",
        title="Pie Chart Example",
    )

    # ===> Histogram Chart <=== #
    his_data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Pineapple", "Apple", "Banana", "Cherry", "Pineapple"],
        "Sales": [50, 75, 30, 60, 55, 80, 25, 65]
    })
    # Membuat histogram
    his_fig = px.histogram(
        his_data,
        x="Fruits",  # Kolom data untuk sumbu X
        y="Sales",  # Kolom data untuk sumbu Y
        color="Fruits",
        title="Histogram Example",  # Judul histogram
        nbins=5,  # Jumlah bin (rentang)
        labels={"Sales": "Total Sales"}  # Label sumbu
    )
    
    # ===> Box Plot Chart <=== #
    box_data = pd.DataFrame({
        "Fruits": ["Apple", "Banana", "Cherry", "Pineapple", "Apple", "Banana", "Cherry", "Pineapple"],
        "Sales": [50, 75, 30, 60, 55, 80, 25, 65]
    })
    # Membuat box plot
    box_fig = px.box(
        box_data,
        x="Fruits",  # Kolom untuk kategori
        y="Sales",   # Kolom untuk nilai numerik
        title="Box Plot Example",  # Judul box plot
        color="Fruits",  # Kolom untuk memberikan warna berbeda
        labels={"Sales": "Total Sales"}  # Label sumbu
    )
    
    

    # Mengonversi figure Plotly menjadi JSON menggunakan metode `to_json()`
    scatter_json = scatter_fig.to_json()
    bar_json = bar_fig.to_json()
    line_json = line_fig.to_json()
    pie_json = pie_fig.to_json()
    his_json = his_fig.to_json()
    box_json = box_fig.to_json()
    
    
    
    # Kirim grafik ke template
    return render_template('index.html', scatter_plot=scatter_json, bar_chart=bar_json,
                           line_chart=line_json, pie_chart=pie_json, his_chart = his_json, box_chart=box_json)

if __name__ == '__main__':
    app.run(debug=True)
