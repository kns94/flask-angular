'use strict';


angular.module('myApp')
  .controller('HomeCtrl', function($scope, $http, $location) {

    $scope.submit = function() {

        $scope.out = {
            'argument1': $scope.arg1,
            'relation': $scope.rel,
            'argument2': $scope.arg2,
        };

        var data = {
            'arg1': $scope.arg1,
            'arg2': $scope.arg2,
            'rel': $scope.rel
        }

        var config = {
            headers : {
                'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8;'
            }
        }

        $http.post('/query', data)
            .success(function (response) {
                //$scope.ServerResponse = data;
                //$location.path('/query');
                $scope.temp = response;
                $location.path('/query/');
            })
            .error(function (data, status, header, config) {
                $location.path('/');
                $scope.ServerResponse = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
        });


        //$scope.dat = {
        //    'one': '1';
        //}
       
        //$location.path('/dashboard');
        
        //return false;
    };

    $scope.arg1 = '';
    $scope.rel = '';
    $scope.arg2 = '';

    $scope.one = function(){
        $scope.arg1 = 'People';
        $scope.rel = 'Killed';
        $scope.arg2 = 'ParisBombing';
    }

    $scope.two = function(){
        $scope.arg1 = 'Places';
        $scope.rel = 'Bombed';
        $scope.arg2 = 'ParisAttack';
    }

    $scope.three = function(){
        $scope.arg1 = 'Suspects';
        $scope.rel = 'Identified';
        $scope.arg2 = 'ParisAttack';
    }

    $scope.four = function(){
        $scope.arg1 = 'Suspects';
        $scope.rel = 'Nationalities';
        $scope.arg2 = 'ParisAttack';
    }

    $scope.check = function(){
        if($scope.arg1.length < 1 && $scope.arg2.length < 1){
            return true;
        }
        else{
            if($scope.arg1.length < 1 && $scope.rel.length < 1){
                return true;
            }
            else{
                if($scope.arg2.length < 1 && $scope.rel.length < 1){
                    return true;
                } 
                else{
                    return false;
                }             
            }
        }
    }   

  });

angular.module('myApp')
  .controller('QueryCtrl', function($scope, $http, $location) {

    var param = $routeParams.param;
  });
