'use strict';

/* Services */

var taskServices = angular.module('taskServices', []);

taskServices.factory('Task', ['Restangular',
  function(Restangular) {
    return Restangular.service('tasks');
  }]);

taskServices.factory('Session', ['Restangular',
  function(Restangular) {
    return Restangular.service('sessions');
  }]);
