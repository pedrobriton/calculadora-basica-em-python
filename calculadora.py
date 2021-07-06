from flask import Flask, render_template, request


#########################################
### LOGICA PARA CALCULADORA BASICA    ###
### OPERAÇÕES BÁSICAS                 ### 
### SOMAR                             ###
### SUBTRAIR                          ###
### MULTIPLICAR                       ###      
### DIVIDIR                           ###
#########################################
# develope by Pedro Brito               #
#########################################


# instanciando a variavel app que sera referencia ao flask
app = Flask(__name__)


# rotas
@app.route('/')
def main():
    return render_template('index.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':
            try:
                sum = float(num1) + float(num2)
                return render_template('index.html', sum=sum)
            except Exception:
                return "Ocorreu um erro, retorne para pagina inicial"

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            return render_template('index.html', sum=sum)

        elif operation == 'multiply':
                sum = float(num1) * float(num2)
                return render_template('index.html', sum=sum)
            
        elif operation == 'divide':
            sum = float(num1) / float(num2)
            return render_template('index.html', sum=sum)
        else:
            return render_template('index.html')

# falta implementar excessoes para tratar alguns possiveis erros, e melhorar 
# o front


# incia o app, no modo de debug
if __name__ == '__main__':
    app.debug = True
    app.run()

