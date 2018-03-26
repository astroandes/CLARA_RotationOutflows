The emission line galaxy catalogue consists of two tables: A catalogue
of all 831 detected emission line objects and a table of all 1652
detected emission lines in those objects.  These tables are described
in detail in Sect. 4.1 and 4.2 of the paper.  Both tables are in the
FITS binary table format, adhering to the FITS standard described in
Pence et al. (2010).

The object table MW_1-24_main_table.fits contains the following
columns:

(1) UNIQUE_ID: Unique MUSE-Wide object ID.
(2) RA: Right Ascension (J2000) in degrees
(3) DEC: Declination (J2000) in degrees
(4) Z: Redshift of the source
(5) Z_ERR: Error on the determined redshift
(6) LEAD_LINE: Highest S/N detected line
(7) SN: S/N of the lead line (abbreviations according to Table 5 in the paper)
(8) QUALITY: Quality flag (see Sect. 3.2 of the paper)
(9) CONFIDENCE: Confidence value (see Sect. 3.2 of the paper)
(10) OTHER_LINES: Other detected lines in that source
(11) GUO_ID: Associated source in the Guo et al. (2013) photometric
             catalogue
(12) GUO_SEP: Angular separation (in arcsec) to the Guo et al. (2013)
              source
(13) SKELTON_ID: Associated source in the Skelton et al. (2014)
                 photometric catalogue
(14) SKELTON_SEP: Angular separation (in arcsec) to the Skelton et al.
                  (2014) source

The emission line table MW_1-24_emline_table.fits contains the columns:

(1) UNIQUE_ID: Unique MUSE-Wide object ID (to establish link to the
               object table)
(2) POINTING_ID: MUSE-Wide Pointing ID (see Fig. 1 in paper)
(3) OBJ_ID: Object ID (only unique per pointing)
(4) RID: Running ID (only unique per pointing)
(5) IDENT: Line identification (abbreviations according to Table 5 in the
           paper)
(6) COMMENT: Free form comment, added during classifications and cleaning.
             (see Sect. 3.2 in the paper)
(7) SN: Detection significance
(8,9,10): RA_SN, DEC_SN, LAMBDA_SN: 3D S/N weighted emission line position
          in datacube (right ascension and declination J2000 degrees and
	      air wavelength in Angstrom).
(11,12,13): RA_PEAK_SN, DEC_PEAK_SN, LAMBDA_PEAK_SN: 3D S/N peak emission
            line position in data cube (right ascension and declination
		J2000 degrees and air wavelength in Angstrom).
(14,15): RA_1MOM, DEC_1MOM: First central moment position of emission line
         (right ascension and declination J2000 degrees - see Sect. 3.3 in
	     the paper)
(16,17,18,19): F_KRON, F_2KRON, F_3KRON, F_4KRON: Emission line flux
               extracted in k*Kron (Kron 1980) radii apertures
		   (in 10**(-20)erg/s/cm^2)
(20,21,22,23): F_KRON_ERR, F_2KRON_ERR, F_3KRON_ERR, F_4_KRON_ERR:
		   Errors on column 16-19 (in 10**(-20)erg/s/cm^2)
(24): BORDER_FLAG: Flag indicating whether 3*R_KRON overlaps with pointing
      border.

In addition we also provide 1D spectra and 3D source datacubes for
all 831 detected sources.  These data products are described in detail
in Sects. 4.3 and 4.4 of the paper.

The 1D spectra are in the sub-directory 1d_spectra and have the
filenames spectrum_IIIIIIIII.fits, where IIIIIIIII refers to the
objects MUSE-Wide UNIQUE_ID.

The 1D spectra are provided as FITS binary tables (Pence et al. 2010)
with 4 columns:
(1) WAVE_AIR: Air wavelength (in Angstrom).
(2) WAVE_VAC: Vacuum wavelength (in Angstrom). Converted from air 
    wavelength with the formula used in the Vienna atomic line database
	(Ryabchikova et al. 2015):
	http://www.astro.uu.se/valdwiki/Air-to-vacuum\%20conversion
(3) FLUX: Flux density for a given wavelength bin
    (in 10**(-20)erg/s/cm**2/Angstrom)
(4) FLUX_ERR: Error on the flux density in column (3)
    (in 10**(-20)erg/s/cm**2/Angstrom)

The 3D source datacubes are in the sub-directory 3d_source_cubes,
with filenames IIIIIIIII_objcube.fits, where IIIIIIIII refers to
the objects MUSE-Wide UNIQUE_ID.  These FITS files consist of 3
header-data units, with correct world-coordinates included in each
header following the conventions given in Calabretta & Greisen
(2002), Greisen & Calabretta (2002), and Greisen et al. (2006).

(HDU 1): A datacube of dimensions a*b*3680, where a and b are the spatial
         dimensions matched to the objects extent, and 3680 is the spectral
	     dimension. Each volume pixel stores the flux density
	     in 10**(-20)erg/s/cm**2/Angstrom.
(HDU 2): A vector of length 3680 storing the variance for each wavelength
         layer in the datacube.
(HDU 3): An array of dimensions a*b storing the amount of MUSE exposures
         that went into each spectral pixel of the datacube.

References:

    Calabretta & Greisen 2002, A&A, 395, 1077 - 2002A%26A...395.1077C
    Guo et al. 2013, ApJS, 207, 24 - 2013ApJS..207...24G
    Greisen & Calabretta 2002, A&A, 395, 1061 - 2002A%26A...395.1061G
    Greisen et al. 2006, A&A, 446, 747 - 2006A%26A...446..747G
    Kron 1980, ApJS, 43, 305 - 1980ApJS...43..305K
    Pence et al. 2010, A&A, 524, A42 - 2010A%26A...524A..42P
    Skelton et al. 2014, ApJS, 214, 24 - 2014ApJS..214...24S
