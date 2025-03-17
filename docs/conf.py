"""sphinx-ifelse documentation build configuration file"""

import datetime
import os

from typing import Dict, List, Tuple

from sphinx import __version__ as sphinx_version
print ('sphinx version: ' + str(sphinx_version))

from sphinx_ifelse import __version__ as sphinx_ifelse_version
print ('sphinx_ifelse version: ' + str(sphinx_ifelse_version))

#from sphinx_needs import __version__ as sphinx_needs_version
#print ('sphinx-needs version: ' + str(sphinx_needs_version))

from sphinx_ifelse.utils import tags2dict
# -- General configuration ------------------------------------------------

# General information about the project.
project = "Sphinx-IfElse"
now = datetime.datetime.now()
copyright = f"2025-{now.year}, PhilipPartsch"
author = "PhilipPartsch"

master_doc = "index"
language = "en"

version = release = sphinx_ifelse_version

# -- General configuration
on_rtd = os.environ.get("READTHEDOCS") == "True"

extensions = [
   'sphinx_ifelse',
]

#if tags.has('mac'):
#    tags.add("os_MAC")

ifelse_variants = {
   'html': True,
   'latex': False,
   'pdf': False,
   'epub': False,
   'l1': 3,
   'l2': 3,
   'l3': 3,
}


#for key, value in tags2dict(tags).items():
#   ifelse_variants[key] = value

print('ifelse_variants')
print( ifelse_variants)

from sphinx.config import is_serializable

print('is_serializable(ifelse_variants)')
print( is_serializable(ifelse_variants))

from sphinx.config import Config, _Opt, logger
from sphinx.locale import __

def myadd(
        self,
        name: str,
        default: Any,
        rebuild: _ConfigRebuild,
        types: type | Collection[type] | ENUM,
        description: str = '',
    ) -> None:
        if name in self._options:
            raise ExtensionError(__('Config value %r already present') % name)

        # standardise rebuild
        if isinstance(rebuild, bool):
            rebuild = 'env' if rebuild else ''

        # standardise valid_types
        valid_types = _validate_valid_types(types)
        self._options[name] = _Opt(default, rebuild, valid_types, description)

#Config.add = myadd

def __my_getstate__(self) -> dict[str, Any]:
   """Obtains serializable data for pickling."""
   # remove potentially pickling-problematic values from config
   __dict__ = {
      key: value
      for key, value in self.__dict__.items()
      if not key.startswith('_') and is_serializable(value)
   }
   # create a pickleable copy of ``self._options``
   __dict__['_options'] = _options = {}
   for name, opt in self._options.items():
      if not isinstance(opt, _Opt) and isinstance(opt, tuple) and len(opt) <= 3:
            # Fix for Furo's ``_update_default``.
            self._options[name] = opt = _Opt(*opt)
      real_value = getattr(self, name)
      if name == 'ifelse_variants':
         print('---------------1---------------------')
         print('name')
         print(name)
         print('real_value')
         print(real_value)
         print('is_serializable(real_value)')
         print(is_serializable(real_value))
         print('----------------1--------------------')

      if not is_serializable(real_value):
            if opt.rebuild:
               # if the value is not cached, then any build that utilises this cache
               # will always mark the config value as changed,
               # and thus always invalidate the cache and perform a rebuild.
               logger.warning(
                  __(
                        'cannot cache unpickleable configuration value: %r '
                        '(because it contains a function, class, or module object)'
                  ),
                  name,
                  type='config',
                  subtype='cache',
                  once=True,
               )
            # omit unserializable value
            real_value = None
      # valid_types is also omitted
      _options[name] = real_value, opt.rebuild
      if name == 'ifelse_variants':
         print('---------------2---------------------')
         print('name')
         print(name)
         print('real_value')
         print(real_value)
         print('is_serializable(real_value)')
         print(is_serializable(real_value))
         print('_options[name]')
         print(_options[name])
         print('is_serializable(_options[name])')
         print(is_serializable(_options[name]))
         print('----------------2--------------------')

   return __dict__

#Config.__getstate__ = __my_getstate__
