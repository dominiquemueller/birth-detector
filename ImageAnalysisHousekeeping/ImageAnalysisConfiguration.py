#!/usr/bin/env python3
#-*- coding: utf-8 -*-



#==========================================================================
# ImageAnalysisConfiguration.py – DESCRIPTIONS 
#==========================================================================

"""
@author: Dominique Müller <Dominique Müller <dominiquepeter.mueller@students.bfh.ch>
"""


#==========================================================================
# IMPORT DECLARATIONS
#==========================================================================

import sys
sys.path.append('../VO-Library')
sys.path.append('../Testdata')
sys.path.append('../Testresults')


## Import Value Objects
import HSV
import BGR
import ColorRange





#=====================================================================================================================
#=====================================================================================================================
#
# IMPPORTANT NOTES
#
# this part of the configuration is highly important and influences the results of the analysis a lot! 
# this configuration part is quite specific to images. it is based on the position of the cow in the stable
# and the lightning and brightness quality of the image
#==========================================================================


#Filepath and Filename for the Image Reader

READER_FILE_PATH = '../Testdata/'
# reader file name without extension. by default extension is jpg, other confifuration can be provided below.
READER_FILE_NAME = '5'




# AdvancedUnimportantColorRange  defines, whether you already know, which areas of the image can be considered
# to be unimportant. Knowing that, the Image Analysis will provide better results. If you do not do not have 
# this knowledge, the corresponding variable needs to set to False. In any case, the information, that the light bulb
# is at the very bright position will be used, because this is a quite generic Information.
ADVANCED_UNIMPORTANT_COLOR_RANGE = True

# if the cow is only able to laying straight in the box, set FILTER_BY_ANGLE to True. 
# If the cow is lying next to an empty box and therefore able to lying anyhow, set FILTER_BY_ANGLE to false
FILTER_BY_ANGLE = True



# If you now which areas of the image are not important, do the following_
    # 1. Define Lower and upper Bound in HSV Color Space
    # 2. Create a Color Range Object with the lower and upper Bound in Stept 1.
    # 3. Add the Color Range Object to the list additionalUnimportantColorRanges
    # 4. Be Patient And  Have Fun!
    
# light (HSV) Bounds
LOWER_BOUND_LIGHT_FLIMMERING= HSV.HSV(hue=0, saturation=0, value=100)
UPPER_BOUND_LIGHT_FLIMMERING= HSV.HSV(hue=360, saturation=100, value=255)
      
LOWER_BOUND_LIGHT= HSV.HSV(hue=0, saturation=0, value=140)
UPPER_BOUND_LIGHT= HSV.HSV(hue=360, saturation=100, value=255)
                     
#floor (HSV) 
LOWER_BOUND_FLOOR= HSV.HSV(hue=0, saturation=0, value=0) 
UPPER_BOUND_FLOOR = HSV.HSV(hue=360, saturation=100, value=90)

#Straw (HSV) 
LOWER_BOUND_STRAW= HSV.HSV(hue=0, saturation=138, value=0) 
UPPER_BOUND_STRAW = HSV.HSV(hue=360, saturation=1000, value=2000)

# Color Ranges
lightColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_LIGHT, upperBound=UPPER_BOUND_LIGHT )
lightFlimmeringColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_LIGHT, upperBound=UPPER_BOUND_LIGHT )
floorColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_FLOOR, upperBound=UPPER_BOUND_FLOOR )
strawColorRange = ColorRange.ColorRange(lowerBound = LOWER_BOUND_STRAW, upperBound=UPPER_BOUND_STRAW )


defaultColorRanges = [lightColorRange]
additionalUnimportantColorRanges = [floorColorRange ]



#=====================================================================================================================
#=====================================================================================================================


#==========================================================================
# FURTHER CONFIGURATION OF THE IMAGE ANALYSIS CONTROLLER
# this part of the configuration is more generic and does not really depend 
# on the current analysed image.
#==========================================================================

#configuration for angle filtering
LIGHT_BULB_ANGLE_EXPECTION= 90
MIN_LEG_ANGLE_EXPECTION= 70
MAX_LEG_ANGLE_EXPECTION= 110

# Scale for rotated image
SCALE = 0.75

