#ifndef MAIN_H
#define MAIN_H

#include "mainwindow.h"
#include "screensaver.h"
#include <QApplication>
#include <QStyleFactory>
#include <QWindow>
#include <QMessageBox>
#include <QDebug>

int main(int argc, char *argv[]);

void runDemoMode(MainWindow *w);
void runScreensaver(MainWindow *w, const WId window_id);

WId getXScreensaverWindowId();

#endif // MAIN_H
