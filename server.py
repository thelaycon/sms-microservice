import connexion
from flask import redirect

app = connexion.App(__name__, specification_dir='./')

# Read the swagger.yml file to configure the endpoints

app.add_api('openapi.yaml')

def home():
    return redirect("/v1/ui")

app.add_url_rule("/", 'home', home)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
