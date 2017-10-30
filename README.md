plex-seedbox-server
=========

This role will install all these applications in a Ubuntu-16.04 server:

  * [plexmediaserver](https://www.plex.tv/downloads/)
  * [transmission-daemon](https://transmissionbt.com/)
  * [plexdrive](https://github.com/dweidenfeld/plexdrive)
  * [rclone](https://rclone.org/)
  * [plexpy](https://github.com/JonnyWong16/plexpy)
  * [sickrage](https://sickrage.github.io/)
  * [x2go-server](https://wiki.x2go.org/)
  * [mate-desktop](https://mate-desktop.org/)

A dedicated user is added to the server (e.g. "seedboxuser") and all daemons (plexpy, sickrage, transmission-daemon) will run as this user.

Few folders are created in the home folder of the seedbox user:

 * $HOME/torrents/temp
 * $HOME/torrents/completed
 * $HOME/plexdrive (to mount plexdrive)
 * $HOME/.plexdrive (to store plexdrive config)

By default Mate and X2Go won't be installed unless you define "install_x2go_and_mate: True"


Role Variables
--------------

* `seedbox_user: "seedboxuser"`
* `seedbox_user_pass: "pass_hash"`     [how to generate crypted pass](http://docs.ansible.com/ansible/latest/faq.html#how-do-i-generate-crypted-passwords-for-the-user-module)
* `plexmediaserver_version: "1.9.4.4325-1bf240a65"`
* `plexdrive_version: "latest"`
* `plexdrive_client_id: "AAAAAAAAAAAAAAAAAA.apps.googleusercontent.com"`
* `plexdrive_client_secret: "adsfadfadfadfadfadfasdf"`
* `rclone_version: "latest"`
* `plexpy_version: "latest"`
* `sickrage_version: "v2017.06.05-1"`   (defining a sickrage version is mandatory. I don't know why I cannot query latest release in https://api.github.com/repos/SickRage/SickRage/releases/latest ?)
* `install_x2go_and_mate: False`

Check available versions in these urls:
 * [plexmediaserver](https://www.plex.tv/es/downloads/)
 * [plexdrive](https://github.com/dweidenfeld/plexdrive/releases)
 * [rclone](https://github.com/ncw/rclone/releases)
 * [plexpy](https://github.com/JonnyWong16/plexpy/releases)
 * [sickrage](https://github.com/SickRage/SickRage/releases)

Check here [how to generate your client-id for plexdrive](https://rclone.org/drive/#making-your-own-client-id) 

Dependencies
------------

none

Requirements
------------

none

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: plex-seedbox-server,
             plexmediaserver_version: "1.9.4.4325-1bf240a65",
             plexdrive_client_id: "AAAAAAAAAAAAAAAAAA.apps.googleusercontent.com",
             plexdrive_client_secret: "adsfadfadfadfadfadfasdf" }

License
-------

GPLv3

Author Information
------------------

Pablo Escobar - https://github.com/pescobar
