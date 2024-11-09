from django.shortcuts import render, redirect
from myapp.models import Colaborador,EPIgenerico, Emprestimo
from django.shortcuts import render, get_object_or_404




def frente(request):
    return render(request, 'myapp/globals/frente.html')

def cadastrarColaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        telefone = request.POST.get('telefone')
        if nome and cpf and telefone:
            Colaborador.objects.create(
                nome=nome,
                cpf=cpf,
                telefone=telefone
            )
            return redirect('/')
    return render(request, 'myapp/globals/cadastrarColaborador.html') 

def atualizarColaborador(request, id):
    Colaboradores = Colaborador.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cpf = request.POST.get('cpf')
        cargo = request.POST.get('cargo')
        telefone = request.POST.get('telefone')
        
        if nome and cpf and cargo and telefone:
            Colaboradores.nome = nome
            Colaboradores.cpf = cpf
            Colaboradores.cargo = cargo
            Colaboradores.telefone = telefone
            Colaboradores.save()
            return redirect('/')
        else:
            return render(request, 'globals/atualizar.html', {'atualizarColaborador': atualizarColaborador, "erro": True})

    return render(request, 'myapp/globals/atualizarColaborador.html')

def colaboradores(request):
    return render(request, 'myapp/globals/colaboradores.html')

def atualizarEPI(request, id):
    epis = EPIgenerico.objects.get(id=id)
    if request.method == 'POST':
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        prazo_dias = request.POST.get('prazo_dias')
        
        if nome and descricao and prazo_dias:
            epis.nome = nome
            epis.descricao = descricao
            epis.prazo_dias = prazo_dias
            epis.save()
            return redirect('/')
        else:
            return render(request, 'globals/atualizarEPI.html', {'atualizarEPI': atualizarEPI, "erro": True})
    return render(request, 'myapp/globals/atualizarEPI.html')

def cadastrarEPI(request):
    if request.method == 'POST':
        nome_epi = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        prazo_dias = request.POST.get('prazo_dias')
        if nome_epi and descricao and prazo_dias:
            EPIgenerico.objects.create(
                    nome = nome_epi,
                    descricao = descricao,
                    prazo_dias = prazo_dias,
            )
            return redirect('/')
    return render(request, 'myapp/globals/cadastrarEPI.html')

def registrar(request):
    colaboradores = Colaborador.objects.all()
    epis = EPIgenerico.objects.all()
    
    if request.method == 'POST':
        equipamento = EPIgenerico.objects.get(nome=request.POST.get('equipamento'))
        colaborador = Colaborador.objects.get(nome=request.POST.get('colaborador'))
        data_emprestimo = request.POST.get('data_emprestimo')
        data_prevista = request.POST.get('data_prevista')
        status = request.POST.get('status')
        condicoes = request.POST.get('condicoes_equipamento')
        data_devolucao = request.POST.get('data_devolucao')
        observacao = request.POST.get('observacao')

        print(equipamento, colaborador, data_emprestimo, data_prevista, status, condicoes, data_devolucao, observacao)
    
        print(equipamento.id, colaborador.id)
        
        
        if equipamento and colaborador and data_emprestimo and data_prevista and status and condicoes and data_devolucao and observacao:
            print("aobamein")
            Emprestimo.objects.create(
                id_EPIgenerico_fk = equipamento,
                nome = colaborador,
                data_emprestimo = data_emprestimo,
                data_prevista = data_prevista,
                status = status,
                condicoes = condicoes,
                data_devolucao = data_devolucao,
                motivo_devolucao = observacao
            )
        

            return redirect('/')
    return render(request, 'myapp/globals/registrar.html', {"colaboradores":colaboradores, "epis":epis})

def relatorioEPI(request):
    coladores = Colaborador.objects.all()
    epis = EPIgenerico.objects.all()
    emprestimo = Emprestimo.objects.all()
    if request.method == 'POST':

        colaborador_id = request.POST.get('colaborador')
        colaborador = get_object_or_404(Colaborador, id=colaborador_id)
        
        epi_id = request.POST.get('epi')
        epi = get_object_or_404(EPIgenerico, id=epi_id)
        status = request.POST.get('status')
        return render(request, 'myapp/globals/relatorioEPI.html', {"emprestimo":emprestimo, "colaboradores":coladores, "epis":epis, "colaborador":colaborador, "epi":epi, "status":status})

    return render(request, 'myapp/globals/relatorioEPI.html', {"emprestimo":emprestimo, "colaboradores":coladores, "epis":epis})

def relatorioColaborador(request):
    colaboradores = Colaborador.objects.all()
    emprestimo = Emprestimo.objects.all()

    if request.method == 'POST':
        colaborador = Colaborador.objects.get(nome=request.POST.get('colaborador'))
        print(colaborador)
        return render(request, 'myapp/globals/relatorioColaborador.html', {"emprestimo":emprestimo, "colaboradores":colaboradores, "colaborador":colaborador})
    return render(request, 'myapp/globals/relatorioColaborador.html', {"emprestimo":emprestimo, "colaboradores":colaboradores})

def colaboradorAtualizar(request):
    colaborador = Colaborador.objects.all()
    return render(request, 'myapp/globals/colaboradorAtualizar.html', {"colaboradores":colaborador})
def EPIatualizar(request):
    epi = EPIgenerico.objects.all()
    return render(request, 'myapp/globals/EPIatualizar.html', {"EPI":epi})

def deletarColaborador(request, id):
    int(id)
    colaboradores = Colaborador.objects.get(id=id)
    colaboradores.delete()
    return redirect('/')
def deletarEPI(request, id):
    int(id)
    epis = EPIgenerico.objects.get(id=id)
    epis.delete()
    return redirect('/')