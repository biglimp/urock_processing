from builtins import str
# This file prints out run information used for each specific run
from time import strftime


def writeRunInfo(folderPath, build_file, veg_file, attenuationVeg):

    # with open(folderPath + '/RunInfoSOLWEIG.txt', 'w') as file:           	#FO#
    #FO#
    with open(folderPath + '/RunInfoURock.txt', 'w') as file:
        file.write('This file provides run settings for the URock run initiated at: ' + strftime("%a, %d %b %Y %H:%M:%S"))
        file.write('\n')
        file.write('\n')
        file.write('Version: ' + 'URock v1.0.1')
        file.write('\n')
        file.write('\n')
        file.write('SURFACE DATA')
        file.write('\n')
        if build_file is not None:
            file.write('Building layer: ' + build_file)
            file.write('\n')
            #TODO: More info?
        else:
            file.write('No building data used')
            file.write('\n')
        
        if veg_file is not None:
            file.write('Vegetation layer: ' + veg_file)
            file.write('\n')
            file.write('Attenuation though vegetation: ' + attenuationVeg)
            file.write('\n')
        else:
            file.write('No vegetation data used')
            file.write('\n')

        file.write('\n')
        file.write('METEOROLOGICAL FORCING DATA')
        file.write('\n')
        #TODO: Add more info

        file.write('\n')
        file.close()
        # if metfileexist == 1:
        #     file.write('Meteorological file: ' + filePath_metfile)
        #     file.write('\n')
        #     if onlyglobal == 1:
        #         file.write('Diffuse and direct shortwave radiation estimated from global radiation')
        #         file.write('\n')
        # else:
        #     file.write('Meteorological file not used')
        #     file.write('\n')							#FO# ' ' -> file.write('\n')
        #     file.write('Year: ' + str(metdata[0, 0]))
        #     file.write('\n')
        #     file.write('Day of Year: ' + str(metdata[0, 1]))
        #     file.write('\n')
        #     file.write('Hour: ' + str(metdata[0, 2]))
        #     file.write('\n')
        #     file.write('Minute: ' + str(metdata[0, 3]))
        #     file.write('\n')
        #     file.write('Air temperature: ' + str(metdata[0, 11]))	#FO# Ait -> Air
        #     file.write('\n')
        #     file.write('Relative humidity: ' + str(metdata[0, 10]))
        #     file.write('\n')
        #     file.write('Global radiation: ' + str(metdata[0, 14]))
        #     file.write('\n')
        #     file.write('Diffuse radiation: ' + str(metdata[0, 21]))
        #     file.write('\n')
        #     file.write('Direct radiation: ' + str(metdata[0, 22]))
        #     file.write('\n')

        # file.write('\n')
        # file.write('ENVIRONMENTAL PARAMETERS')
        # file.write('\n')
        # file.write('Albedo of walls: ' + str(albedo_b))
        # file.write('\n')
        # file.write('Albedo of ground (not used if land cover scheme is active): ' + str(albedo_g))
        # file.write('\n')
        # file.write('Emissivity (walls): ' + str(ewall))
        # file.write('\n')
        # file.write('Emissivity of ground (not used if land cover scheme is active): ' + str(eground))
        # file.write('\n')
        # file.write('\n')
        # file.write('ADDITIONAL SETTINGS')
        # file.write('\n')
        # if elvis == 1:
        #     file.write('Sky emissivity adjusted according to Jonsson et al. (2005)')
        #     file.write('\n')
        # if cyl == 1:
        #     file.write('Human considered as a standing cylinder')	#FO# '' -> standing
        # else:
        #     file.write('Human considered as a standing cube')
        # file.write('\n')
        # if ani == 1:
        #     file.write('Anisotropic sky diffuse shortwave (Perez et al. 1993) and longwave (Martin & Berdahl, 1984) radiation')
        # else:
        #     file.write('Isotropic sky')
        # file.write('\n')
        # file.close()
