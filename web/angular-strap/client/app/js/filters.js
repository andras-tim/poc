'use strict';

/* Filters */

var taskFilters = angular.module('taskFilters', [])

taskFilters.filter('checkmark', function() {
  return function(input) {
    return input ? '\u2713' : '\u2718';
  };
});
