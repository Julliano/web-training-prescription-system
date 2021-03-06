;(function() {
	"use strict";

	angular.module("consultoria").controller("LiberarTreinoAdminController", LiberarTreinoAdminController);

	LiberarTreinoAdminController.$inject = ['$http', 'LoginService', 'Notification', 'treino', '$state'];

	function LiberarTreinoAdminController($http, LoginService, Notification, treino, $state) {
		var vm = this;
		vm.usuario = LoginService.getUsuario();
		vm.treino = treino;
		vm.salvar = salvar;
		vm.ajusteFormulario = ajusteFormulario;
		vm.submitPromise = { message : "Aguarde..."	};
		vm.baixarArquivo = baixarArquivo;
		
		init();
		
		function init(){
			$http.get('/admin/modeloTreino/').then(function(response){
				vm.modelos = response.data
			})
			$http.get('/admin/arquivos/' + vm.treino.venda.id).then(function(response){
				vm.arquivos = response.data
			})
			$http.get('/usu/treinos/' + vm.treino.venda.usuario.id).then(function(response){
				vm.treinosUsuario = response.data
			})
		}
		
		function baixarArquivo(nome){
			var fd = new FormData();
			fd.append('id', vm.treino.venda.id);
			fd.append('nome', nome);
			$http.put('/arquivosInternos/', fd, {
				timeout : 50400000,
				transformRequest : angular.identity,
				responseType: 'arraybuffer',
				headers : {
					'Content-Type' : undefined
				}
			}).then(function(response){
				var blob = new Blob([response.data], {
					 type: 'application/pdf'
					});
				saveAs(blob, nome);
			})
		}
		
		function salvar(){
			vm.treino.nome = vm.modelo.titulo
			vm.treino.explicacao = vm.modelo.explicacao
			vm.treino.ver = vm.modelo.ver
			$http.put('/admin/treinos/', vm.treino).then(httpSuccess, httpFail)
		}
		
		function ajusteFormulario(){
			vm.submitPromise.promise = $http.put('/ajustarFormulario/', vm.treino.venda).then(httpSuccessFormulario, httpFailFormulario)
		}
		

		function httpSuccess(response) {
			Notification.success("Treino liberado com sucesso");
			$state.go("admin.treinos")
		}
		
		function httpFail(response) {
			Notification.error("Erro, favor contate o administrador do sistema.");
		}

		function httpSuccessFormulario(response) {
			Notification.success("Solicitacao de ajuste enviada");
			$state.go("admin.treinos")
		}
	
		function httpFailFormulario(response) {
			Notification.error("Erro, favor contate o administrador do sistema.");
		}
		
	}
})();