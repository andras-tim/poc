'use strict';

/* Controllers */

var taskControllers = angular.module('taskControllers', []);

taskControllers.controller('CommonCtrl', function($scope, Restangular, $alert) {
  Restangular.setErrorInterceptor(function (resp) {
    console.debug(resp);
    $alert({
      title: "Error " + resp.status,
      content: resp.statusText + "<br />" + resp.data,
      container: "body",
      placement: "top-right",
      type: "danger",
      duration: 10,
      show: true
    });
  });
});

taskControllers.controller('TaskListCtrl', ['$scope', 'Task',
  function($scope, Task) {
    $scope.tasks = Task.getList().$object;
    $scope.orderProp = 'title';

    $scope.toggle_done = function(task) {
      task.done = ! task.done;
      task.put();
    }

    $scope.remove = function(task) {
      task.remove().then(function() {
        $scope.tasks = _.without($scope.tasks, task);
      });
    }
  }]);

taskControllers.controller('AddTaskCtrl', ['$scope', 'Restangular', 'Task',
  function($scope, Restangular, Task) {
    $scope.task = {title: '', description: ''};

    $scope.update = function(task) {
      Task.post(Restangular.copy(task)).then(function(resp) {
        $scope.tasks.push(resp);
      });
    }
  }]);

taskControllers.controller('TaskDetailCtrl', ['$scope', '$routeParams', 'Task',
  function($scope, $routeParams, Task) {
    $scope.task = Task.one($routeParams.taskId).get().$object;
  }]);
