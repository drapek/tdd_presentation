from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    home_html = """
    <html>
    <h1>Witryna fakturowania</h1> 
    <h2> Mega ważne faktury do opłacenia dziś bo inaczej komornik </h2>
    <p><a href='/invoices'>link</a></p>
    
    </html>
    """
    return home_html


@app.route('/invoices/')
def invoices():
    from example_crashed_py_file.invoices import InvoicesRepo
    invoices = InvoicesRepo().get_with_term_today()
    invoices_links = [f'<a href="/{i}"> {i} </a>' for i in invoices]
    return f'faktury: {invoices_links}'


if __name__ == '__main__':
    app.run()
