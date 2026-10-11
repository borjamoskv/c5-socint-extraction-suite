# c5-socint-extraction-suite

> **Omnivector Social Intelligence (SOCINT) & Forensic Extraction Engine in Pure Python Standard Library.**  
> *Zero external dependencies. 11 public platforms. Epistemic tiering. Astroturf & Sybil detection. SQLite WAL persistence.*

**Por Borja Fernández Angulo**  
*Investigador en Sistemas Complejos*

[![Python: 3.9+](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-0%20(Pure%20Stdlib)-orange.svg)](#zero-dependency-guarantee)
[![Tests: 35/35](https://img.shields.io/badge/Tests-35%2F35%20Deterministic-brightgreen.svg)](#silicon-certification--testing)

---

## 1. Visión General

`c5-socint-extraction-suite` es un motor soberano de extracción forense y análisis de telemetría discursiva diseñado para operar sin fricción técnica, sin necesidad de tokens de API de terceros y sin dependencias externas pesadas.

Diseñado bajo el principio de **alta exergía informativa**, procesa publicaciones, árboles jerárquicos de discusión, perfiles y métricas en 11 plataformas públicas de Internet, calculando simultáneamente la pureza epistemológica del texto analizado y la probabilidad matemática de astroturfing o ataques Sybil en los comentarios.

---

## 2. Los 11 Vectores Públicos Soportados

| # | Plataforma | Mecanismo de Ingestión | Capacidades Específicas |
| :---: | :--- | :--- | :--- |
| **01** | **X (Twitter)** | `api.fxtwitter.com` + Syndication Fallback | Hilos completos desenrollados (`--unfold`), métricas de engagement, perfiles de autor. |
| **02** | **Substack** | Archive REST API + HTML Reader | Artículos completos, árbol de comentarios y red de recomendaciones (PODs). |
| **03** | **Reddit** | JSON API + Auto-Fallback a Atom RSS | Bypass determinista de WAF 403, hilos anidados, índice de controversia y entropía de Shannon ($H_{\text{sub}}$). |
| **04** | **YouTube** | oEmbed API + Transcripción Pública | Metadatos de vídeo, miniaturas y extracción de subtítulos automáticos en texto plano. |
| **05** | **Hacker News** | Algolia REST API (`hn.algolia.com/api/v1`) | Árbol recursivo de comentarios y karma histórico de usuario vía Firebase v0. |
| **06** | **Bluesky (ATProto)** | Public AppView (`public.api.bsky.app`) | Hilos públicos, reposts, likes y perfiles desautenticados. |
| **07** | **Telegram** | Web Preview (`t.me/s/{channel}`) | Canales abiertos, vistas acumuladas y mensajes reenviados sin bot token. |
| **08** | **GitHub** | Atom Feed (`github.com/{user}.atom`) | Trazabilidad de actividad de desarrolladores, commits y lanzamientos públicos. |
| **09** | **Mastodon** | Fediverse Instance REST API | Toots, reblogs, réplicas y metadatos de instancias federadas abiertas. |
| **10** | **Prediction Markets** | Polymarket Gamma & Manifold REST | Probabilidades implícitas de consenso, volumen acumulado y liquidez de mercado. |
| **11** | **Wikipedia** | MediaWiki Revisions API (`w/api.php`) | Detección de guerras de edición, frecuencia de reversiones y concentración de editores. |

---

## 3. Motores Forenses y Epistémicos

### Clasificación Epistémica C5-REAL (4 Tiers)
El analizador descompone el texto y clasifica cada párrafo o segmento informativo en 4 niveles de solidez:
- **Tier 1 (Hechos Verificados):** Enlaces directos a fuentes primarias (DOIs, GitHub commits, repositorios oficiales, hashes on-chain).
- **Tier 2 (Evidencia Experimental):** Citas numéricas concretas, benchmarks, métricas reproducibles y telemetría.
- **Tier 3 (Modelos / Doctrina):** Marcos teóricos, analogías estructuradas, postulados y modelos explicativos.
- **Tier 4 (Especulación / Cheap Talk):** Retórica sin datos, adjetivación vacía, hypes y afirmaciones sin soporte empírico.

$$\text{SNR} = \frac{\text{Tier 1} + 0{,}75 \cdot \text{Tier 2}}{1 + 0{,}5 \cdot \text{Tier 3} + \text{Tier 4}}$$

### Detección de Astroturfing y Granjas Sybil
Evalúa la matriz de comentarios comparando la similitud léxica cruzada entre participantes mediante el índice de Jaccard sobre 3-gramas:

$$J(A, B) = \frac{|N_3(A) \cap N_3(B)|}{|N_3(A) \cup N_3(B)|}$$

$$\text{Riesgo} = \min(1{,}0, \; 0{,}35 \cdot C_{\text{autor}} + 1{,}30 \cdot R_{\text{duplicados}})$$

Detecta patrones donde cuentas con identificadores formalmente distintos copian y pegan el mismo mensaje o plantilla propagandística con pequeñas variaciones.

### TemporalForensics & Detección de Ráfagas Coordinadas (CIB)
Evalúa los intervalos entre comentarios ($\Delta t$) calculando el parámetro de Burstiness $B = \frac{\sigma - \mu}{\sigma + \mu} \in [-1, 1]$ y el factor de Fano ($F = \frac{\sigma^2}{\mu}$):
- **Inyección Periódica ($B \le -0.70$):** Detecta bots cronometrados y scripts de goteo deterministas.
- **Ráfagas Coordinadas ($B > 0.25$, $\ge 3$ comentarios en $\le 15$s):** Detecta ataques coordinados de bots o spam sincronizado.
- **Llegada Poissoniana:** Comportamiento estocástico orgánico de usuarios humanos.

### LexicalDispersion & Entropía Hapax Legomena
Mide la riqueza del vocabulario y la tasa de términos únicos (Hapax Legomena) frente a la masa total de tokens, discriminando texto sintético o plantillas prefabricadas de LLMs frente a la prosa humana espontánea.

### IdentityPivotEngine & Dossier Unificado OSINT
Genera objetivos de investigación unificada expandiendo cualquier handle hacia las plataformas soportadas (X, Bluesky, GitHub, Telegram, Reddit, Substack, YouTube, Hacker News, Mastodon) mediante `--pivot`.

### MerkleAttestation & Sello Criptográfico Anti-Manipulación
Calcula de forma determinista la raíz de Merkle SHA-256 (`merkle_root`) sobre todos los campos de evidencia indexados. Cualquier alteración posterior de un byte en el contenido o metadatos invalida la raíz, garantizando admisibilidad forense (`INV_C5_CANONICAL_ONTOLOGY` O1 y O8).

### SentimentAffectEngine & Volatilidad Emocional
Motor léxico puro de valencia y excitación emocional:
- **Polaridad Media:** Puntuación normalizada en $[-1.0, +1.0]$.
- **Volatilidad Emocional:** Desviación estándar de sentimiento entre comentarios.
- **Alerta de Indignación Polarizada (Manufactured Outrage):** Detecta campañas hostiles coordinadas con fuerte sesgo negativo y alta volatilidad.

### ActorNetwork & Extracción de Grafos de Entidad
Construye sobre la marcha el grafo de interacción social extrayendo menciones (`@usuario`, `u/autor`), dominios citados y relaciones de réplica/recomendación:
- **Gephi XML GEXF:** Formato nativo de grafos para análisis de centralidad y comunidades (`--export-gexf`).
- **Visualización Mermaid:** Exportación directa a diagramas compatibles con GitHub y editores Markdown (`--export-mermaid`).
- **Graphviz DOT:** Topologías de red exportables a formatos vectoriales para Graphviz (`--export-dot`).

### Bóveda Local SQLite WAL
Almacenamiento transaccional local (`~/.gemini/antigravity/socint_vault.db`) en modo WAL (Write-Ahead Logging), garantizando cero filtración de telemetría a infraestructuras en la nube.

---

## 4. Instalación y Uso

### Requisitos
- Python 3.9 o superior.
- **Cero dependencias externas:** utiliza exclusivamente la biblioteca estándar (`urllib`, `sqlite3`, `xml.etree.ElementTree`, `re`, `json`, `math`, `html`, `argparse`, `hashlib`).

### Instalación Rápida
```bash
git clone https://github.com/borjamoskv/c5-socint-extraction-suite.git
cd c5-socint-extraction-suite
pip install -e .
```

También puede ejecutarse directamente sin instalación:
```bash
./bin/socint --help
```

---

## 5. Ejemplos de Línea de Comandos

### Extracción de Hilo en X (Twitter) con Desenlace Completo
```bash
socint --url "https://x.com/borjamoskv/status/123456789" --unfold --save-vault
```

### Dossier de Identidad Cruzada (OSINT Pivot hacia 11 Plataformas)
```bash
socint --pivot "borjamoskv"
```

### Auditoría Forense Completa con Detección de Ráfagas (CIB) y Dispersión Léxica
```bash
socint --url "https://reddit.com/r/technology/comments/xyz123/title/" --burst-check --lexical-check
```

### Exportación a Gephi GEXF y Diagrama Mermaid
```bash
socint --url "https://news.ycombinator.com/item?id=40000000" --network --export-gexf red.gexf --export-mermaid red.mmd
```

### Generación de Dossier Forense Interactivo (Dashboard HTML Offline)
```bash
socint --url "https://reddit.com/r/technology/comments/xyz123/title/" --format html -o dossier.html
```

### Exportación Tabular para Datasets Forenses (CSV RFC 4180)
```bash
socint --batch urls.txt --format csv -o dataset.csv
```

### Consulta de Bóveda Local SQLite
```bash
# Ver estadísticas acumuladas
socint --stats

# Búsqueda semántica o por palabras clave en telemetría archivada
socint --vault-query "SELECT platform, author, extracted_at FROM socint_vault;"
```

---

## 6. Certificación en Silicio (Tests Deterministas)

El repositorio incluye una suite de pruebas unitarias 100% offline y reproducibles sin acceso a red:

```bash
make test
# O directamente:
python3 tests/test_socint.py
```

```text
=== SOCINT C5-REAL DETERMINISTIC TEST SUITE (35/35 OMNIVECTOR) ===
  [PASS] 01. X / Twitter URL Parsing (Tweets & Profiles)
  [PASS] 02. Substack URL Parsing (Posts & Publications)
  [PASS] 03. Reddit URL Parsing (Threads, Subreddits & Users)
  [PASS] 04. YouTube URL Parsing (Watch & youtu.be)
  [PASS] 05. Hacker News URL Parsing (Items & Users)
  [PASS] 06. Bluesky URL Parsing (Posts & Profiles)
  [PASS] 07. Telegram URL Parsing (Channels & Messages)
  [PASS] 08. GitHub URL Parsing (Repositories & Users)
  [PASS] 09. Mastodon / Fediverse URL Parsing
  [PASS] 10. Prediction Market URL Parsing (Polymarket & Manifold)
  [PASS] 11. Wikipedia URL Parsing (Language & Encoded Title)
  [PASS] 12. EpistemicClassifier (4 C5-REAL Tiers & SNR Calculation)
  [PASS] 13. AstroturfDetector (Jaccard N-Grams & Sybil Attack Detection)
  [PASS] 14. Shannon Entropy Calculation for Distributions
  [PASS] 15. Hacker News Data Normalization
  [PASS] 16. Bluesky ATProto Data Normalization
  [PASS] 17. Telegram Channel Data Normalization
  [PASS] 18. GitHub Feed & Commit Data Normalization
  [PASS] 19. Wikipedia Revision Forensics & Edit War Analysis
  [PASS] 20. SQLite Readonly Query CLI & Omnivector Markdown Report Rendering
  [PASS] 21. ActorNetwork Mentions, Links & Interactions Extraction
  [PASS] 22. ActorNetwork Mermaid Graph Serialization
  [PASS] 23. ActorNetwork Graphviz DOT Graph Serialization
  [PASS] 24. Standalone HTML Forensic Dashboard Generation (Zero CDN, Offline)
  [PASS] 25. Tabular CSV Export (RFC 4180 Escaping & Extraction)
  [PASS] 26. TemporalForensics Periodic Bot Drip / Scheduler Detection
  [PASS] 27. TemporalForensics Coordinated Burst Detection (CIB Bot Burst)
  [PASS] 28. LexicalDispersion & Hapax Legomena Richness (Anti-LLM Monotony)
  [PASS] 29. IdentityPivotEngine Cross-Platform Footprint Dossier Generation
  [PASS] 30. Full Omnivector Report Synthesis (Temporal + Lexical + Epistemic)
  [PASS] 31. Merkle Root Hash & Cryptographic Tree Computation (Tamper-Proof)
  [PASS] 32. ActorNetwork Gephi XML GEXF Graph Serialization
  [PASS] 33. SentimentAffectEngine Valence & Polarity Scoring (Zero Dependencies)
  [PASS] 34. SentimentAffectEngine Outrage & Emotional Volatility Detection
  [PASS] 35. Full Omnivector Attestation Report (Merkle + Sentiment + Topology)

[✓] ALL 35/35 OMNIVECTOR VERIFICATION CHECKS PASSED DETERMINISTICALLY.
```

---

## 7. Licencia

Distribuido bajo licencia **MIT**. Consulte el archivo [LICENSE](LICENSE) para más detalles.

---

**Firmado:**  
**Borja Fernández Angulo**  
*Investigador en Sistemas Complejos*
