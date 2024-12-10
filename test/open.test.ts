import * as gdal from 'gdal-async'
import * as path from 'path'
import * as assert from 'assert'
import * as semver from 'semver'
import { runGC } from './_hooks'

describe('Open', () => {
  afterEach(runGC)

  it('should throw when invalid file', () => {
    const filename = path.join(__dirname, 'data/invalid')
    assert.throws(() => {
      gdal.open(filename)
    }, semver.gte(gdal.version, '3.0.0') ? /not recognized.*supported file format/ : /Error/)
  })
  it('should throw when non-existing file', () => {
    const filename = path.join(__dirname, 'data/inexisting')
    assert.throws(() => {
      gdal.open(filename)
    }, semver.gte(gdal.version, '3.0.0') ? /No such file or directory/ : /Error/)
  })
})
