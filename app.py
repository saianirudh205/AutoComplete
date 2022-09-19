from flask import Flask, request, render_template

from Trie import Trie
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():  
    return render_template("index.html", data=Trie().load())

@app.route('/add_loc',methods=['POST'])
def add_loc():
   
    if request.method == 'POST':
        a=request.form['city']
        return render_template('index.html',data=Trie().insert(a))
    
    return render_template('input.html',data='SOMETHING WENT WORNG')



@app.route('/delete',methods=['POST'])
def delete():
   
    if request.method == 'POST':
        a=request.form['city']
        return render_template('index.html',data=Trie().delete(a))
    
    return render_template('input.html',data='SOMETHING WENT WORNG')



if __name__ == '__main__':
 app.run(debug=True)
