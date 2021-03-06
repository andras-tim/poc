#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_widget_windowTitleChanged(const QString &title);

private:
    Ui::MainWindow *ui;
    static const QString WINDOW_TITLE;
};

#endif // MAINWINDOW_H
