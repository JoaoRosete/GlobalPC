from django.shortcuts import redirect

# Em vez de o servidor abrir no default 800 com a página de erro agora abre com 800/loja/inicio
def inicio_redirect(request):
    return redirect('/loja/inicio/')
