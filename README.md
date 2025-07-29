## 🧱 Blockchain Simulation

A **minimalistic blockchain network** with Flask-based REST API, interactive HTML dashboard, and multi-node consensus. This project demonstrates the core principles of blockchain such as proof of work, decentralization, mining, and resolving conflicts — without any external blockchain libraries.

---

### 📁 Project Structure

```
blockchain_simulation/
├── blockchain.py         # Core Blockchain class and logic
├── app.py                # Flask app defining API endpoints
├── run.py                # Launch node on specified port
├── templates/
│   └── index.html        # Interactive frontend dashboard
├── static/
│   └── style.css         # Basic UI styling
├── requirements.txt      # Python dependencies
├── README.md             # Project documentation
└── venv/                 # (Optional) Virtual environment
```

---

## 🚀 Features

✅ Proof-of-Work algorithm
✅ Mining reward system
✅ Transaction pool before mining
✅ Decentralized node registration
✅ Consensus mechanism (longest valid chain wins)
✅ Real-time blockchain visualization (via web UI)

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/blockchain_simulation.git
cd blockchain_simulation
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔌 Running the Nodes

You can spin up multiple blockchain nodes on different ports:

```bash
# Launch node on port 5000
python run.py 5000

# Launch another node on port 5001
python run.py 5001
```

Once running, open the browser:

* `http://127.0.0.1:5000` → Node 1 Dashboard
* `http://127.0.0.1:5001` → Node 2 Dashboard

---

## 🌐 Flask API Endpoints

| Endpoint            | Method | Description                    |
| ------------------- | ------ | ------------------------------ |
| `/mine`             | `GET`  | Mines a new block              |
| `/transactions/new` | `POST` | Adds a new transaction         |
| `/chain`            | `GET`  | Returns the full blockchain    |
| `/nodes/register`   | `POST` | Register other nodes           |
| `/nodes/resolve`    | `GET`  | Resolve conflicts by consensus |

---

### 🧪 Sample API Usage

#### ➕ Add a transaction

```http
POST /transactions/new
Content-Type: application/json

{
  "sender": "Alice",
  "recipient": "Bob",
  "amount": 10
}
```

#### ⛏️ Mine a block

```http
GET /mine
```

#### 📦 View the blockchain

```http
GET /chain
```

#### 🌐 Register a node

```http
POST /nodes/register
Content-Type: application/json

{
  "nodes": ["http://127.0.0.1:5001"]
}
```

#### 🔁 Resolve conflicts (consensus)

```http
GET /nodes/resolve
```

---

## 💻 Frontend Dashboard

The HTML interface (`/templates/index.html`) allows you to:

* Add transactions via form
* Mine new blocks
* Resolve conflicts
* View the entire blockchain dynamically

![screenshot blockchain dashboard](https://via.placeholder.com/800x400?text=Blockchain+Dashboard+Preview)

---

## 🧠 How It Works

* **Proof of Work**: Uses a simple algorithm to find a number that when hashed with previous block’s hash, produces a hash with specific properties.
* **Transactions**: Stored temporarily until a block is mined.
* **Mining**: Solves the proof, appends block, and gives miner a reward.
* **Consensus**: If a node receives a longer valid chain, it replaces its own.
* **Decentralization**: Multiple nodes can be registered and sync over HTTP.

---

## 🛠️ Technologies Used

* Python 3
* Flask
* HTML/CSS (Vanilla)
* `hashlib`, `json`, `uuid`, `requests`, `time` (Standard Python)

---

## 🧪 Test Plan

* Launch 3+ nodes on different ports
* Add transactions and mine on different nodes
* Register nodes to each other using `/nodes/register`
* Use `/nodes/resolve` to sync the longest valid chain

---

## 🔒 Security Notes (for future improvements)

* Use digital signatures (RSA/ECDSA) for transaction authenticity
* Add persistent storage (SQLite, NoSQL, or JSON)
* Support smart contracts and Merkle Trees
* Migrate to WebSockets for real-time sync

