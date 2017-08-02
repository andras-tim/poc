#include "mainwindow.h"
#include "ui_mainwindow.h"

const QString MainWindow::WINDOW_TITLE = QString("Web Lullaby Demo");

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setWindowTitle(this->WINDOW_TITLE);
}

MainWindow::~MainWindow()
{
    delete ui;
}
