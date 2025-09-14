import logging
import json
import azure.functions as func

from .cpf_validator import is_cpf_valid

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Ponto de entrada da Azure Function para validação de CPF.
    """
    logging.info('Requisição de validação de CPF recebida.')

    cpf = req.params.get('cpf')
    if not cpf:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            cpf = req_body.get('cpf')

    if cpf:
        if is_cpf_valid(cpf):
            response_data = {
                "cpf": cpf,
                "isValid": True,
                "message": "CPF válido."
            }
            return func.HttpResponse(
                body=json.dumps(response_data, ensure_ascii=False),
                mimetype="application/json",
                status_code=200
            )
        else:
            response_data = {
                "cpf": cpf,
                "isValid": False,
                "message": "CPF inválido."
            }
            return func.HttpResponse(
                body=json.dumps(response_data, ensure_ascii=False),
                mimetype="application/json",
                status_code=400
            )
    else:
        response_data = {
            "error": "Por favor, forneça um CPF no corpo da requisição (JSON) ou como um parâmetro de consulta (query string)."
        }
        return func.HttpResponse(
            body=json.dumps(response_data, ensure_ascii=False),
            mimetype="application/json",
            status_code=400
        )
