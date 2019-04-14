# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import mock


from config import Config



ADDONS_SETTINGS = {
    'plugin.video.catchuptvandmore': Config.get('addon_settings'),
    'script.module.codequick': Config.get('codequick_fake_settings'),
    'script.module.inputstreamhelper': Config.get('inputstreamhelper_fake_settings')
}


ADDONS_LABELS = {
    'plugin.video.catchuptvandmore': Config.get('addon_labels'),
    'script.module.codequick': Config.get('codequick_labels'),
    'script.module.inputstreamhelper': Config.get('inputstreamhelper_labels')
}


ADDONS_NAMES = {
    'plugin.video.catchuptvandmore': 'Catch-up TV & More',
    'script.module.codequick': 'CodeQuick',
    'script.module.inputstreamhelper': 'InputStream Helper'
}


ADDONS_PATHS = {
    'plugin.video.catchuptvandmore': Config.get('addon_path'),
    'script.module.codequick': Config.get('codequick_addon_path'),
    'script.module.inputstreamhelper': Config.get('inputstreamhelper_addon_path')
}

ADDONS_FANARTS = {
    'plugin.video.catchuptvandmore': Config.get('addon_fanart_filepath'),
    'script.module.codequick': Config.get('codequick_fanart_filepath'),
    'script.module.inputstreamhelper': Config.get('inputstreamhelper_fanart_filepath')
}

ADDONS_ICONS = {
    'plugin.video.catchuptvandmore': Config.get('addon_icon_filepath'),
    'script.module.codequick': Config.get('codequick_icon_filepath'),
    'script.module.inputstreamhelper': Config.get('inputstreamhelper_icon_filepath')
}


class FakeAddon(object):
    def __init__(self, id='plugin.video.catchuptvandmore'):
        self._id = id
        self._settings = ADDONS_SETTINGS[self._id]
        self._labels = ADDONS_LABELS[self._id]
        self._name = ADDONS_NAMES[self._id]
        self._path = ADDONS_PATHS[self._id]
        self._fanart = ADDONS_FANARTS[self._id]
        self._icon = ADDONS_ICONS[self._id]

    def getAddonInfo(self, info_id):
        result = ''
        if info_id == 'id':
            result = self._id
        elif info_id == 'name':
            result = self._name
        elif info_id == 'path':
            result = self._path
        elif info_id == 'fanart':
            result = self._fanart
        elif info_id == 'icon':
            result = self._icon
        elif info_id == 'profile':
            result = Config.get('userdata_path')
        else:
            raise Exception(
                'Need to complete getAddonInfo mock for info_id: {}'.format(info_id))

        if not Config.get('disable_xbmcaddon_mock_log'):
            print('[FakeAddon] getAddonInfo of "{}" --> "{}"'.format(info_id, result))
        return result

    def getSetting(self, setting_id):
        if setting_id not in self._settings:
            print('[FakeAddon] Missing setting_id "{}" in ADDON_FAKE_SETTINGS (config.py)'.format(setting_id))
            exit(-1)
        if not Config.get('disable_xbmcaddon_mock_log'):
            print('[FakeAddon] getSetting of "{}" --> "{}"'.format(setting_id, self._settings.get(setting_id)))
        return self._settings.get(setting_id, '')

    def setSetting(self, _id, value):
        if not Config.get('disable_xbmcaddon_mock_log'):
            print('[FakeAddon] setSetting of "{}" --> "{}"'.format(_id, value))
        self._settings[_id] = value

    def getLocalizedString(self, _id):
        if not Config.get('disable_xbmcaddon_mock_log'):
            print('[FakeAddon] getLocalizedString of "{}" --> "{}"'.format(_id, self._labels.get(id)))
        return self._labels.get(_id, str(_id))


mock_xbmcaddon = mock.MagicMock()

mock_xbmcaddon.Addon.side_effect = FakeAddon

# Say to Python that the xbmcaddon module is mock_xbmcaddon
sys.modules['xbmcaddon'] = mock_xbmcaddon