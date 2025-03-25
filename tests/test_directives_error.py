import os
import pytest
from sphinx.application import Sphinx

def test_error_project():

   # Get test project dir
   current_dir = os.path.dirname(os.path.abspath(__file__))
   project_dir = os.path.join(current_dir, "error_project")
   src_dir = os.path.join(project_dir, "source")
   build_dir = os.path.join(project_dir, "build")

   # Run Sphinx build
   app = Sphinx(src_dir, src_dir, build_dir, build_dir, "html")
   app.build()
   status = app.statuscode
   assert 0 == status

   warning_list = app._warning

   # Verify the output
   output_file_index = os.path.join(build_dir, "index.html")
   assert os.path.exists(output_file_index)

   output_file_elif_error = os.path.join(build_dir, "error.html")
   assert os.path.exists(output_file_elif_error)
   with open(output_file_elif_error, "r") as f:
      output_content = f.read()

      assert "<p>IfDirective /Undefined element in condition/ text shall be in the output." in output_content
      assert "<p>IfDirective /Empty condition/ text shall not be in the output." not in output_content
      assert "<p>ElIfDirective /Undefined element in condition/ text before shall not be in the output." not in output_content
      assert "<p>ElIfDirective /Undefined element in condition/ text shall be in the output." in output_content
      assert "<p>ElIfDirective /Empty condition/ text before shall not be in the output." not in output_content
      assert "<p>ElIfDirective /Empty condition/ text shall not be in the output." not in output_content
      assert "<p>ElIfDirective /Missing IfDirective before ElIfDirective with evaluating to True/ text shall be in the output." in output_content
      assert "<p>ElIfDirective /Missing IfDirective before ElIfDirective with evaluating to False/ text shall not be in the output." not in output_content
      assert "<p>ElseDirective /Missing IfDirective before ElseDirective/ text shall be in the output." in output_content