# determines, how many lateral lying contours are necessary to make prediction
MIN_NUMBER_LYING_CONTOURS = 2
MIN_NUMBER_STANDING_CONTOURS = 1
## configuration for shape analysis
ROUNDNESS_THRESHOLD = 0.7
EXTENT_MAX = 0.5
ASPECT_RATIO_MIN = 1.5
ANKER_ANGLE = 300
SIMILARITY_MAX= 15

# value from 1 to 3
MATCHING_METHOD = 1

#============================================
###### IMAGE READER CONFIGURATION ######
#============================================

#Mimetype Information for Image Reader 
READER_MAJOR = 'image'
READER_MINOR = 'jpeg'
READER_EXTENSION = 'jpg' 

#============================================
###### IMAGE WRITER CONFIGURATION ######
#============================================
   
#Mimetype Information for Image Writer 
WRITER_MAJOR = 'image'
WRITER_MINOR = 'jpeg'
WRITER_EXTENSION = 'jpg'

# Prepare FilePaths to write . 
WRITER_FILE_PATH_MAIN = '../Testresults/'

# Prepare FileNames to write . 
WRITER_FILE_NAME_BRIGHTENED = '1originalImage'
WRITER_FILE_NAME_FILTERED = '2filteredImage'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_MASK = '3unimportantAreaMask'
WRITER_FILE_NAME_UNIMPORTANT_AREAS_IMAGE = '4unimportantAreaimage'
WRITER_FILE_NAME_THRESHOLDED_MASK = '5thresholdedMask'
WRITER_FILE_NAME_THRESHOLDED_IMAGE = '6ContoursAfterThresholding'
WRITER_FILE_NAME_ANGLE_DEMO = '99AngleAdjustmentDemonstration'


#==========================================================================
# INFORMATION AND CONFIGURATION FOR IMAGE PROCESSOR
#==========================================================================


#============================================
###### BRIGHTENING CONFIGURATION ######
#============================================
   
# Brighten Configuration #
# PAY ATTENTION: FOR inRange() FUNCTION, IT IS CHANGING RESULTS HEAVILY AFTER BRIGHTENING
# THEREFORE, BRIGHTENING SHOULD BE DEACTIVATED BEFORE PERFORMING inRange(). 
# This influences many parts of the Application. Tresholding results are better after brightening.

BRIGHTENING_IMAGE_TRUE = True
BRIGHTENING_IMAGE_FALSE = False
BRIGHTENER_FACTOR = 60
EQUALIZING_IMAGE_TRUE = True
EQUALIZING_IMAGE_FALSE = False
CLIP_LIMIT = 4.0

## Equalizing Type
'''
    Possible Values for  ENUM_SELECT_EQUALIZING:
    - 1 corresponds to CLAHE

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_EQUALIZING = 1 #CLAHE



# Color Space Conversion Configuration #
CONVERTING_IMAGE = True
## Converting Type
'''
    Possible Values for  ENUM_SELECT_FILTERING:
    - 1 corresponds to COLOR_BGR2GRAY  
    - 2 corresponds to COLOR_BGR2HSV 
    - 3 corresponds to COLOR_HSV2BGR
    - 4 corresponds to COLOR_GRAY2BGR 
    - 5 corresponds to COLOR_BGR2YUV 
    - 6 corresponds to COLOR_YUV2BGR 

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_CONVERTING_BGR2GRAY = 1 #COLOR_BGR2GRAY
ENUM_SELECT_CONVERTING_BGR2HSV = 2




#============================================
###### FILTERING CONFIGURATION ######
#============================================ 
FILTER_NAME = 'GAUSSIANBLUR'
FILTERING_IMAGE = True
KERNEL_WIDTH = 9
KERNEL_LENGTH = 9

## Filtering Type
'''
    Possible Values for  ENUM_SELECT_FILTERING:
    - 1 corresponds to GAUSSIANBLUR

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_FILTERING = 1 #GAUSSIANBLUR  


#============================================
###### THRESHOLDING CONFIGURATION ######
#============================================

SIMPLE_THRESHOLD_NAME = 'cv2.THRESHOLD'
ADAPTIVE_THRESHOLD_NAME = 'cv2.ADAPTIVE_THRESHOLD'

THRESHOLDING_IMAGE = True
MAXIMUM_VALUE = 255 # value between 0 and 255 possible
THRESHOLD =90

## Thresholding Method Enumeration
'''
    Possible Values for  ENUM_SELECT_METHOD:
    - 1 corresponds to cv2.THRESHOLD
    - 2 corresponds to cv2.ADAPTIVE_THRESHOLD
    

    Any other Values are not allowed and end up with an error message. 
