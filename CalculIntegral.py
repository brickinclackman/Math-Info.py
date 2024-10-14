import math

def safe_eval(expression_litteral,x_val):
    """Fonction qui permet de sécurité la fonction 'éval' en limitant son utilisation et 
    en remplaçant la chaine de caractère complète par une expression utilisable, équivaut au 'f(x)'

    Args:
        expression_litteral (string): tout est dit dans son nom, c'est une expression littérale, une fonction mathématique,...
        x_val (int): le calcul qui va être fait dans l'expression lit

    Returns:
        any: retourne le résultat de la fonction
    """
    allowed_function = {
        'sin': math.sin,
        'cos': math.cos,
        'sqrt': math.sqrt,
        'log': math.log,
        'exp': math.exp,
        'pow': pow,
        'abs': abs
    } #Creation d'un dictionnaire
    local_dict = {'x' : x_val} #Petit dictionnaire
    local_dict.update(allowed_function) #Mis à jour du dictionnaire en y insérant les fonctions mathématiques

    return eval(expression_litteral,{"__builtins__":None},local_dict)

user_input = input("Veuillez saisir une expression en fonction de x (par exemple, (x**2 + 1)) : ")

def integrale_generale(a,b,n):
    """Cette fonction calcul l'intégrale pour tout type de fonction

    Args:
        a (int): valeur de début
        b (int): valeur de fin
        n (int): nombre de cas

    Returns:
        float: S et T deux valeurs qui seront deux encadrements
    """
    dx = (b - a) / n
    S = sum(safe_eval(user_input,a + i * dx) * dx for i in range(n))
    T = sum(safe_eval(user_input,a + (i + 1) *dx) * dx for i  in range(n))
    return S, T

a_input = int(input("Veuillez entre la valeur a : "))
b_input = int(input("Veuillez entre la valeur b : "))
n_input = int(input("Veuillez entre la valeur n : "))

Valeur1, Valeur2 = integrale_generale(a_input,b_input,n_input)

print("Encadrement de l'expression \"",user_input,"\" de ",a_input," à ",b_input,"pour ",n_input,"valeurs vaut :\n",Valeur1,"< x <",Valeur1)

print("Aire :",Valeur2-Valeur1)

