import os
import pytest
import tempfile
from sphinx.application import Sphinx

def test_docu_generation():

   # Create a temporary directory for the Sphinx build
   with tempfile.TemporaryDirectory() as temp_dir:
      src_dir = os.path.join(temp_dir, "source")
      build_dir = os.path.join(temp_dir, "build")
      os.makedirs(src_dir)

      # Create a minimal Sphinx configuration
      conf_py = """
project = 'Test Project'
extensions = ['sphinx_ifelse']
ifelse_variants = {
    'VARIANT1': True,
    'VARIANT2': False,
}

"""
      with open(os.path.join(src_dir, "conf.py"), "w") as f:
         f.write(conf_py)

      # Create a test reStructuredText file
      index_rst = """
.. if:: VARIANT1

   This content is included.

.. elif:: VARIANT2

   This content is excluded.

.. else::

   This content is also excluded.

"""
      with open(os.path.join(src_dir, "index.rst"), "w") as f:
         f.write(index_rst)

      # Run Sphinx build
      app = Sphinx(src_dir, src_dir, build_dir, build_dir, "html")
      app.build()

      # Verify the output
      output_file = os.path.join(build_dir, "index.html")
      assert os.path.exists(output_file)
      with open(output_file, "r") as f:
         output_content = f.read()
         assert "This content is included." in output_content
         assert "This content is excluded." not in output_content
         assert "This content is also excluded." not in output_content

