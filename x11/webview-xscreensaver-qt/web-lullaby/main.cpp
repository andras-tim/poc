#include "main.h"

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QApplication::setStyle(QStyleFactory::create("gtk"));
    MainWindow w;

    WId window_id = getXScreensaverWindowId();

    QMessageBox::information(w, "!!!", QString("%1\n%2").arg(window_id).arg(qgetenv("XSCREENSAVER_WINDOW").constData()));

    if (window_id == 0x0)
    {
        runDemoMode(&w);
    }
    else
    {
        runScreensaver(&w, window_id);
    }

    return a.exec();
}


void runDemoMode(MainWindow *w)
{
    w->show();
}

void runScreensaver(MainWindow *w, const WId window_id)
{
    QWindow* parent_window = QWindow::fromWinId(window_id);
    //QWidget* parent_widget = QWidget::createWindowContainer(parent_window);

    parent_window->show();
    parent_window->requestActivate();

    //w->setWindowFlags(w->windowFlags() | Qt::FramelessWindowHint);

    qDebug() << "Geometry:" << parent_window->geometry();
    qDebug() << "Active?:" << parent_window->isActive();
    qDebug() << "Flags:" << parent_window->flags();

    // TODO: https://bugreports.qt.io/browse/QTBUG-40320
    //w->setParent(parent_widget);
    //w->setGeometry(parent_window->geometry());

    w->show();

    delete parent_widget;
    delete parent_window;
}


WId getXScreensaverWindowId()
{
    bool convert_ok;
    WId window_id;

    QByteArray xscreensaver_window = qgetenv("XSCREENSAVER_WINDOW");

    if (xscreensaver_window.isNull())
    {
        //return WId(0x68000E1);
        //return WId(117440838);
        return WId(0);
    }

    window_id = (WId)(xscreensaver_window.toULongLong(&convert_ok, 16));
    if (!convert_ok)
    {
        return WId(0);
    }

    return window_id;
}
