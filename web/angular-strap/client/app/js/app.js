'use strict';

/* App Module */

var taskApp = angular.module('taskApp', [
  'mgcrea.ngStrap',
  'ngSanitize',
  'ngRoute',
  'ngAnimate',
  'restangular',
  'taskControllers',
  'taskFilters',
  'taskServices'
]);

taskApp.config(['$modalProvider',
  function($modalProvider) {
    angular.extend($modalProvider.defaults, {
      html: true
    });
  }]);


taskApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('/tasks', {
        templateUrl: 'partials/task-list.html',
        controller: 'TaskListCtrl'
      }).
      when('/tasks/:taskId', {
        templateUrl: 'partials/task-detail.html',
        controller: 'TaskDetailCtrl'
      }).
      otherwise({
        redirectTo: '/tasks'
      });
  }]);

taskApp.config(['RestangularProvider',
  function(RestangularProvider) {
    RestangularProvider.setBaseUrl('api');
  }]);
