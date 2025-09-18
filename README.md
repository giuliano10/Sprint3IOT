Problema
Um dos grandes desafios em sistemas digitais é a segurança e a identificação de usuários.  
Muitas vezes, senhas ou cartões de acesso podem ser esquecidos, perdidos ou até mesmo clonados, o que gera riscos de invasão e acesso não autorizado.  
Esse problema é ainda mais crítico em bancos e empresas, onde a proteção de dados e do espaço físico é essencial.


Solução
Para resolver esse problema, desenvolvemos um aplicativo com reconhecimento facial.  

Este sistema permite:
- Cadastrar o rosto do usuário.  
- Validar a identidade em tempo real.  
- Liberar acesso apenas para pessoas autorizadas, garantindo mais segurança que métodos tradicionais.  

Além disso, a solução é prática:  
O usuário não precisa lembrar de senhas nem carregar cartões.  
O próprio rosto é a chave de acesso.  


Objetivo
Implementar um sistema de reconhecimento facial em tempo real, com cadastro de usuários e exibição de landmarks faciais (olhos, nariz, boca e contorno do rosto).  
Esse sistema pode ser facilmente integrado a dispositivos IoT, como fechaduras eletrônicas, sistemas de monitoramento e automação residencial/empresarial.

Execução

1. Clone ou baixe este repositório.  
2. Instalar as dependências  
   Certifique-se de ter o Python 3.9+ instalado.  
   Em seguida, instale as bibliotecas necessárias:
   ```bash
   pip install opencv-python dlib numpy
3. Baixe os modelos necessários e coloque-os na pasta do projeto:  
   - [`shape_predictor_68_face_landmarks.dat`](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)  
   - [`dlib_face_recognition_resnet_model_v1.dat`](http://dlib.net/files/dlib_face_recognition_resnet_model_v1.dat.bz2)


Controles
- `E` Cadastrar novo usuário (somente uma face deve estar visível).  
- `V` Ativar/Desativar validação em tempo real.  
- `Q` Encerrar o programa.  

Dependências

- Python 3.9+  
- OpenCV  
- dlib
- numpy  

Instale com:
```bash
pip install opencv-python dlib numpy
```

Parâmetros

- `PREDICTOR`: caminho para `shape_predictor_68_face_landmarks.dat`  
- `RECOG`: caminho para `dlib_face_recognition_resnet_model_v1.dat`  
- `DB_FILE`: arquivo local que armazena embeddings faciais (`db.pkl`)  
- `THRESH`: limiar de distância para aceitação/rejeição (padrão: `0.6`)  
