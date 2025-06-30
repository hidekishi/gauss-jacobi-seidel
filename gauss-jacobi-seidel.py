# Caso queira executar, é só modificar as matrizes A e b nas linhas 70 e 76 respectivamente.
# Após isso, executar "python gauss-jacobi-seidel.py"

def error_calc(next_guess, current_guess):
    max_diff = 0
    for i in range(len(next_guess)):
        diff = abs(next_guess[i] - current_guess[i])
        if diff > max_diff:
            max_diff = diff

    abs_next_guess = []
    for num in next_guess:
        abs_next_guess.append(abs(num))
    err = max_diff / max(abs_next_guess)
    return err

def gauss_jacobi(n_iter, initial_guess, A, b):
    print("Gauss-Jacobi: \n")
    def fx1(x1, x2, x3, x4):
        return (b[0]-A[0][1]*x2-A[0][2]*x3-A[0][3]*x4)/A[0][0]
    def fx2(x1, x2, x3, x4):
        return (b[1]-A[1][0]*x1-A[1][2]*x3-A[1][3]*x4)/A[1][1]
    def fx3(x1, x2, x3, x4):
        return (b[2]-A[2][0]*x1-A[2][1]*x2-A[2][3]*x4)/A[2][2]
    def fx4(x1, x2, x3, x4):
        return (b[3]-A[3][0]*x1-A[3][1]*x2-A[3][2]*x3)/A[3][3]
    
    current_guess = initial_guess
    print(f"Chute inicial:\nx1 = {current_guess[0]:.4f}\nx2 = {current_guess[1]:.4f}\nx3 = {current_guess[2]:.4f}\nx4 = {current_guess[3]:.4f}\n")
    for i in range(n_iter):
        x1 = fx1(current_guess[0], current_guess[1], current_guess[2], current_guess[3])
        x2 = fx2(current_guess[0], current_guess[1], current_guess[2], current_guess[3])
        x3 = fx3(current_guess[0], current_guess[1], current_guess[2], current_guess[3])
        x4 = fx4(current_guess[0], current_guess[1], current_guess[2], current_guess[3])
        next_guess = [x1, x2, x3, x4]

        err = error_calc(next_guess, current_guess)
        current_guess = next_guess
        print(f"{i+1}° iteração:")
        print(f"x1 = {current_guess[0]:.4f}\nx2 = {current_guess[1]:.4f}\nx3 = {current_guess[2]:.4f}\nx4 = {current_guess[3]:.4f}")
        print(f"Erro = {err:.4f}\n")
    return current_guess

def gauss_seidel(n_iter, initial_guess, A, b):
    print("Gauss-Seidel: \n")
    def fx1(x1, x2, x3, x4):
        return (b[0]-A[0][1]*x2-A[0][2]*x3-A[0][3]*x4)/A[0][0]
    def fx2(x1, x2, x3, x4):
        return (b[1]-A[1][0]*x1-A[1][2]*x3-A[1][3]*x4)/A[1][1]
    def fx3(x1, x2, x3, x4):
        return (b[2]-A[2][0]*x1-A[2][1]*x2-A[2][3]*x4)/A[2][2]
    def fx4(x1, x2, x3, x4):
        return (b[3]-A[3][0]*x1-A[3][1]*x2-A[3][2]*x3)/A[3][3]
    
    current_guess = initial_guess
    print(f"Chute inicial:\nx1 = {current_guess[0]:.4f}\nx2 = {current_guess[1]:.4f}\nx3 = {current_guess[2]:.4f}\nx4 = {current_guess[3]:.4f}\n")
    for i in range(n_iter):
        x1 = fx1(current_guess[0], current_guess[1], current_guess[2], current_guess[3])
        x2 = fx2(x1, current_guess[1], current_guess[2], current_guess[3])
        x3 = fx3(x1, x2, current_guess[2], current_guess[3])
        x4 = fx4(x1, x2, x3, current_guess[3])
        next_guess = [x1, x2, x3, x4]

        err = error_calc(next_guess, current_guess)
        current_guess = next_guess
        print(f"{i+1}° iteração:")
        print(f"x1 = {current_guess[0]:.4f}\nx2 = {current_guess[1]:.4f}\nx3 = {current_guess[2]:.4f}\nx4 = {current_guess[3]:.4f}")
        print(f"Erro = {err:.4f}\n")
    return current_guess

A = [[16, 4, 8, 4],
     [4, 10, 8, 4],
     [8, 8, 12, 10],
     [4, 4, 10, 12]
     ]

b = [32, 26, 38, 30]

initial_guess = [3, 3, 3, 3]

n_iter = int(input("Número de iterações: "))
method = int(input("Método(0 - Jacobi/ 1 - Seidel): "))

if method == 0:
    guess = gauss_jacobi(n_iter, initial_guess, A, b)
    print(f"A solução final após {n_iter} iterações foi:\nx1 = {guess[0]:.4f}\nx2 = {guess[1]:.4f}\nx3 = {guess[2]:.4f}\nx4 = {guess[3]:.4f}")
else:
    guess = gauss_seidel(n_iter, initial_guess, A, b)
    print(f"A solução final após {n_iter} iterações foi:\nx1 = {guess[0]:.4f}\nx2 = {guess[1]:.4f}\nx3 = {guess[2]:.4f}\nx4 = {guess[3]:.4f}")