from flask import Flask, jsonify, request, render_template
from uuid import uuid4
from blockchain import Blockchain
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

node_identifier = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/')
def dashboard():
    return render_template('index.html')


@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.last_block
    proof = blockchain.proof_of_work(last_block['proof'])

    blockchain.new_transaction(sender="0", recipient=node_identifier, amount=1)
    block = blockchain.new_block(proof)

    block_with_hash = block.copy()
    block_with_hash['hash'] = blockchain.hash(block)
    return jsonify(block_with_hash), 200


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
        return 'Missing values', 400
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201


@app.route('/chain', methods=['GET'])
def full_chain():
    chain_with_hashes = []
    for block in blockchain.chain:
        block_copy = block.copy()
        block_copy['hash'] = blockchain.hash(block)
        chain_with_hashes.append(block_copy)
    return jsonify({'chain': chain_with_hashes, 'length': len(chain_with_hashes)}), 200


@app.route('/nodes/register', methods=['POST'])
def register_nodes():
    values = request.get_json()
    nodes = values.get('nodes')
    if nodes is None:
        return "Error: Please supply a valid list of nodes", 400
    for node in nodes:
        blockchain.register_node(node)
    return jsonify({'message': 'New nodes added', 'nodes': list(blockchain.nodes)}), 201


@app.route('/nodes/resolve', methods=['GET'])
def consensus():
    replaced = blockchain.resolve_conflicts()
    updated_chain = []
    for block in blockchain.chain:
        block_copy = block.copy()
        block_copy['hash'] = blockchain.hash(block)
        updated_chain.append(block_copy)

    if replaced:
        return jsonify({'message': 'Our chain was replaced', 'new_chain': updated_chain}), 200
    else:
        return jsonify({'message': 'Our chain is authoritative', 'chain': updated_chain}), 200

@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response
