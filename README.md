# Category-Aware News Sentiment & Opposition Opinion Generator

## Project Overview

**Category-Aware News Sentiment & Opposition Opinion Generator** is a full-stack AI application that analyzes news articles to extract category (Politics/Sports), sentiment, and generates a respectful opposing viewpoint. Built with Flask (backend) and vanilla JavaScript (frontend), it aims to foster balanced perspectives and critical thinking.

### Key Features
- **Category Detection**: Classifies news as Politics or Sports
- **Sentiment Analysis**: Determines if the article is positive, negative, or neutral
- **Opposition Generation**: Creates a respectful, balanced opposing opinion
- **User-Friendly Interface**: Simple, clean web UI for news input and results display
- **Clean Architecture**: Separation of concerns (API layer, services, gateways)

---

## Architecture

### Project Structure
```
category-aware-news-opposition/
├── backend/
│   ├── app.py                    # Flask app factory
│   ├── config.py                 # Configuration
│   ├── requirements.txt           # Python dependencies
│   ├── __init__.py               # Package initializer
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py             # Health check endpoint
│   │   └── analyze.py            # /analyze POST endpoint
│   ├── services/
│   │   ├── __init__.py
│   │   ├── category_service.py   # Category detection logic
│   │   ├── sentiment_service.py  # VADER sentiment analysis
│   │   └── opposition_service.py # Opposition opinion generation
│   ├── gateways/
│   │   └── __init__.py           # Adapter layer placeholder
│   ├── models/                    # (future ML models)
│   ├── tests/
│   │   ├── test_health.py        # Health endpoint tests
│   │   └── test_integration_analyze.py  # Integration tests
│   ├── scripts/
│   │   ├── print_routes.py       # Debug helper
│   │   └── import_analyze.py     # Dependency checker
│   └── .venv/                     # Virtual environment
│
└── frontend/
    ├── index.html                # UI markup
    ├── style.css                 # Clean, minimal styling
    └── script.js                 # Frontend logic (fetch, render)
```

### Architecture Principles
- **Clean Layers**: HTTP API → Services → Business Logic
- **Testability**: Services are pure functions; easy to unit test
- **Modularity**: Each service has a single responsibility
- **Extensibility**: New services (e.g., ML models) fit naturally into the gateway layer

---

## AI Usage Explanation

### 1. **Sentiment Analysis (VADER)**
- **Service**: `backend/services/sentiment_service.py`
- **AI Library**: `vaderSentiment` (rule-based lexicon)
- **What it does**: Scores text on a scale from -1 (most negative) to +1 (most positive)
- **Output**: Label (positive/negative/neutral) + numerical score
- **Use case**: Determines the emotional tone of the article

### 2. **Category Detection**
- **Service**: `backend/services/category_service.py`
- **Method**: Rule-based keyword matching (currently)
- **Keywords**: 
  - Politics: "election", "government", "senate", "policy", "parliament", etc.
  - Sports: "game", "match", "score", "team", "coach", "tournament", etc.
- **Output**: Category (Politics or Sports)
- **Future**: Can be replaced with a trained ML classifier (Phase 5+)

### 3. **Opposition Opinion Generation**
- **Service**: `backend/services/opposition_service.py`
- **Method**: Template-based reasoning
- **Logic**: 
  - If positive sentiment → suggest potential downsides
  - If negative sentiment → highlight potential upsides
  - If neutral → present balanced view
- **Output**: Respectful opposing perspective + ethical disclaimer

**Why this matters**: These AI components help users see multiple viewpoints, reducing echo chambers and promoting critical thinking.

---

## API Details

### Health Endpoint
```
GET /
```
**Response (200 OK)**:
```
Backend running
```

### Analyze Endpoint
```
POST /analyze
Content-Type: application/json
```

**Request Body**:
```json
{
  "text": "The government announced a new policy after the election campaign."
}
```

**Response (200 OK)**:
```json
{
  "category": "Politics",
  "sentiment": {
    "label": "positive",
    "score": 0.456
  },
  "opposition_view": "An alternative, respectful perspective: Policy-focused alternative: Although this piece emphasizes concerns, an alternative view is that some measures cited could lead to beneficial outcomes...",
  "disclaimer": "This is an AI-generated alternative perspective intended to broaden understanding. It is not endorsement of any position."
}
```

