function TasksViewModel()
{
  var self = this;
  self.tasks = ko.observableArray();


  self.tasks([
    {
      title: ko.observable('title #1'),
      description: ko.observable('description #1'),
      done: ko.observable(false)
    },
    {
      title: ko.observable('title #2'),
      description: ko.observable('description #2'),
      done: ko.observable(true)
    }
  ]);


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
}

ko.applyBindings(new TasksViewModel(), $('#main')[0]);
