'use strict';

/* Services */

var taskServices = angular.module('taskServices', ['ngResource']);

taskServices.factory('Task', ['$resource',
  function($resource){
    return $resource('api/tasks/:taskId', {taskId:'@id'}, {
      'put': {method:'PUT'}
    });
  }]);