**Error Response (400 Bad Request)**:
```json
{
  "error": "Text must be at least 10 characters."
}
```

**Validation Rules**:
- Text must be non-empty and between 10 and 5000 characters
- Missing or invalid JSON returns 400
- Server errors return 500 with generic message

---

## Limitations

1. **Rule-Based Category Detection**: Currently uses keyword matching. Limited accuracy for nuanced topics.
   - *Fix*: Train a classifier (Naive Bayes, SVM, or transformer-based) on labeled news dataset

2. **VADER Sentiment**: Lexicon-based; may miss context, sarcasm, domain-specific slang.
   - *Fix*: Integrate a pre-trained transformer model (e.g., DistilBERT, RoBERTa)

3. **Opposition Generation**: Template-based; lacks true reasoning.
   - *Fix*: Implement LLM-based reasoning (GPT, LLaMA) with ethical guardrails

4. **Small Sample Size**: No multi-language support; tested only on English.

5. **No Persistent Storage**: Responses are stateless; no database for history or analytics.

6. **UI Simplicity**: Minimal frontend; no advanced visualizations or chart support.

---

## Ethical Disclaimer

### Important Notice
This tool generates AI-powered alternative perspectives and is **not** intended to:
- Promote misinformation or bias
- Replace human judgment or editorial review
- Endorse any political, social, or ideological position
- Be used for generating misleading or deceptive content

### Intended Use
- **Educational**: Help users understand diverse viewpoints
- **Critical Thinking**: Encourage questioning and analysis
- **Awareness**: Highlight potential blind spots and assumptions

### Responsibility
Users are responsible for:
- Verifying facts from reputable sources
- Applying their own judgment
- Not using output for misleading or harmful purposes

**The developers of this tool do not endorse, approve, or take responsibility for the use of generated opinions in real-world decisions.**

---

## Getting Started

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. **Clone or navigate to the project directory**:
   ```bash
   cd category-aware-news-opposition
   ```

2. **Create and activate a virtual environment**:
   ```bash
   cd backend
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # or: source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application

#### Backend (Flask Server)
```bash
cd backend
.venv\Scripts\python.exe -c "from backend import create_app; app=create_app(); app.run(host='127.0.0.1', port=5000)"
```
The server will start on `http://127.0.0.1:5000`

#### Frontend
Open `frontend/index.html` in your browser (or serve via a simple HTTP server):
```bash
# Python 3
cd frontend
python -m http.server 8000
# Then visit http://localhost:8000/index.html
```

---

## Testing

### Run Backend Tests
```bash
cd backend
.venv\Scripts\python.exe -m pytest -q
```

**Test Files**:
- `tests/test_health.py`: Health endpoint
- `tests/test_integration_analyze.py`: /analyze endpoint

### Sample Test Headlines

Use these headlines to test the application:

1. **Politics (Positive)**:
   > "The government announced a new policy after the election campaign aimed at improving healthcare for all citizens."
   - Expected: Category=Politics, Sentiment=positive

2. **Sports (Positive)**:
   > "The team won the championship match convincingly and the coach praised their exceptional effort."
   - Expected: Category=Sports, Sentiment=positive

3. **Politics (Negative)**:
   > "The government faces criticism over its controversial policy that many groups oppose."
   - Expected: Category=Politics, Sentiment=negative

4. **Sports (Neutral)**:
   > "The match ended with a score of 2-1. Both teams competed fairly."
   - Expected: Category=Sports, Sentiment=neutral

---

## Future Enhancements (Phase 5+)

- [ ] **ML-Based Category & Sentiment**: Replace rule-based detection with trained classifiers
- [ ] **LLM Integration**: Use GPT/LLaMA for richer opposition generation
- [ ] **Database & History**: Store analyses for user tracking and analytics
- [ ] **Multi-Language Support**: Extend beyond English
- [ ] **Advanced UI**: Charts, export to PDF, sharing features
- [ ] **Authentication**: User accounts and preferences
- [ ] **Fact Checking**: Integration with fact-check APIs
- [ ] **Bias Detection**: Identify and flag potential biases in source material

---

## License

This project is provided as-is for educational and research purposes. See LICENSE file for details.

---

## Contact & Support

For questions, issues, or contributions:
- Open an issue on GitHub
- Contact the development team

---

**Version**: 1.0.0 (Phase 4 — Hardened & Documented)  
**Last Updated**: December 18, 2025
