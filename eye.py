# Função para detectar tentativas de invasão em registros de log
def detectar_invasao(registros):
    # Variáveis para rastrear o ID do usuário atual e suas falhas consecutivas
    usuario_atual = None
    tentativas_consecutivas = 0
    invasor_detectado = None

    # Percorre cada registro de log
    for registro in registros:
        # Separa o ID do usuário e o status do registro (sucesso ou falha)
        id_usuario, status = registro.split(":")
        
        # Se o usuário atual for o mesmo do anterior
        if id_usuario == usuario_atual:
            if status == "falha":
                # Se a tentativa foi "falha", incrementa o contador de falhas
                tentativas_consecutivas += 1
                # Se as falhas consecutivas ultrapassarem 3, marca o invasor
                if tentativas_consecutivas > 3:
                    invasor_detectado = id_usuario
                    break
            else:
                # Se for "sucesso", reseta o contador de falhas
                tentativas_consecutivas = 0
        else:
            # Se mudar de usuário, verifica se o usuário anterior teve mais de 3 falhas consecutivas
            if tentativas_consecutivas > 3:
                invasor_detectado = usuario_atual
                break
            # Atualiza para o novo usuário e reinicia a contagem de falhas
            usuario_atual = id_usuario
            tentativas_consecutivas = 1 if status == "falha" else 0
    
    # Após o loop, verifica se o último usuário teve mais de 3 tentativas de falha consecutivas
    if tentativas_consecutivas > 3:
        invasor_detectado = usuario_atual

    # Retorna o resultado final
    return invasor_detectado if invasor_detectado else "Nenhum invasor detectado"

# Função principal para executar o programa
def main():
    # Solicita ao usuário que insira os registros de log
    entrada = input()
    
    # Converte a entrada em uma lista de registros
    registros = [registro.strip().strip('"') for registro in entrada.split(",")]

    # Chama a função para detectar tentativas de invasão
    resultado = detectar_invasao(registros)

    # Imprime o resultado
    print(resultado)

# Chama a função principal para executar o programa
if __name__ == "__main__":
    main()
