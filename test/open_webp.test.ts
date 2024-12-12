import * as gdal from 'gdal-async'
import { expect } from 'chai'
import * as path from 'path'
import { runGC } from './_hooks'

describe('Open WebP', () => {
  afterEach(runGC)

  it('should open WebP format', () => {
    const filename = path.join(__dirname, 'data/test_webp_js.webp')
    const ds = gdal.open(filename)
    expect(ds).to.be.instanceOf(gdal.Dataset)
    expect(ds.rasterSize).to.have.property('x')
    expect(ds.rasterSize).to.have.property('y')
    expect(ds.driver.description).to.equal('WEBP')
  })

  it('should list WebP driver', () => {
    const drivers = gdal.drivers.getNames()
    expect(drivers).to.include('WEBP')
  })
})
