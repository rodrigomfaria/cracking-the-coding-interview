"""
O problema 1.2 (o segundo problema do capítulo de Arrays and Strings) do Cracking the Coding Interview chama-se "Check Permutation" (ou "Verificar Permutação").

Enunciado do Problema
Dadas duas strings, escreva um método para decidir se uma é uma permutação da outra.

(Uma permutação significa que ambas as strings possuem exatamente os mesmos caracteres, nas mesmas quantidades, mas em ordens potencialmente diferentes. Exemplo: "god" e "dog" são permutações; "hello" e "llheo" também).

Perguntas e Premissas Importantes

- Diferencia maiúsculas de minúsculas (case-sensitive)?

R: Por padrão, sim. Exemplo: "God" e "dog" não seriam permutações.

- Espaços são significativos?

R: Por padrão, sim. Exemplo: "dog " (com espaço no fim) não é permutação de "dog".

Qual é o tamanho das duas strings?

R: Se as duas strings tiverem tamanhos diferentes (len(s1) != len(s2)), elas jamais poderão ser permutações. Podemos retornar False imediatamente.

Solução: Contagem de Frequências
Se duas strings forem permutações uma da outra, elas devem conter exatamente os mesmos caracteres na mesma quantidade.
Ideia: Contar a frequência de cada caractere em uma string e descontar os valores ao percorrer a outra.
Complexidade de Tempo: O(n), onde n é o comprimento da string.
Complexidade de Espaço: O(1) para alfabetos fixos, como ASCII, ou O(k) para um alfabeto de tamanho k.

"""

class Solution:
    def check_permutation_count(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        
        # Assumindo tabela ASCII (128 caracteres)
        letters = [0] * 128
        
        # Conta a frequência dos caracteres de s1
        for char in s1:
            letters[ord(char)] += 1
            
        # Desconta a frequência usando s2
        for char in s2:
            val = ord(char)
            letters[val] -= 1
            # Se a contagem ficar negativa, s2 tem mais desse caractere do que s1
            if letters[val] < 0:
                return False
                
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.check_permutation_count("abc", "bce"))