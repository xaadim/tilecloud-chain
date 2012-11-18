# -*- coding: utf-8 -*-

from testfixtures import log_capture

from tilecloud_chain.tests import CompareCase
from tilecloud_chain import controller, TileGeneration


class TestError(CompareCase):

    @log_capture()
    def test_resolution(self, l):
        self.run_cmd(
            './buildout/bin/generate_controller -c tilegeneration/wrong_resolutions.yaml',
            controller.main)
        l.check(
            ('tilecloud_chain', 'ERROR', "The reolution 0.1 * resolution_scale 5 is not an integer."),
            ('tilecloud_chain.tests', 'INFO', ''),
            ('tilecloud_chain.tests', 'INFO', ''),
        )

    @log_capture()
    def test_mapnik_grid_meta(self, l):
        self.run_cmd(
            './buildout/bin/generate_controller -c tilegeneration/wrong_mapnik_grid_meta.yaml',
            controller.main)
        l.check(
            ('tilecloud_chain', 'ERROR', "The layer 'b' is of type Mapnik/Grid, that can't support matatiles."),
            ('tilecloud_chain.tests', 'INFO', ''),
            ('tilecloud_chain.tests', 'INFO', ''),
        )

    @log_capture()
    def test_exists(self, l):
        self.run_cmd(
            './buildout/bin/generate_controller -c tilegeneration/wrong_exists.yaml',
            controller.main)
        l.check(
            ('tilecloud_chain', 'ERROR', "The attribute 'grids' is required in the object config."),
            ('tilecloud_chain.tests', 'INFO', ''),
            ('tilecloud_chain.tests', 'INFO', ''),
        )

    @log_capture()
    def test_type(self, l):
        self.run_cmd(
            './buildout/bin/generate_controller -v -c tilegeneration/wrong_type.yaml',
            controller.main)
        l.check(
            ('tilecloud_chain', 'ERROR', "The attribute 'resolutions' is required in the object grid[swissgrid_3]."),
            ('tilecloud_chain', 'ERROR', "The attribute 'bbox' is required in the object grid[swissgrid_3]."),
            ('tilecloud_chain', 'ERROR', "The attribute 'srs' is required in the object grid[swissgrid_3]."),
            ('tilecloud_chain', 'ERROR', "The attribute 'resolution_scale' of the object grid[swissgrid_2] "
                "is not a <type 'int'>."),
            ('tilecloud_chain', 'ERROR', "The attribute 'bbox' of the object grid[swissgrid_2] "
                "has an element who is not a right float expression: a."),
            ('tilecloud_chain', 'ERROR', "The attribute 'srs' of the object grid[swissgrid_2] is not a <type 'str'>."),
            ('tilecloud_chain', 'ERROR', "The attribute 'bbox' of the object grid[swissgrid_1] is not an array."),
            ('tilecloud_chain', 'ERROR', "The attribute 'srs' of the object grid[swissgrid_1] is not a <type 'str'>."),
            ('tilecloud_chain.tests', 'INFO', ''),
            ('tilecloud_chain.tests', 'INFO', ''),
        )

    def test_validate_type(self):
        class Opt:
            verbose = False
            test = 0
        gene = TileGeneration('tilegeneration/test.yaml', Opt())
        obj = {'value': 1}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), False)
        self.assertEquals(obj['value'],  1)

        obj = {'value': 1.0}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), True)

        obj = {'value': '1 + 1'}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), False)
        self.assertEquals(obj['value'],  2)

        obj = {'value': '1 * 1.5'}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), False)
        self.assertEquals(obj['value'],  2)

        obj = {'value': 'a'}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), True)

        obj = {'value': {}}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), True)

        obj = {'value': []}
        self.assertEquals(gene.validate(obj, 'object', 'value', int), True)

        obj = {'value': 1}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), False)
        self.assertEquals(obj['value'],  1.0)

        obj = {'value': 1.0}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), False)
        self.assertEquals(obj['value'],  1.0)

        obj = {'value': '1 + 1'}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), False)
        self.assertEquals(obj['value'],  2.0)

        obj = {'value': '1 * 1.5'}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), False)
        self.assertEquals(obj['value'],  1.5)

        obj = {'value': 'a'}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), True)

        obj = {'value': {}}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), True)

        obj = {'value': []}
        self.assertEquals(gene.validate(obj, 'object', 'value', float), True)
