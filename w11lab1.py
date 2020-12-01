from flask import Flask, request, jsonify

app = Flask(__name__)

d = {}

@app.route('/', methods=['GET'])
def get_dsstudents():
    return jsonify(d)

@app.route('/', methods=['POST'])
def create_record():
    ds_students = {}
    for k,v in request.args.items():
        if not k in d.keys():
            dsstudents[k] = v
            d[k] = v
    return jsonify({"ds_students": dsstudents, "current": d})

@app.route('/', methods=['DELETE'])
def delete_record():
    deletedstudents = {}
    for k,v in request.args.items():
        try:
            d.pop(k)
            deletedstudents[k] = v
        except:
            continue
    return jsonify({"deletedstudents": deletedstudents, "current": d})
                
if __name__ == '__main__':
    app.run(debug=True)