'use strict';


angular.module('myApp')
  .controller('HomeCtrl', function($scope, $http, $location, dataShare, localStorageService) {

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

                $scope.status = response.status
                $scope.$watch('status', function () {
                    if ($scope.status == "Error!") {
                        $location.path('/not_found');  
                    } else {
                        dataShare.sendData(data);
                        localStorageService.set('params',data);
                        $location.path('/queryOut');
                    }
                });
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
        $scope.arg1 = 'people';
        $scope.rel = 'killed';
        $scope.arg2 = 'parisBombing';
    }

    $scope.two = function(){
        $scope.arg1 = 'places';
        $scope.rel = 'bombed';
        $scope.arg2 = 'parisAttack';
    }

    $scope.three = function(){
        $scope.arg1 = 'suspects';
        $scope.rel = 'identified';
        $scope.arg2 = 'parisAttack';
    }

    $scope.four = function(){
        $scope.arg1 = 'suspects';
        $scope.rel = 'nationalities';
        $scope.arg2 = 'parisAttack';
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
  .controller('QueryCtrl', function($scope, $http, $location, dataShare, localStorageService) {

    //$scope.jsonify = JSON.parse($scope.data);
    //$scope.data = ''
    //$scope.init = function(){
    //    $scope.data = dataShare.getData();
    //};

    $scope.params = localStorageService.get('params');
    $scope.out = ''

     $http.post('/query', $scope.params)
            .success(function (response) {
                //$scope.ServerResponse = data;
                //$location.path('/query');

                $scope.status = response.status
                $scope.$watch('status', function () {
                    if ($scope.status == "Error!") {
                        $location.path('/not_found');  
                    } else {
                       $scope.out = response.data.data
                    }
                });
            })
            .error(function (data, status, header, config) {
                $location.path('/');
                $scope.ServerResponse = "Data: " + data +
                    "<hr />status: " + status +
                    "<hr />headers: " + header +
                    "<hr />config: " + config;
        });

});
  