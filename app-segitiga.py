from flask import Flask, render_template, request

aplikasi = Flask(__name__)

@aplikasi.route("/")
def app():
    return render_template("segitiga.html")

@aplikasi.route("/send", methods=["POST"])
def send(sum=sum):
    if request.method == "POST":
        segitiga = request.form["segitiga"]
        segitiga2= request.form["segitiga2"]
        sum = float(segitiga)
        sum2 = float(segitiga2)
        result = 0.5 * (sum * sum2)
        result2 = sum * 3
        return render_template("segitiga.html", sum=result, sum2=result2)
    else:
        return render_template("segitiga.html")

if __name__ == '__main__':
    aplikasi.run(debug=True)
