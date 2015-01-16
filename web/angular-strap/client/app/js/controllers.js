'use strict';

/* Controllers */

var taskControllers = angular.module('taskControllers', []);

taskControllers.controller('ApplicationController', function ($scope, USER_ROLES, AuthService) {
  $scope.currentUser = null;
  $scope.userRoles = USER_ROLES;
  $scope.isAuthorized = AuthService.isAuthorized;
  $scope.isLoginPage  = false;

  $scope.setCurrentUser = function (user) {
    $scope.currentUser = user;
  };
})

taskControllers.controller('LoginController', function ($scope, $rootScope, AUTH_EVENTS, AuthService) {
  $scope.credentials = {
    username: '',
    password: ''
  };
  $scope.login = function (credentials) {
    AuthService.login(credentials).then(function (user) {
      $rootScope.$broadcast(AUTH_EVENTS.loginSuccess);
      $scope.setCurrentUser(user);
    }, function () {
      $rootScope.$broadcast(AUTH_EVENTS.loginFailed);
    });
  };
})

taskControllers.controller('TaskListCtrl', function($scope, $location, Task, Session) {
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
  });

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
