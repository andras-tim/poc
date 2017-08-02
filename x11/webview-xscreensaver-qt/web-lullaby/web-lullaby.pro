#-------------------------------------------------
#
# Project created by QtCreator 2017-08-03T00:23:24
#
#-------------------------------------------------

QT       += core gui webkitwidgets

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = web-lullaby
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    screensaver.cpp

HEADERS  += mainwindow.h \
    screensaver.h

FORMS    += mainwindow.ui \
    screensaver.ui

RESOURCES += \
    images.qrc
