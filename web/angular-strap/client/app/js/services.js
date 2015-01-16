'use strict';

/* Services */

var taskServices = angular.module('taskServices', []);

taskServices.factory('AuthService', function (Restangular, Session) {
  var authService = Restangular.service('sessions');

  authService.login = function (credentials) {
    return authService.post({email: credentials.username, password: credentials.password}).then(
      function (user) {
        console.debug(["AuthService/login", user]);
        Session.create(user.id, user.email,
                       user.roles);
        return user;
      });
  };

  authService.isAuthenticated = function () {
    return !!Session.userId;
  };

  authService.isAuthorized = function (authorizedRoles) {
    if (!angular.isArray(authorizedRoles)) {
      authorizedRoles = [authorizedRoles];
    }
    return (authService.isAuthenticated() &&
      authorizedRoles.indexOf(Session.userRole) !== -1);
  };

  return authService;
});

taskServices.factory('AuthInterceptor', function ($rootScope, $q, AUTH_EVENTS) {
  return function (response) {
    console.debug(["AuthInterceptor", response]);
    $rootScope.$broadcast({
      401: AUTH_EVENTS.notAuthenticated,
      403: AUTH_EVENTS.notAuthorized,
      419: AUTH_EVENTS.sessionTimeout,
      440: AUTH_EVENTS.sessionTimeout
    }[response.status], response);
    return $q.reject(response);
  };
});


taskServices.service('Session', function () {
  this.create = function (sessionId, userId, userRole) {
    this.id = sessionId;
    this.userId = userId;
    this.userRole = userRole;
  };
  this.destroy = function () {
    this.id = null;
    this.userId = null;
    this.userRole = null;
  };
  return this;
})

taskServices.factory('Task', ['Restangular',
  function(Restangular) {
    return Restangular.service('tasks');
  }]);
