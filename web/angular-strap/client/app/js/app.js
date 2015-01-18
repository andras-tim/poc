'use strict';

/* App Module */

var taskApp = angular.module('taskApp', [
  'mgcrea.ngStrap',
  'ngSanitize',
  'ngRoute',
  'ngAnimate',
  'restangular',
  'gettext',
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
      when('/login', {
        templateUrl: 'partials/login.html',
        controller: 'LoginCtrl'
      }).
      when('/tasks', {
        templateUrl: 'partials/task-list.html',
        controller: 'TaskListCtrl'
      }).
      when('/tasks/:taskId', {
        templateUrl: 'partials/task-detail.html',
        controller: 'TaskDetailCtrl'
      }).
      otherwise({
        redirectTo: '/login'
      });
  }]);

taskApp.config(['RestangularProvider',
  function(RestangularProvider) {
    RestangularProvider.setBaseUrl('api');
  }]);


taskApp.run(function (gettextCatalog) {
  gettextCatalog.currentLanguage = 'en';
  gettextCatalog.debug = true;
});
