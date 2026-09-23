"""
O problema 1.1 do livro Cracking the Coding Interview ( Gayle Laakmann McDowell) chama-se "Is Unique" (ou "É Único").

Enunciado do Problema
Implemente um algoritmo para determinar se uma string possui apenas caracteres únicos (sem repetições).
Desafio extra: E se você não puder usar estruturas de dados adicionais?

Perguntas e Premissas Importantes (O que esclarecer em uma entrevista)
Antes de sair escrevendo código, o primeiro passo em uma entrevista é definir o escopo:

- A string é em ASCII ou Unicode?

- Se for ASCII padrão (128 caracteres) ou ASCII estendido (256 caracteres), o tamanho do alfabeto é fixo. Se a string tiver mais caracteres do que o tamanho do alfabeto, pela Lei dos Pombos (Pigeonhole Principle), ela precisa ter caracteres repetidos.

- Caixa alta/baixa diferem?

- 'A' e 'a' são considerados o mesmo caractere ou diferentes? O padrão é considerá-los diferentes (código ASCII distinto).

Solução: Utilizando uma Estrutura de Dados (Vetor Booleano / Hash Set) Se assumirmos que a string é ASCII (128 caracteres):

Ideia: Criamos um array booleano de tamanho 128 onde a posição i indica se o caractere com valor ASCII i já foi encontrado.
Complexidade de Tempo: O(n) ou O(1), já que a busca termina no máximo em 128 iterações.
Complexidade de Espaço: O(1) (pois o tamanho do array é constante: 128 posições).

"""

class Solution:
    def is_unique_bitmask(self, s: str) -> bool:
        checker = 0
        for char in s:
            val = ord(char) - ord('a')
            # Verifica se o bit na posição `val` já está ativado
            if (checker & (1 << val)) > 0:
                return False
            # Ativa o bit na posição `val`
            checker |= (1 << val)
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.is_unique_bitmask("abc"))