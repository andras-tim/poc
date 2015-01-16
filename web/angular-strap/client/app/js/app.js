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
  'taskServices',
  'taskDirectives'
]);


taskApp.constant('AUTH_EVENTS', {
  loginSuccess: 'auth-login-success',
  loginFailed: 'auth-login-failed',
  logoutSuccess: 'auth-logout-success',
  sessionTimeout: 'auth-session-timeout',
  notAuthenticated: 'auth-not-authenticated',
  notAuthorized: 'auth-not-authorized'
});

taskApp.constant('USER_ROLES', {
  all: '*',
  admin: 'admin',
  editor: 'editor',
  guest: 'guest'
});


taskApp.constant('ROUTES', {
  "/tasks": {
    templateUrl: 'partials/task-list.html',
    controller: 'TaskListCtrl',
    data: {
      authorizedRoles: ['admin', 'editor']
    }
  },
  "/tasks/:taskId": {
    templateUrl: 'partials/task-detail.html',
    controller: 'TaskDetailCtrl',
    data: {
      authorizedRoles: ['all']
    }
  }
});


taskApp.config(['$modalProvider',
  function($modalProvider) {
    angular.extend($modalProvider.defaults, {
      html: true
    });
  }]);


taskApp.config(function($routeProvider, ROUTES) {
  for(var path in ROUTES) {
    $routeProvider.when(path, ROUTES[path]);
  }
  $routeProvider.otherwise({
    redirectTo: '/tasks'
  });
});


taskApp.config(['RestangularProvider',
  function(RestangularProvider) {
    RestangularProvider.setBaseUrl('api');
  }]);


taskApp.run(function ($rootScope, AUTH_EVENTS, AuthService, ROUTES) {
  $rootScope.$on('$locationChangeStart', function (event, next, current) {
    for (var path in ROUTES) {
      if (next.indexOf(path) != -1) {
        var route = ROUTES[path];
        var authorizedRoles = route.data.authorizedRoles;
        if (!AuthService.isAuthorized(authorizedRoles)) {
          event.preventDefault();
          if (AuthService.isAuthenticated()) {
            console.debug("user is not allowed");
            $rootScope.$broadcast(AUTH_EVENTS.notAuthorized);
          } else {
            console.debug("user is not logged in");
            $rootScope.$broadcast(AUTH_EVENTS.notAuthenticated);
          }
        }
      }
    }
  });
});


taskApp.run(function (Restangular, AuthInterceptor) {
  Restangular.setErrorInterceptor(AuthInterceptor);
});
