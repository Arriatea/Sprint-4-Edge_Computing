<h1 align="center">⚽ Sistema IoT de Detecção de Gols com Jogadoras</h1>
<h3 align="center">Projeto desenvolvido pela <strong>Nova Tech Global</strong></h3>

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-IoT-blue?style=for-the-badge&logo=arduino&logoColor=white">
  <img src="https://img.shields.io/badge/Wokwi-Simulation-green?style=for-the-badge&logo=wokwi&logoColor=white">
  <img src="https://img.shields.io/badge/MQTT-Comunicação-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Dashboard-Python-orange?style=for-the-badge&logo=python&logoColor=white">
</p>

---

##  Objetivo do Projeto

O objetivo deste projeto é **simular um sistema inteligente de monitoramento de gols** em partidas de futebol feminino, 
usando sensores e conectividade IoT.

O sistema **detecta automaticamente quando ocorre um gol**, mede a **velocidade do chute (em km/h)** e identifica a **jogadora responsável**, 
enviando os dados via **protocolo MQTT** para um **dashboard em Python (Dash + Plotly)**.

---

##  Componentes e Tecnologias Utilizadas

| Componente / Tecnologia | Função |
|--------------------------|--------|
|  **Arduino UNO** | Controla sensores e LEDs |
|  **Sensor Ultrassônico (HC-SR04)** | Mede a velocidade estimada da bola |
|  **Sensor Infravermelho (IR)** | Detecta a passagem da bola no gol |
|  **LEDs (verde e vermelho)** | Indicadores visuais de gol válido ou inválido |
|  **MQTT (via broker público)** | Transmissão dos dados dos gols para o dashboard |
|  **Python (Dash + Plotly)** | Dashboard em tempo real para monitoramento dos gols |
|  **Wokwi** | Simulação virtual do circuito Arduino |

---

##  Funcionamento do Sistema

1. O **sensor IR** detecta a passagem da bola pela linha do gol.  
2. O **sensor ultrassônico** mede a velocidade aproximada do chute.  
3. Caso o valor esteja dentro da faixa configurada → ⚽ **Gol confirmado!**  
4. O **LED verde** é aceso e o evento é publicado via **MQTT**.  
5. Se houver erro ou velocidade fora do padrão → 🚫 **Gol anulado**, e o **LED vermelho** é aceso.  
6. O **dashboard em Python** recebe os dados em tempo real e exibe:
   - Velocidade do chute no gol  
   - Jogadora responsável  
   - Histórico de eventos e média de velocidade  

---

<p align="center">
  <a href="https://youtu.be/lE0nkbuZJ8A?si=eVurd49faYQqqQc_" target="_blank">
    <img src="[https://upload.wikimedia.org/wikipedia/commons/b/b8/YouTube_Logo_2017.svg](https://youtu.be/eT5AYNRDoN8)" width="160">
  </a>
</p>


##  Código do Arduino

```cpp
#define trigPin 9
#define echoPin 10
#define sensorGol 2
#define ledVerde 3
#define ledVermelho 4

long duracao;
int distancia;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(sensorGol, INPUT);
  pinMode(ledVerde, OUTPUT);
  pinMode(ledVermelho, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // Simulação da leitura do sensor ultrassônico
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duracao = pulseIn(echoPin, HIGH);
  distancia = duracao * 0.034 / 2;

  int gol = digitalRead(sensorGol);

  if (gol == HIGH && distancia < 40) {
    Serial.println(" Gol confirmado!");
    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledVermelho, LOW);
  } else if (gol == HIGH && distancia >= 40) {
    Serial.println(" Gol anulado - velocidade fora do padrão.");
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, HIGH);
  } else {
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, LOW);
  }

  delay(1000);
}
## 👥 Integrantes do Grupo

| [<img loading="lazy" src="./imgs/Vitor.png" width=115><br><sub>Vitor Alcantara</sub>](https://github.com/VitorAlcantara-tech) | [<img loading="lazy" src="./imgs/Thiago.png" width=115><br><sub>Thiago Lima</sub>](https://github.com/thiagolima-tech) | [<img loading="lazy" src="./imgs/Matheus.png" width=115><br><sub>Matheus Vasques</sub>](https://github.com/maatvasques) | [<img loading="lazy" src="./imgs/Marco.png" width=115><br><sub>Marco Aurélio</sub>](https://github.com/Arriatea) | [<img loading="lazy" src="./imgs/Bernardo.png" width=115><br><sub>Bernardo Hanashiro</sub>](https://github.com/BernardoYuji) |
| :---: | :---: | :---: | :---: | :---: |


