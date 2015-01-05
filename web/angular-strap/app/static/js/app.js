'use strict';

/* App Module */

var taskApp = angular.module('taskApp', [
  'mgcrea.ngStrap',
  'ngRoute',
  'taskControllers',
  'taskFilters',
  'taskServices'
]);

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
