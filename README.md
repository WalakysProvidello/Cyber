# CyberSecurity | Sistema de monitoramento de segurança


# Sistema de Monitoramento de Segurança - Detecção de Invasões
**Descrição do Problema:**
Você foi encarregado de implementar um sistema de monitoramento para um sistema de acesso. Esse sistema deve analisar registros de log de tentativas de acesso e identificar possíveis invasões com base nas falhas consecutivas. Cada registro de log contém o identificador de um usuário e o status da tentativa de acesso.

**Objetivo:**
Detecção de Invasão: O sistema deve emitir um alerta quando um usuário tiver mais de 3 tentativas consecutivas de falha de acesso.

**Entrada:**
A entrada consiste em uma lista de registros de log no formato id_usuario:status, onde:
id_usuario é o identificador do usuário.

**status pode ser:**
"sucesso" – A tentativa de acesso foi bem-sucedida.
"falha" – A tentativa de acesso falhou.
A lista de registros pode ter qualquer número de entradas.

**Saída:**
O sistema deve retornar o id_usuario que teve mais de 3 tentativas consecutivas de falha.
Se nenhum usuário tiver mais de 3 tentativas de falha consecutivas, o sistema deve retornar a mensagem: "Nenhum invasor detectado".

![image](https://github.com/user-attachments/assets/120473fd-dd4d-43d0-ac1d-ac1b87d94aa5)
![image](https://github.com/user-attachments/assets/2768790e-d665-4e87-ae86-498121f319b4)

