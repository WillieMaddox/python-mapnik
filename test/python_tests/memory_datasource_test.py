# encoding: utf8
from nose.tools import eq_

import mapnik

from .utilities import run_all


def test_add_feature():
    md = mapnik.MemoryDatasource()
    eq_(md.num_features(), 0)
    context = mapnik.Context()
    context.push('foo')
    feature = mapnik.Feature(context, 1)
    feature['foo'] = 'bar'
    feature.geometry = mapnik.Geometry.from_wkt('POINT(2 3)')
    md.add_feature(feature)
    eq_(md.num_features(), 1)

    featureset = md.features_at_point(mapnik.Coord(2, 3))
    retrieved = []

    for feat in featureset.features:
        retrieved.append(feat)

    eq_(len(retrieved), 1)
    f = retrieved[0]
    eq_(f['foo'], 'bar')

    featureset = md.features_at_point(mapnik.Coord(20, 30))
    retrieved = []
    for feat in featureset.features:
        retrieved.append(feat)
    eq_(len(retrieved), 0)

if __name__ == "__main__":
    exit(run_all(eval(x) for x in dir() if x.startswith("test_")))
