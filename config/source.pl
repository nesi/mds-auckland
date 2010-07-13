# These directories are created by install_mip
mipdir     => '/usr/local/mip',
moduledir  => '/usr/local/mip/modules',
configdir  => '/usr/local/mip/config',

# Packages are ordered in terms of priority
#     left - lowest priority
#     right - highest priority
pkgs       => ['default','er171'],
#pkgs       => ['er171'],

# Default producer to use
producer   => 'glue',
