# Peer-to-Peer Blockchain Simulation

A simple peer-to-peer blockchain simulation with a Flask backend and interactive HTML/CSS frontend.

## Features
- Transaction creation
- Proof-of-Work mining
- Multiple nodes with consensus
- Real-time blockchain display in browser
- Chain conflict resolution
- REST API

## How to Run

1. Create virtual environment:
python -m venv venv
source venv/bin/activate (Linux/macOS) OR venv\Scripts\activate (Windows)

markdown
Copy
Edit

2. Install dependencies:
pip install -r requirements.txt

csharp
Copy
Edit

3. Start nodes on different terminals:
python run.py 5000
python run.py 5001

markdown
Copy
Edit

4. Visit dashboard:
http://127.0.0.1:5000/

markdown
Copy
Edit

## API Endpoints

- `/mine` → mine a block
- `/transactions/new` → POST a transaction
- `/chain` → get full chain
- `/nodes/register` → connect to peers
- `/nodes/resolve` → run consensus algorithm