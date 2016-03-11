'use strict';  

var myApp = angular.module('myApp', ['ngRoute', 'ngAnimate']);

myApp.config(['$routeProvider',
     function($routeProvider) {
         $routeProvider.
             when('/', {
                 templateUrl: 'static/partials/home.html',
                 controller: 'HomeCtrl',    
             }).
             when('/queryOut', {
                 templateUrl: 'static/partials/queryOut.html',
                 controller: 'QueryCtrl',
             }).
             otherwise({
                 redirectTo: '/'
             });
    }]);