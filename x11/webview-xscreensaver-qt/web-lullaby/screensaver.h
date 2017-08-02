#ifndef SCREENSAVER_H
#define SCREENSAVER_H

#include <QWidget>

namespace Ui {
class Screensaver;
}

class Screensaver : public QWidget
{
    Q_OBJECT

public:
    explicit Screensaver(QWidget *parent = 0);
    ~Screensaver();

private slots:
    void on_webView_titleChanged(const QString &title);

private:
    Ui::Screensaver *ui;
};

#endif // SCREENSAVER_H
