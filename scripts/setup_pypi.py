#!/usr/bin/env python3
"""
PyPI Publishing Setup Helper
Helps configure credentials and validate setup for publishing to PyPI.
"""

import os
import sys
from pathlib import Path


def check_pypirc():
    """Check if ~/.pypirc exists and is configured."""
    pypirc_path = Path.home() / ".pypirc"
    
    if not pypirc_path.exists():
        print("❌ ~/.pypirc not found")
        return False
        
    content = pypirc_path.read_text()
    
    if "pypi" not in content:
        print("❌ ~/.pypirc missing PyPI configuration")
        return False
        
    if "YOUR_ACTUAL" in content:
        print("❌ ~/.pypirc contains placeholder tokens")
        return False
        
    print("✅ ~/.pypirc looks configured")
    return True


def check_build_tools():
    """Check if required build tools are installed."""
    try:
        import build
        import twine
        print("✅ Build tools (build, twine) are installed")
        return True
    except ImportError as e:
        print(f"❌ Missing build tools: {e}")
        print("   Run: pip install build twine")
        return False


def create_pypirc_template():
    """Create a template ~/.pypirc file."""
    pypirc_path = Path.home() / ".pypirc"
    
    template = """[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR_ACTUAL_PYPI_TOKEN_HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR_ACTUAL_TESTPYPI_TOKEN_HERE
"""
    
    if pypirc_path.exists():
        print(f"⚠️  ~/.pypirc already exists. Backup created as ~/.pypirc.backup")
        (Path.home() / ".pypirc.backup").write_text(pypirc_path.read_text())
    
    pypirc_path.write_text(template)
    pypirc_path.chmod(0o600)  # Secure permissions
    
    print("✅ Created ~/.pypirc template")
    print("📝 Edit ~/.pypirc and replace YOUR_ACTUAL_*_TOKEN_HERE with real tokens")


def main():
    """Main setup helper."""
    print("🚀 PyPI Publishing Setup Helper")
    print("=" * 40)
    
    # Check current status
    has_pypirc = check_pypirc()
    has_tools = check_build_tools()
    
    print("\n📋 Setup Status:")
    print(f"   PyPI config: {'✅' if has_pypirc else '❌'}")
    print(f"   Build tools: {'✅' if has_tools else '❌'}")
    
    if not has_tools:
        print("\n❗ Please install build tools first:")
        print("   pip install build twine")
        sys.exit(1)
    
    if not has_pypirc:
        print("\n❓ Create ~/.pypirc template? [y/N]", end=" ")
        if input().lower().startswith('y'):
            create_pypirc_template()
    
    print("\n🎯 Next Steps:")
    print("1. Get API tokens from:")
    print("   • PyPI: https://pypi.org/manage/account/token/")
    print("   • Test PyPI: https://test.pypi.org/manage/account/token/")
    print("2. Edit ~/.pypirc with your actual tokens")
    print("3. Run: make build check-dist upload-test")
    print("4. If test works: make upload")
    
    if has_pypirc and has_tools:
        print("\n🎉 Setup looks complete!")
        print("   Ready to publish with: make build upload-test upload")


if __name__ == "__main__":
    main()