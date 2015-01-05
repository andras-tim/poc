'use strict';

/* Controllers */

var taskControllers = angular.module('taskControllers', []);

taskControllers.controller('TaskListCtrl', ['$scope', 'Task',
  function($scope, Task) {

    Task.query({}, function(tasks) {
      console.debug(tasks);

      if (tasks.length == 4) {
        tasks[1].$delete();

      } else if (tasks.length <= 4) {
        var newTask = new Task();
        newTask.title = 'Tia Random ' + Math.floor((Math.random() * 1000) + 1);
        newTask.description = 'oasndfoijasfio asoifjasdf';
        newTask.$save();
      }

      tasks[0].done = !tasks[0].done;
      console.debug(tasks[0])
      tasks[0].$put();
    });

    $scope.tasks = Task.query();
    $scope.orderProp = 'title';
  }]);

taskControllers.controller('TaskDetailCtrl', ['$scope', '$routeParams', 'Task',
  function($scope, $routeParams, Task) {
    $scope.task = Task.get({taskId: $routeParams.taskId});
  }]);
