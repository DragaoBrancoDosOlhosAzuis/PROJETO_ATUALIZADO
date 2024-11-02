from flask import Blueprint, request, jsonify
from app.db_config import db
from tinydb import Query

reserva_bp = Blueprint('reserva', __name__)

@reserva_bp.route('/reservar_pousada', methods=['POST'])
def reservar_pousada():
    cpf_cnpj = request.form.get('cpf_cnpj')
    pousada_id = request.form.get('pousada_id')
    data_fim = request.form.get('data_fim')

    if cpf_cnpj and pousada_id:
        Reserva = Query()
        reservas = db.search((Reserva.tipo == 'reserva') & (Reserva.pousada_id == pousada_id))
        if reservas:
            return jsonify({'message': 'Pousada já reservada!'}), 400

        db.insert({'tipo': 'reserva', 'cpf_cnpj': cpf_cnpj, 'pousada_id': pousada_id, 'data_fim': data_fim})
        db.update({'status': 'reservada'}, Query().id == pousada_id)
        return jsonify({'message': 'Reserva feita com sucesso!'}), 200
    return jsonify({'message': 'Falha ao reservar pousada! Campos vazios.'}), 400

@reserva_bp.route('/listar_reservas', methods=['GET'])
def listar_reservas():
    Reserva = Query()
    reservas = db.search(Reserva.tipo == 'reserva')
    return jsonify(reservas), 200

@reserva_bp.route('/editar_reserva', methods=['POST'])
def editar_reserva():
    cpf_cnpj = request.form.get('cpf_cnpj')
    pousada_id = request.form.get('pousada_id')
    data_fim = request.form.get('data_fim')

    if cpf_cnpj and pousada_id:
        Reserva = Query()
        result = db.update(
            {'data_fim': data_fim},
            (Reserva.tipo == 'reserva') & (Reserva.cpf_cnpj == cpf_cnpj) & (Reserva.pousada_id == pousada_id)
        )

        if result:
            return jsonify({'message': 'Reserva atualizada com sucesso!'}), 200
        else:
            return jsonify({'message': 'Reserva não encontrada!'}), 404

    return jsonify({'message': 'Falha ao atualizar reserva! Campos vazios.'}), 400

@reserva_bp.route('/remover_reserva', methods=['POST'])
def remover_reserva():
    cpf_cnpj = request.form.get('cpf_cnpj')
    pousada_id = request.form.get('pousada_id')

    if cpf_cnpj and pousada_id:
        Reserva = Query()
        db.remove((Reserva.tipo == 'reserva') & (Reserva.cpf_cnpj == cpf_cnpj) & (Reserva.pousada_id == pousada_id))
        db.update({'status': 'livre'}, Query().id == pousada_id)  # Define a pousada como "livre" após remoção da reserva
        return jsonify({'message': 'Reserva removida com sucesso!'}), 200
    return jsonify({'message': 'Falha ao remover reserva! Campos vazios.'}), 400