'''
ENUM_SELECT_METHOD = 1

 
# Thresholding Type Enumeration
'''
    Possible Values for  ENUM_SELECT_TYPE:
    - 1 corresponds to THRESH_BINARY
    - 2 corresponds to THRESH_BINARY_INV
    - 3 corresponds to THRESH_TRUNC
    - 4 corresponds to THRESH_TOZERO
    - 5 corresponds to THRESH_TOZERO_INV
    - 6 corresponds to THRESH_BINARY_AND_THRESH_OTSU 
    - 7 corresponds to THRESH_BINARY_AND_THRESH_TRIANGLE
    

    Any other Values are not allowed and end up with an error message.
    PLEASE NOTE: For adaptive Thresholding only THRESH_BINARY and THRESH_BINARY_INV are available
'''
ENUM_SELECT_TYPE = 1

#adaptive Thresholding Configuration
BLOCK_SIZE = 11
C_SUBTRACTOR = 3

'''
    Possible Values for  ENUM_SELECT_ADAPTIVE_THRESHOLDING:
    - 1 corresponds to ADAPTIVE_THRESH_MEAN_C
    - 2 corresponds to ADAPTIVE_THRESH_GAUSSIAN_C     

    Any other Values are not allowed and end up with an error message. 
''' 
ENUM_SELECT_ADAPTIVE_THRESHOLDING = 1





#============================================
###### IMPORTANT AREAS CONFIGURATION ######
#============================================

# Important Areas Configuration

#============================================
###### CONTOUR FINDER CONFIGURATION ######
#============================================

MIN_AREA = 1250
MIN_AREA_BIG = 2000

DELETE_CIRCLES_TRUE = True
DELETE_CIRCLES_FALSE = False


'''
    Possible Values for  ENUM_SELECT_APPROX:
    - 1 corresponds to CHAIN_APPROX_NONE
    - 2 corresponds to CHAIN_APPROX_SIMPLE
    - 3 corresponds to CHAIN_APPROX_TC89_L1
    - 4 corresponds to CHAIN_APPROX_TC89_KCOS

    

    Any other Values are not allowed and end up with an error message. 
'''
    
ENUM_SELECT_APPROX = 1

'''
    Possible Values for  ENUM_SELECT_FINDER:
    - 1 corresponds to RETR_EXTERNAL
    - 2 corresponds to RETR_LIST
    - 3 corresponds to RETR_CCOMP
    - 4 corresponds to RETR_TREE
    - 5 corresponds to RETR_FLOODFILL

        = 1

    Any other Values are not allowed and end up with an error message. 
'''
    
ENUM_SELECT_FINDER = 1



#============================================
###### CONTOUR DRAWER CONFIGURATION ######
#============================================

CIRCLE_DRAWING_MODE = 'CIRCLE'
OUTLINE_DRAWING_MODE = 'OUTLINE'
POINTS_DRAWING_MODE = 'POINTS'


THICKNESS_FILL = -1
THICKNESS_BOLD = 10
THICKNESS_THICK = 5
THICKNESS_THIN = 2



RED = BGR.BGR(blue=0, green=0, red=250)
BLUE= BGR.BGR(blue=255, green=0, red=0)
GREEN= BGR.BGR(blue=120, green=200, red=120)
BLACK= BGR.BGR(blue=0, green=0, red=0)


#============================================
###### TRAIT RECOGNITOR CONFIGURATION ######
#============================================

CONTOUR_NAME_STANDING = 'standingContours'
CONTOUR_NAME_LATERAL_LYING = 'lateralLyingContours'

TRAIT_RECOGNITOR_TITLE = '############ RESULT OF THE TRAIT RECOGNITOR ############'
NEWLINE = '\n'

INFORMATION_MSG_NO_COW = 'NO COW DETECTED IN THIS IMAGE. '
INFORMATION_MSG_LATERAL_LYING_COW= 'IT APPEARS, THAT THE COW IS IN LATERAL LYING POSITION. CHECK THE CAMERA!'
INFORMATION_MSG_STANDING_COW = 'IT APPEARS, THAT THE COW IS STANDING. PLEASE STAY PATIENT AND HANG ON!'
INFORMATION_MSG_STANDING_COW_OR_NO_COW = 'ITS NOT SURE: EITHER THE COW IS STANDING OR NO COW IS DETECTED.'
