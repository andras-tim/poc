function TasksViewModel()
{
  var self = this;
  self.tasksURI = 'http://localhost:5000/todo/api/v1.0/tasks';
  self.username = "miguel";
  self.password = "python";
  self.tasks = ko.observableArray();

  self.ajax = function(uri, method, data)
  {
    var request = {
      url: uri,
      type: method,
      contentType: "application/json",
      accepts: "application/json",
      cache: false,
      dataType: 'json',
      data: JSON.stringify(data),
      beforeSend: function (xhr)
      {
        xhr.setRequestHeader("Authorization", "Basic " + btoa(self.username + ":" + self.password));
      },
      error: function(jqXHR)
      {
        console.log("ajax error " + jqXHR.status);
      }
    };
    return $.ajax(request);
  }

  self.beginAdd = function()
  {
      alert("Add");
  }

  self.beginEdit = function(task)
  {
      alert("Edit: " + task.title());
  }

  self.remove = function(task)
  {
      alert("Remove: " + task.title());
  }

  self.markInProgress = function(task)
  {
      task.done(false);
  }

  self.markDone = function(task)
  {
      task.done(true);
  }


  self.ajax(self.tasksURI, 'GET').done(function(data)
  {
    for (var i = 0; i < data.tasks.length; i++) {
      self.tasks.push({
        uri: ko.observable(data.tasks[i].uri),
        title: ko.observable(data.tasks[i].title),
        description: ko.observable(data.tasks[i].description),
        done: ko.observable(data.tasks[i].done)
      });
    }
  });

}

ko.applyBindings(new TasksViewModel(), $('#main')[0]);
