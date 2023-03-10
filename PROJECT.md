# Протоколы Git-a!

## 1. Локальный протокол.

* Базовый протоколом является ```Локальный протокол```, для которого удаленный репозиторий - это другой католог на диске.

### Достоинства.

* Приемущества основынных на файлах репозиторием в том, что они
просты и используют существующие разграничения прав на файлах и
сетевой доступю Если у вас есть общая файловая система, доступ к
которой имеет все команда, настройка репозитория очень проста.

* Так-же жто хорошая возмажность быстро получить наработки из
чьего-то рабочего репозитория.

### Недостатки.

* Недостаток этого метода в том, что общий доступ обычно сложнее
настроить и получить из разных мест, чем простой сетевой доступ.

* Недостаток этого метода в том, что общий доступ обычно сложнее
настроить и получить из разных мест, чем простой сетевой доступ.

* Наконец, этот протокол не защищает репозиторий от случайного
повреждения. Все пользователи имеют доступ к «удалённому» каталогу и
ничего не мешает изменению или удалению внутренних файлов Git и, как
следствие, повреждению репозитория.

## 2. Протокол http/s.

### Достоинства.

* Простота использования одного адреса URL для всех типов доступа и
аутентификации только при необходимости упрощает работу для конечного
пользователя. Возможность аутентификации посредством логина и пароля
также даёт преимущество перед SSH, так как пользователям перед
использованием не нужно создавать SSH-ключи и загружать публичный
ключ на сервер. Для неопытных пользователей или пользователей систем,
где SSH мало распространён, это большой плюс. Это также очень быстрый
и эффективный протокол, сравнимый с SSH.

Вы также можете предоставлять доступ к своим репозиториям только для
чтения по HTTPS, шифруя содержимое передачи; или вы можете зайти так
далеко, что клиенты будут использовать персональные подписанные
SSL-сертификаты.

Другой плюс в том, что HTTP/S очень распространённые протоколы и
корпоративные брандмауэры часто настроены для разрешения их работы.

### Недостатки.

* На некоторых серверах Git поверх HTTP/S может быть немного сложнее
в настройке по сравнению с SSH. Кроме этого, преимущества других
протоколов доступа к Git перед Умным HTTP незначительны.

## 3 Протокол SSH.

### Достоинства.

* SSH имеет множество достоинств. Во-первых, SSH достаточно легко 
настроить — демоны SSH распространены, многие системные администраторы 
имеют опыт работы с ними и во многих дистрибутивах они предустановлены 
или есть утилиты для управления ими. Далее, доступ по SSH безопасен — данные 
передаются зашифрованными по авторизованным каналам. Наконец, так же 
как и протоколы HTTP/S, Git и локальный протокол, SSH эффективен 
благодаря максимальному сжатию данных перед передачей.

### Недостатки. 

* Недостаток SSH в том, что, используя его, вы не можете обеспечить
анонимный доступ к репозиторию. Клиенты должны иметь доступ к машине
по SSH, даже для работы в режиме только на чтение, что делает SSH
неподходящим для проектов с открытым исходным кодом. Если вы
используете Git только внутри корпоративной сети, то, возможно,
SSH — единственный протокол, с которым вам придётся иметь дело. Если
же вам нужен анонимный доступ на чтение для своих проектов, придётся
настроить SSH для себя, чтобы выкладывать изменения, и что-нибудь
другое для других, для скачивания.

## 4 Протокол Git.

### Достоинства.

* Git-протокол ― часто самый быстрый из доступных протоколов. Если у
вас проект с публичным доступом и большой трафик, или у вас очень
большой проект, для которого не требуется аутентификация
пользователей для чтения, вам стоит настроить демон Git для вашего
проекта. Он использует тот же механизм передачи данных, что и
протокол SSH, но без дополнительных затрат на шифрование и
аутентификацию.

### Недостатки. 

* Недостатком Git-протокола является отсутствие аутентификации.
Поэтому обычно не следует использовать этот протокол как единственный
способ доступа к вашему проекту. Обычно он используется в паре с SSH
или HTTPS для нескольких разработчиков, имеющих доступ на запись,
тогда как все остальные используют git:// с доступом только на
чтение. Кроме того, это, вероятно, самый сложный для настройки
протокол. Вы должны запустить отдельный демон, для чего необходимо
дополнительно настраивать xinetd или systemd или им подобные, что не
всегда легко сделать. Также необходимо, чтобы сетевой экран позволял
доступ на порт 9418, который не относится к стандартным портам,
всегда разрешённым в корпоративных брандмауэрах. За сетевыми экранами
крупных корпораций этот неизвестный порт часто заблокирован.

4.2 Git на сервере. 
