import sympy as sp

# Inicializa a impressão bonita
sp.init_printing()

# Função para formatar uma expressão em uma string legível
def format_expression(expr):
    return str(expr).replace("**", "^")

# Define a variável simbólica
x = sp.symbols("x")

print("--- ENTRADA ---")
# Solicita as expressões f(x) e g(x) ao usuário
expr_f = sp.sympify(input("Digite a expressão para f(x): "))
expr_g = sp.sympify(input("Digite a expressão para g(x): "))

# Calcula as composições das funções
gf = expr_g.subs(x, expr_f).expand()
ff = expr_f.subs(x, expr_f).expand()
gg = expr_g.subs(x, expr_g).expand()
fg = expr_f.subs(x, expr_g).expand()

print("--- RESULTADO ---")
# Exibe as expressões e suas composições
print("f(x) = ", format_expression(expr_f))
print("g(x) = ", format_expression(expr_g))
print("(g°f)(x) = ", format_expression(gf))
print("(f°f)(x) = ", format_expression(ff))
print("(g°g)(x) = ", format_expression(gg))
print("(f°g)(x) = ", format_expression(fg))

# Função para formatar um número em uma string legível
def format_float(number):
    if number == 0:
        return "0"
    else:
        return str(number).rstrip("0").rstrip(".")

# Função para calcular f(x) para um valor x fornecido
def calculate_fx(expr, value_x):
    return format_float(expr.subs({"x": value_x}).evalf(chop=True))

i = 1
while True:
    print(f"--- TESTE {i} ---")
    i += 1
    # Solicita um valor de x ao usuário
    value_x = float(input("Digite o valor de x: "))
    
    # Calcula e exibe as composições para o valor de x fornecido
    print(f"(g°f)({format_float(value_x)}) = {calculate_fx(gf, value_x)}")
    print(f"(f°f)({format_float(value_x)}) = {calculate_fx(ff, value_x)}")
    print(f"(g°g)({format_float(value_x)}) = {calculate_fx(gg, value_x)}")
    print(f"(f°g)({format_float(value_x)}) = {calculate_fx(fg, value_x)}")
