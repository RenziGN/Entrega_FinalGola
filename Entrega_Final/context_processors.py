from ..Login.models import Usuario

def usuario_context(req):
    usuario = None
    if req.user.is_authenticated:
        try:
            usuario = Usuario.objects.get(user=req.user)
        except Usuario.DoesNotExist:
            pass
    return {'usuario': usuario}