# define the path to the data
datadir = '/Volumes/SD-Mac/alma_bhr71/2016.1.00391.S/science_goal.uid___A001_X88e_X1d/group.uid___A001_X88e_X1e/member.uid___A001_X88e_X1f/product/'
im_spw25 = datadir+'uid___A001_X88e_X1f.bhr71_sci.spw25.cube.I.pbcor.fits'
im_spw27 = datadir+'uid___A001_X88e_X1f.bhr71_sci.spw27.cube.I.pbcor.fits'
im_spw29 = datadir+'uid___A001_X88e_X1f.bhr71_sci.spw29.cube.I.pbcor.fits'
im_spw31 = datadir+'uid___A001_X88e_X1f.bhr71_sci.spw31.cube.I.pbcor.fits'
regionfile = '/Volumes/SD-Mac/alma_bhr71/cont_source.crtf'
logdir = '/Volumes/SD-Mac/alma_bhr71/'

# parse the region file
# region file contains, for each spw, one region without channel selection for extracting the whole spectrum,
# and several regions with a range of channels for the spectral line fitting.
# The ranges of channels are learned from the visual inspection with the CASA viewer.
regions = open(regionfile).readlines()
regions_dict = {}
for i, reg in enumerate(regions):
    if (reg[0] == '#') and ('spw' not in reg):
        continue
    elif (reg[0] == '#') and ('spw' in reg):
        regions_dict['spw'+reg.strip().split('spw')[1]] = []
        current_spw = 'spw'+reg.strip().split('spw')[1]
        continue
    regions_dict[current_spw].append(reg.strip())


# extract spectrum in the specified region, fitted with 2D Gaussian fit from the viewer
specflux(imagename=im_spw25, region=regionfile,logfile='/Volumes/SD-Mac/alma_bhr71/spw25_spectrum.txt')
