'use strict';

/* Controllers */

var taskControllers = angular.module('taskControllers', []);

taskControllers.controller('CommonCtrl', function($scope, Restangular, $alert, gettextCatalog) {
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


  $scope.changeLanguage = function (lang) {
    gettextCatalog.currentLanguage = lang;
  };
});

taskControllers.controller('LoginCtrl', function($scope, $location, Restangular, Session) {
  //$scope.is_authenticated = false;

  $scope.login = function() {
    $scope.$broadcast('show-errors-check-validity');
    if ($scope.userForm.$valid) {
      Session.post({email: $scope.user.email, password: $scope.user.password}).then(function (resp) {
        console.debug("OK");
        console.debug(resp);
        $scope.reset();
        $location.path('/tasks');
      }, function(resp) {
        console.debug(resp.status + " " + resp.statusText + ": " + JSON.stringify(resp.data));
      });
    }
  }
  $scope.reset = function () {
    $scope.$broadcast('show-errors-reset');
    $scope.user = { email: '', password: '' }
  }

  $scope.reset();
});

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

    $scope.login = function() {
      $location.path('/login');
    }

    $scope.loginTest = function() {
      Session.one().get().then(function (resp) {
        console.debug(resp);
      });
    }

    $scope.logout = function() {
      Session.one().remove().then(function (resp) {
        console.debug(resp);
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
