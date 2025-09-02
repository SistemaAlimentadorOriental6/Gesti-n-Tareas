from django.core.mail import EmailMessage
from django.conf import settings  

def enviar_componente_por_correo(componente, destinatario):
    asunto = f"Componente Reparado N° {componente.id}"
    mensaje = "Adjunto encontrarás el comprobante del componente reparado."

    email = EmailMessage(
        asunto,
        mensaje,
        settings.DEFAULT_FROM_EMAIL,
        [destinatario],
    )
    email.attach(f'componente_{componente.id}.pdf', 'application/pdf')
    email.send()