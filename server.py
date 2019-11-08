from flask import Flask, render_template
import watson

app = Flask(__name__)
model = "aaa"

@app.route('/train')
def train():
    api = watson.getAPI()
    #result = watson.ls(api)
    #result = watson.rm(api, result["classifiers"][0]["classifier_id"])
    zip_path = "./img/myself.zip"
    return watson.make(api,zip_path)

@app.route('/isReady')
def isReady():
    api = watson.getAPI()
    result = watson.ls(api)
    print(result)
    if "ready" == result["classifiers"][0]["status"]:
        return "true"
    return "false"

@app.route('/judge')
def judge():
    api = watson.getAPI()
    result = watson.ls(api)
    url = "https://loccio.com/line/bear/userimg/kuma.jpg"
    result = watson.judge(api, result["classifiers"][0]["classifier_id"],url)
    bear = 0
    human = 0 
    for i in result["images"][0]["classifiers"][0]["classes"]:
        if "bear" == i["class"]:
            bear = i["score"]
        if "myself" == i["class"]:
            human = i["score"]
    return "人間率"+str(human)+"%  熊率"+str(bear)+"%"

if __name__ == "__main__":
    app.run(debug=True,port=5500)

