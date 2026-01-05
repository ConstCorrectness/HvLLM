# HvLLM
HvLLM


/HvLLM-Project
├── /docs                    # Architecture diagrams, rubrics for social scoring
├── /backend                 # The Central Orchestrator
│   ├── /api                 # Endpoints for Frontend and Agents
│   ├── /core                # User auth, Matchmaking, Database connections
│   ├── /engine              # The loop that runs the tests
│   └── /environments        # THE HEART OF THE PROJECT
│       ├── /base_env.py     # Defines the standard class
│       ├── /logic           # IQ tests, Pattern Rec
│       ├── /social          # Chat scenarios, negotiation prompts
│       └── /games           # Chess, Go, Custom 3D logic
│
├── /frontend                # Human User Interface
│   ├── /components          # React/Vue components
│   ├── /rendering           # Canvas/WebGL code for 3D tests
│   └── /views               # Dashboard, Leaderboards
│
├── /agents                  # The "AI Player" wrappers
│   ├── /local_llm           # Scripts to run Llama/Mistral locally
│   ├── /api_wrappers        # Connectors for GPT/Claude APIs
│   └── /baselines           # Simple bots (random, heuristic) for control groups
│
└── /analysis                # Post-processing
    ├── /metrics             # Scripts to calculate speed/accuracy/ELO
    └── /visualization       # Jupyter notebooks or scripts to generate charts



/HvLLM
├── /frontend (React + Vite + TS)
│   ├── /src
│   │   ├── /components    # GameBoard, ChatBox, ScoreCard
│   │   ├── /hooks         # useWebSocket (for live game state)
│   │   └── /types         # Shared TypeScript interfaces
│   ├── vite.config.ts
│   └── package.json
│
├── /backend (Python FastAPI)
│   ├── /app
│   │   ├── /api           # Endpoints (POST /match/start)
│   │   ├── /core          # Config, DB connection
│   │   ├── /agents        # The AI wrappers (OpenAI, Local Llama)
│   │   ├── /engines       # The Logic: ChessEngine, SocialEngine
│   │   └── /schemas       # Pydantic models (Input validation)
│   ├── main.py
│   └── requirements.txt
│
├── /infra
│   ├── docker-compose.yml # Spins up Postgres(Timescale) + Redis
│   └── /db_scripts        # SQL init scripts