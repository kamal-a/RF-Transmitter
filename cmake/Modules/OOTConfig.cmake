INCLUDE(FindPkgConfig)
PKG_CHECK_MODULES(PC_OOT OOT)

FIND_PATH(
    OOT_INCLUDE_DIRS
    NAMES OOT/api.h
    HINTS $ENV{OOT_DIR}/include
        ${PC_OOT_INCLUDEDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/include
          /usr/local/include
          /usr/include
)

FIND_LIBRARY(
    OOT_LIBRARIES
    NAMES gnuradio-OOT
    HINTS $ENV{OOT_DIR}/lib
        ${PC_OOT_LIBDIR}
    PATHS ${CMAKE_INSTALL_PREFIX}/lib
          ${CMAKE_INSTALL_PREFIX}/lib64
          /usr/local/lib
          /usr/local/lib64
          /usr/lib
          /usr/lib64
)

INCLUDE(FindPackageHandleStandardArgs)
FIND_PACKAGE_HANDLE_STANDARD_ARGS(OOT DEFAULT_MSG OOT_LIBRARIES OOT_INCLUDE_DIRS)
MARK_AS_ADVANCED(OOT_LIBRARIES OOT_INCLUDE_DIRS)

