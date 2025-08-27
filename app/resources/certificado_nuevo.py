# app/resources/certificado_resource.py
from flask import Blueprint, send_file, jsonify, abort
from app.services.alumno_service import AlumnoService

certificado_bp = Blueprint("certificado", __name__)

@certificado_bp.route("/ficha/<int:id>/json", methods=["GET"])
def certificado_json(id: int):
    res = AlumnoService.obtener_ficha_alumno(id)
    if not res:
        abort(404, description="Alumno no encontrado")
    return jsonify(res)

@certificado_bp.route("/ficha/<int:id>/pdf", methods=["GET"])
def ficha_pdf(id: int):
    res = AlumnoService.generar_ficha_pdf(id)
    if not res:
        abort(404, description="Alumno no encontrado")

    buffer, filename = res
    return send_file(
        buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name=filename,
    )
