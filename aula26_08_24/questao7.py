def questao7(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    print(f"Fibonacci: {fibonacci[:n]}")
