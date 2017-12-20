/*****************************************************
SCRIPT DE CONTROLE DE EVENTOS JS
*****************************************************/

// BOTÃO EDITAR NOTA
// atribuindo evento clicar ao botão editar nota
$(document).on('click', '.bot_editar_nota', function(event) {
    // desabilitando recarregamento da página
    event.preventDefault();
    // salva id da nota na sessão
    sessionStorage.setItem('id_nota', obter_id($(this)));
    // carregando página de editar
    window.open('editar.html', '_self');
});


// BOTÃO EXCLUIR NOTA
// atribuindo evento clicar ao botão excluir nota
$(document).on('click', '.bot_excluir_nota', function(event) {
    // desabilitando recarregamento da página
    event.preventDefault();
    // validação de exclusão
    if (confirm('Deseja mesmo excluir essa nota?')){
        // obtendo id da nota e serializando
        id_nota = 'id_nota=' + obter_id($(this));
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados
            data: obter_sessao() + '&' + id_nota,
            // requisição POST
            type: 'POST',
            // url da api do servidor
            url: 'http://127.0.0.1:8000/notas/deletar/',
            // requisição efetuada com sucesso
            success: function(resposta) {
                // transforma resposta em um objeto json
                resposta = JSON.parse(resposta);
                // exibe mensagem
                alert(resposta.mensagem);
                // carregando página de notas
                window.open('notas.html', '_self');
            },
        });
    }
});


// ao carregar documento
$(document).ready(function() {
    
    // BOTÃO CADASTRAR NOVO USUÁRIO
    // atribuindo evento clicar ao botão cadastrar
    $("#bot_cadastrar").click(function(event) {
        // desabilitando recarregamento da página
        event.preventDefault();
        // carregando página de cadastro
        window.open('cadastro.html', '_self');
    });


    // BOTÃO NOVA NOTA
    // atribuindo evento clicar ao botão nova nota
    $("#bot_nova_nota").click(function(event) {
        // desabilitando recarregamento da página
        event.preventDefault();
        // carregando página de cadastro
        window.open('nova.html', '_self');
    });


    // BOTÃO CANCELAR NOTA
    // atribuindo evento clicar ao botão cancelar nota
    $("#bot_cancelar_nota").click(function(event) {
        // desabilitando recarregamento da página
        event.preventDefault();
        // carregando página de cadastro
        window.open('notas.html', '_self');
    });


    // LINK SAIR
    // atribuindo evento clicar ao botão cadastrar
    $("#link_logout").click(function(event) {
        // desabilitando recarregamento da página
        event.preventDefault();
        // carregando página de cadastro
        logout('Até logo!')
    });


    // ENVIAR FORMULÁRIO DE CADASTRO
    // atribuindo evento de enviar cadastro
    $("#form_cadastro").submit(function(event){
        // previnindo recarregamento da página
        event.preventDefault();
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados do formulário e serializando
            data: $(this).serialize(),
            // obtendo tipo de requisição
            type: $(this).attr('method'),
            // url da api
            url: 'http://127.0.0.1:8000/notas/cadastrar/',
            // requisição efetuada com sucesso
            success: function(resposta) {
                // transforma resposta em um objeto json
                resposta = JSON.parse(resposta);
                // se o estado da requisição for de sucesso
                if (resposta.estado === 'sucesso') {
                    // exibe mensagem de sucesso
                    alert(resposta.mensagem);
                    // carregando página de login
                    window.open('login.html', '_self');
                // se não for sucesso
                } else {
                    // exibe mensagem de erro
                    alert(resposta.mensagem);
                    // recarrega página
                    window.open('cadastro.html', '_self')
                }            
            }
        });
        // retornando falso (cancela ação padrão de submit)
        return false;
    });


    // ENVIAR FORMULÁRIO DE LOGIN
    // atribuindo evento de enviar login
    $("#form_login").submit(function(event){
        // desabilitando recarregamento da página
        event.preventDefault();
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados do formulário
            data: $(this).serialize(),
            // obtendo o tipo de requisição
            type: $(this).attr('method'),
            // url da api do servidor
            url: 'http://127.0.0.1:8000/notas/login/',
            // requisição efetuada com sucesso
            success: function(resposta) {
                // transforma resposta em um objeto json
                resposta = JSON.parse(resposta);
                // se o estado da requisição for de sucesso
                if (resposta.estado === 'sucesso') {
                    // salva nome na sessão
                    sessionStorage.setItem('nome', resposta.nome);
                    // salva nome de usuario na sessão
                    sessionStorage.setItem('username', resposta.username);
                    // salva senha na sessão
                    sessionStorage.setItem('password', resposta.password);
                    // carregando página de notas
                    window.open('notas.html', '_self');
                // se o estado for erro
                } else {
                    // exibe mensagem de erro
                    alert(resposta.mensagem);
                }
            },
        });
        // retornando falso (cancela ação padrão de submit)
        return false;
    });


    // ENVIAR FORMULÁRIO DE NOVA NOTA
    // atribuindo evento de enviar nova nota
    $("#form_nova_nota").submit(function(event){
        // desabilitando recarregamento da página
        event.preventDefault();
        // montando json para envio com dados da sessão e do formulário
        var dados = obter_sessao() + '&' + $(this).serialize();
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados
            data: dados,
            // obtendo o tipo de requisição
            type: $(this).attr('method'),
            // url da api do servidor
            url: 'http://127.0.0.1:8000/notas/nova/',
            // requisição efetuada com sucesso
            success: function(resposta) {
                // transforma resposta em um objeto json
                resposta = JSON.parse(resposta);
                // se o estado da requisição for de sucesso
                if (resposta.estado === 'sucesso') {
                    // exibe mensagem de sucesso
                    alert(resposta.mensagem);
                    // carregando página de notas
                    window.open('notas.html', '_self');
                // se o estado for erro
                } else {
                    // exibe mensagem de erro
                    alert(resposta.mensagem);
                }
            },
        });
        // retornando falso (cancela ação padrão de submit)
        return false;
    });


    // ENVIAR FORMULÁRIO EDITAR NOTA
    // atribuindo evento de enviar edição da nota
    $("#form_editar_nota").submit(function(event){
        // desabilitando recarregamento da página
        event.preventDefault();
        // montando json para envio com dados da sessão e do formulário
        var dados = obter_sessao() + '&' + $(this).serialize();
        // efetuando requisição ajax
        $.ajax({
            // obtendo dados
            data: dados,
            // obtendo o tipo de requisição
            type: $(this).attr('method'),
            // url da api do servidor
            url: 'http://127.0.0.1:8000/notas/editar/',
            // requisição efetuada com sucesso
            success: function(resposta) {
                // transforma resposta em um objeto json
                resposta = JSON.parse(resposta);
                // exibe mensagem
                alert(resposta.mensagem);
                // remove id da nota editada da sessão
                sessionStorage.removeItem('id_nota');
                // carregando página de notas
                window.open('notas.html', '_self');
            },
        });
        // retornando falso (cancela ação padrão de submit)
        return false;
    });
});