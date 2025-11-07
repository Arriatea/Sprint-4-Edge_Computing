<h1 align="center">⚽ Sistema IoT de Detecção de Gols com Arduino</h1>
<h3 align="center">Projeto desenvolvido pela <strong>Nova Tech Global</strong></h3>

<p align="center">
  <img src="https://img.shields.io/badge/Arduino-IoT-blue?style=for-the-badge&logo=arduino&logoColor=white">
  <img src="https://img.shields.io/badge/Wokwi-Simulation-green?style=for-the-badge&logo=wokwi&logoColor=white">
  <img src="https://img.shields.io/badge/MQTT-Comunicação-purple?style=for-the-badge">
  <img src="https://img.shields.io/badge/Dashboard-Visualização-orange?style=for-the-badge">
</p>

---

## 📌 Objetivo do Projeto

Este projeto tem como objetivo **simular um sistema inteligente de monitoramento de gols** em partidas de futebol,
usando sensores e conectividade IoT.

A ideia é **detectar automaticamente o gol**, registrar a **velocidade do chute** e identificar a **jogadora** responsável — 
tudo processado via **Arduino**, com simulação no **Wokwi**.

---

## ⚙️ Componentes e Tecnologias

| Componente | Função |
|-------------|--------|
| 🟩 **Arduino UNO** | Unidade principal de controle |
| 🟧 **Sensor Ultrassônico (HC-SR04)** | Mede a velocidade do chute simulada |
| 🟥 **Sensor Infravermelho (IR)** | Detecta passagem da bola no gol |
| 🟦 **LEDs** | Indicadores visuais de gol (verde) e erro (vermelho) |
| 🟪 **MQTT (Simulado)** | Comunicação entre o dispositivo e o dashboard |
| 🟨 **Dashboard Node-RED (fictício)** | Exibição de dados em tempo real (velocidade, jogadora, replay) |

---

## 🧠 Como Funciona

1. A bola (simulada) é detectada pelo sensor IR.  
2. O sensor ultrassônico mede a velocidade estimada.  
3. Se o valor estiver dentro do intervalo configurado → ⚽ **Gol confirmado!**  
4. O LED verde acende e uma mensagem é enviada via MQTT (simulação).  
5. O LED vermelho acende se houver erro na leitura ou falso positivo.

---

## 💻 Código Base (Arduino)

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
  // Simulação do chute
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duracao = pulseIn(echoPin, HIGH);
  distancia = duracao * 0.034 / 2;

  int gol = digitalRead(sensorGol);

  if (gol == HIGH && distancia < 40) {
    Serial.println("⚽ Gol confirmado!");
    digitalWrite(ledVerde, HIGH);
    digitalWrite(ledVermelho, LOW);
  } else if (gol == HIGH && distancia >= 40) {
    Serial.println("❌ Gol anulado - velocidade fora do padrão.");
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, HIGH);
  } else {
    digitalWrite(ledVerde, LOW);
    digitalWrite(ledVermelho, LOW);
  }

  delay(1000);
}
