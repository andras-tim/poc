'use strict';

/* Services */

var taskServices = angular.module('taskServices', []);

taskServices.factory('Task', ['Restangular',
  function(Restangular) {
    return Restangular.service('tasks');
  }]);
