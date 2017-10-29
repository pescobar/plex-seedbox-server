import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_plex_installed(host):
    assert host.package('plexmediaserver').is_installed


def test_plexmediaserver_running_and_enabled(host):
    plexmediaserver = host.service("plexmediaserver")
    assert plexmediaserver.is_running
    assert plexmediaserver.is_enabled


def test_plexmediaserver_listen(host):
    assert host.socket('tcp://0.0.0.0:32400').is_listening


def test_transmission_running_and_enabled(host):
    transmission = host.service("transmission-daemon")
    assert transmission.is_running
    assert transmission.is_enabled


def test_plexpy_listen(host):
    assert host.socket('tcp://0.0.0.0:8181').is_listening


def test_sickrage_listen(host):
    assert host.socket('tcp://0.0.0.0:8081').is_listening


def test_rclone_binary(host):
    f = host.file('/usr/local/bin/rclone')

    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0755'


def test_plexdrive_binary(host):
    f = host.file('/usr/local/bin/plexdrive')

    assert f.exists
    assert f.is_file
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0755'
