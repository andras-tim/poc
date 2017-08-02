#include "screensaver.h"
#include "ui_screensaver.h"

Screensaver::Screensaver(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Screensaver)
{
    ui->setupUi(this);

    ui->webView->load(QUrl("https://web-animations.github.io/web-animations-demos/#galaxy/"));
}

Screensaver::~Screensaver()
{
    delete ui;
}

void Screensaver::on_webView_titleChanged(const QString &title)
{
    this->setWindowTitle(title);
}
